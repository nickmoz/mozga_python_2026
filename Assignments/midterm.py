import sqlite3

db = sqlite3.connect("midterm.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contacts
                (name TEXT PRIMARY KEY, phone TEXT NOT NULL, email TEXT)""")

print("Enter your 4-digit pin to access the Contacts app")
pin = input("PIN: ")

if len(pin) != 4:
    print("Invalid PIN!")
else:
    choice = -1
    while choice != 0:
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search for Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("0. Exit")
        choice = int(input("SELECT: "))

        if choice == 1:
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            cursor.execute("""
                            INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)""", (name, phone, email))
            db.commit()

        elif choice == 2:
            print("--- ALL CONTACTS ---")
            contacts = cursor.execute("SELECT * FROM contacts").fetchall()
            for row in contacts:
                print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")

        elif choice == 3:
            name = input("Name of contact: ")
            contacts = cursor.execute(
                "SELECT phone, email FROM contacts WHERE name =?", (name,)).fetchall()
            for row in contacts:
                print(f"Phone: {row[0]}, Email: {row[1]}")

        elif choice == 4:
            name = input("Name of contact you would like to edit: ")
            phone = input("New Phone: ")
            email = input("New Email: ")
            cursor.execute(
                "UPDATE contacts SET phone=? WHERE name=?", (phone, name))
            cursor.execute(
                "UPDATE contacts SET email=? WHERE name=?", (email, name))
            rows_affected = cursor.rowcount
            if rows_affected == 0:
                print("Name not found in contacts.")
            else:
                db.commit()

        elif choice == 5:
            name = input("Name of the contact you would like to delete: ")
            confirm = input("Are you sure (Y/N)?: ")
            if confirm == "Y":
                cursor.execute("DELETE FROM contacts WHERE name=?", (name,))
                rows_affected = cursor.rowcount
                if rows_affected == 0:
                    print("Name not found in contacts.")
                else:
                    db.commit()


db.close()
