from student import Student
from university_student import UniversityStudent

if __name__ == "__main__":

    students = []

    students.append(Student("Bob", "IT"))
    students.append(UniversityStudent("Nick", "Psychology"))

    for student in students:
        print(student)

    print("DONE")
