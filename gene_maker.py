import random
import class_infos

def create_gene(lecture, semester, day, hour, room):
    return [lecture, semester, day, hour, room]


def create_genes(semester_info, lecture_series, days_to_avoid, daily_hours_limit, same_class_daily_hours_limit, faculties, hours_to_avoid, prefer_hours_to_avoid):
    length_of_semester, target_semester = semester_info
    genes = []

    for semester, subjects in lecture_series.items():
        if semester != target_semester:
            continue

        for subject, info in subjects.items():
            for _ in range(info["hours"]):
                valid_gene = False
                while not valid_gene:
                    day = random.randint(0, length_of_semester - 1)
                    hour = random.randint(0, 23)

                    # Find the appropriate faculty for the subject
                    faculty_name = None
                    for faculty, faculty_info in faculties.items():
                        if subject in faculty_info["subjects"]:
                            faculty_name = faculty
                            break

                    # Access the appropriate lecturers and lecture halls from the faculty dictionary
                    room = random.choice(faculties[faculty_name]["lecture_halls"])
                    lecturer = random.choice(faculties[faculty_name]["subjects"][subject])

                    # Check if day, hour, and room are valid for this gene
                    if day not in days_to_avoid and not any(start <= hour <= end for start, end in hours_to_avoid):
                        valid_gene = True

                        # Check if there are already same_class_daily_hours_limit scheduled for the same class on the same day
                        same_class_same_day_count = sum(1 for gene in genes if gene[0]["name"] == subject and gene[2] == day)
                        if same_class_same_day_count >= same_class_daily_hours_limit:
                            valid_gene = False

                        # Check if there are already daily_hours_limit scheduled for any class on the same day
                        hours_same_day_count = sum(1 for gene in genes if gene[2] == day)
                        if hours_same_day_count >= daily_hours_limit:
                            valid_gene = False

                    # Check for preferentially avoided hours
                    if valid_gene and any(start <= hour <= end for start, end in prefer_hours_to_avoid):
                        if random.random() < 0.5:
                            valid_gene = False

                    if valid_gene:
                        gene = [{"name": subject, "lecturers": faculties[faculty_name]["subjects"][subject]}, day, hour, room, lecturer]
                        genes.append(gene)

    return genes



def print_genes(genes, start_day, end_day, current_semester, dates=None, semester_start=None):
    output = []
    if semester_start:
        output.append(f"Semester starts on {semester_start}.")
    output.append(f"Query date range: {dates[start_day]} to {dates[end_day]}")
    
    for gene in genes:
        day = gene[1]
        if start_day <= day <= end_day:
            lecture_name = gene[0]['name']
            semester = current_semester
            hour = gene[2]
            room = gene[3]

            days_after_query_start = day - start_day

            if dates:
                date_string = dates[day]
                output.append(f"{lecture_name} (Semester {semester}) is scheduled on {date_string} ({days_after_query_start} days after query start) at hour {hour} in room {room}.")
            else:
                output.append(f"{lecture_name} (Semester {semester}) is scheduled on day {day} ({days_after_query_start} days after query start) at hour {hour} in room {room}.")
    return '\n'.join(output)

