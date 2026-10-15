from student import Student


class UniversityStudent(Student):
    def __init__(self, name, major):
        super().__init__(name, major)
        self.gpa = None

    def set_gpa(self, gpa):
        if 0 <= gpa <= 4:
            self.gpa = gpa

    def __str__(self):
        if self.gpa is None:
            return super.__str__() + f", GPA: {self.gpa}"
        else:
            return super.__str__() + f", GPA: N/A"


if __name__ == "__main__":
    a = UniversityStudent("Jim", "IR")
    a.add_course("sad", 90)
    a.set_gpa(3.7)
    print(a)
