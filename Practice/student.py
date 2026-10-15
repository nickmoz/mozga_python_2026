class Student:
    def __init__(self, name, major):
        print("Constructor is called")
        self.name = name
        self.major = major
        self.courses = {}

    def add_course(self, course, grade):
        if 0 < grade < 100:
            self.courses[course] = grade
        else:
            print(f"Grade {grade} is invalid")

    def display_courses(self):
        for course in self.courses:
            grade = self.courses[course]
            print(f"{course}, grade: {grade}")

    def __str__(self):
        return f"{self.name}, major: {self.major}"


if __name__ == "__main__":
    a = Student("Bill", "Business")
    print(a)
    c = Student("Mark", "IT")
    print(c)

    c.add_course("Python", 90)
    c.add_course("Java", 82)

    c.display_courses()
