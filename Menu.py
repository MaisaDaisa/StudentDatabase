from Student import Student
from StudentDatabase import StudentDatabase


def menu():
    db = StudentDatabase('students.db')

    print("შენ შეგიძლია სტუდენტის შექმნა, შეცვლა, წაშლა, ნახვა")
    print("შექმნისათვის დაწერე 1")
    print("განახლებისთვის დაწერე 2")
    print("წაშლა - 3")
    print("ნახვა - 4")
    print("END terminates program")

    choice = input("შენი არჩევანი: ")

    if choice == "1":
        name = input("Name: ")
        last_name = input("Last name: ")
        gpa = float(input("GPA: "))
        faculty = input("Faculty: ")
        db.add_student(Student(name, last_name, gpa, faculty))
        print("Student has been added to the database")
    elif choice == "2":
        name = input("Name: ")
        last_name = input("Last name: ")
        gpa = float(input("GPA: "))
        faculty = input("Faculty: ")
        db.update_student(last_name, Student(name, last_name, gpa, faculty))
        print("Student has been updated")
    elif choice == "3":
        id = input("id: ")
        db.delete_student(id)
        print("Student has been deleted")
    elif choice == "4":
        id = input("id: ")
        print(db.get_student(id).name)
    elif choice == "END":
        return True
    else:
        return False


while True:
    if menu():
        break
