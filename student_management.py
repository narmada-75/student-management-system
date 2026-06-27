"""students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update")
    print("5. Delete student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        age = input("Enter Age: ")

        student = {
            "Name": name,
            "Roll": roll,
            "Age": age
        }

        students.append(student)

        print("✅ Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\n----- Student Records -----")
            for student in students:
                print(f"Name : {student['Name']}")
                print(f"Roll : {student['Roll']}")
                print(f"Age  : {student['Age']}")
                print("--------------------------")
                
    elif choice == "3":
         Roll = input("Enter Roll Number to search: ")

         found = False

         for student in students:
            if student["Roll"] == roll:
                print("\nStudent Found")
                print(f"Name : {student['Name']}")
                print(f"Roll : {student['Roll']}")
                print(f"Age  : {student['Age']}")
                found = True
                break

         if not found:
            print("Student not found.")
   
    elif choice == "4":
        roll = input("Enter Roll Number to update: ")

        found = False

        for student in students:
            if student["Roll"] == roll:
                 print("Student Found!")

                 student["Name"] = input("Enter New Name: ")
                 student["Age"] = input("Enter New Age: ")

                 print("✅ Student updated successfully!")
                 found = True
                 break

        if not found:
            print("Student not found.")            
    elif choice == "5":
        roll = input("enter roll number to delete: ")
        found = False
        for student in students:
            if student["Roll"]== roll:
                students.remove(student)
                print("student deleted successfully")
                found = True
                break
        if not found:
            print("student not found:")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")"""




import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql password",  # Replace with your MySQL password
    database="student_db"
)

cursor = connection.cursor()

while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        query = "INSERT INTO students (roll, name, age) VALUES (%s, %s, %s)"
        values = (roll, name, age)

        try:
            cursor.execute(query, values)
            connection.commit()
            print(" Student added successfully!")
        except mysql.connector.Error as err:
            print("Error:", err)

    # View Students
    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if len(students) == 0:
            print("No student records found.")
        else:
            print("\n----- Student Records -----")
            for student in students:
                print(f"Roll Number : {student[0]}")
                print(f"Name        : {student[1]}")
                print(f"Age         : {student[2]}")
                print("---------------------------")

    # Search Student
    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        query = "SELECT * FROM students WHERE roll=%s"
        cursor.execute(query, (roll,))
        student = cursor.fetchone()

        if student:
            print("\nStudent Found")
            print(f"Roll Number : {student[0]}")
            print(f"Name        : {student[1]}")
            print(f"Age         : {student[2]}")
        else:
            print("Student not found.")

    # Update Student
    elif choice == "4":
        roll = input("Enter Roll Number to Update: ")

        query = "SELECT * FROM students WHERE roll=%s"
        cursor.execute(query, (roll,))
        student = cursor.fetchone()

        if student:
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))

            query = "UPDATE students SET name=%s, age=%s WHERE roll=%s"
            cursor.execute(query, (name, age, roll))
            connection.commit()

            print(" Student updated successfully!")
        else:
            print("Student not found.")

    # Delete Student
    elif choice == "5":
        roll = input("Enter Roll Number to Delete: ")

        query = "SELECT * FROM students WHERE roll=%s"
        cursor.execute(query, (roll,))
        student = cursor.fetchone()

        if student:
            query = "DELETE FROM students WHERE roll=%s"
            cursor.execute(query, (roll,))
            connection.commit()

            print("Student deleted successfully!")
        else:
            print("Student not found.")

    # Exit
    elif choice == "6":
        cursor.close()
        connection.close()
        print("Thank you! Exiting...")
        break

    else:
        print(" Invalid choice. Please try again.")