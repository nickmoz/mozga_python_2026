import sqlite3

# connect to the database
db = sqlite3.connect("school.db")
cursor = db.cursor()

# create a students table
cursor.execute("""CREATE TABLE IF NOT EXISTS students
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, grade INTEGER)""")

# create a menu to add, view, delete a student and edit a grade
choice = -1
while choice != 0:
    print("1. Add Student")
    print("2. Display All")
    print("3. Change Student's Grade")
    print("4. Delete Student")
    print("0. Exit")
    choice = int(input("Select > "))

    if choice == 1:
        name = input("Name: ")
        grade = int(input("Grade: "))
        cursor.execute("""
                        INSERT INTO students (name, grade) VALUES (?, ?)""", (name, grade))
        db.commit()
    elif choice == 2:
        print("ALL STUDENTS")
        students = cursor.execute("SELECT * FROM students").fetchall()
        for row in students:
            print(f"ID: {row[0]}, NAME: {row[1]}, Grade: {row[2]}")
    elif choice == 3:
        id = int(input("ID of the student: "))
        grade = int(input("New Grade: "))
        cursor.execute("UPDATE students SET grade=? WHERE id=?", (grade, id))
        rows_affected = cursor.rowcount
        if rows_affected == 0:
            print("ID not found")
        else:
            db.commit()
    elif choice == 4:
        id = int(input("ID of the student to be deleted: "))
        answer = input("Are you sure (Y/N)?: ")
        if answer == 'Y':
            cursor.execute("DELETE FROM students WHERE id=?", (id,))
            rows_affected = cursor.rowcount
            if rows_affected == 0:
                print("ID not found")
            else:
                db.commit()


db.close()
