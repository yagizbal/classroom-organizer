#one_gene = [0,#index of class
#            2, #index of teacher
#            3, #index of day
#            (9,10), #start and end hour
#            2, #allocated hours           
#            ]

classes = ["Maths","Physics","Chemistry","Biology"]
teachers = ["Adams","Baker","Clark","Davis"] #the teachers of a class are held in the same index as the class
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
hours = [i for i in range(0,24)]
faculties_rooms = [["Faculty of Science",["Room 1","Room 2","Room 3"]],
                   ["Faculty of Arts",["Room 4","Room 5","Room 6"]],
                   ["Faculty of Engineering",["Room 7","Room 8","Room 9"]]]

def gene_generator(class_number, days):
    max_hours = 5
    allocated_hours = random.randrange(1,max_hours)

    free_days = [3,5,6]
    work_days = [i for i in range(days) if int(i%7) not in free_days]
    chosen_day = random.choice(work_days)

    work_hours = (8,18)
    begin = (random.randrange(work_hours[0],work_hours[1]))
    start_end_hour = (begin,begin+allocated_hours)

    gene = [class_number, chosen_day, start_end_hour, allocated_hours]
