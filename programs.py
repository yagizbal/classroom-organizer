class Program:
    def __init__(self, name, ects_requirement, duration_in_semesters, subjects):
        self.name = name
        self.ects_requirement = ects_requirement
        self.duration_in_semesters = duration_in_semesters
        self.subjects = subjects

    def __repr__(self):
        return f"{self.name} (ECTS: {self.ects_requirement}, Duration: {self.duration_in_semesters} semesters)"

    def get_subjects_for_semester(self, semester):
        return self.subjects.get(semester, [])
