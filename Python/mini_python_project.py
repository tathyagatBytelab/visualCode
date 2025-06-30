students = []
def add_student():
    name = input("Enter the student name : ")
    roll_no = input("Enter the student roll_no : ")
    course = input("Enter the course : ")
    student ={
        "name":name,
        "roll_no":roll_no,
        "course" :course,
        }
    students.append(student)
    print("👨‍🎓✅ Student added successfully!\n")
def view_students():
    if not students:
        print("🗋❌student not found!\n")
    else:
        print("\n All students added list 🚻🚻")
        for student in students :
            print(f"name: {student['name']}, roll_no: {student['roll_no']}, course: {student['course']}")
        print()
def menu():
    while True:
        print("        👨‍🎓👨‍🎓======STUDENTS MANAGEMENT MENU======👨‍🎓👨‍🎓    ")
        print("1. press to add student ")
        print("2. press to view added student ")
        print("3. press to exit ")
        choice = input("Enter you choice (1-3) ").lower()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3" or choice == "exit" :
            print("🫡🫡Hey goodbye , exiting from menu!!")
            break
        else:
            print("❌record not found⁉️❌!!!\n")   
menu()



