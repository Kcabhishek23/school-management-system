import json


class Student:

    school_code = "0068"
    next_number = 1

    def __init__(self, name, age, email_id, department, student_class,
                 phone_no, address, guardian_name, guardian_phone,
                 assign_id=True):

        if assign_id:
            self.student_id = Student.school_code + str(Student.next_number)
            Student.next_number += 1

        self.name = name
        self.age = age
        self.email_id = email_id
        self.department = department
        self.student_class = student_class
        self.phone_no = phone_no
        self.address = address
        self.guardian_name = guardian_name
        self.guardian_phone = guardian_phone

    def introduce(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email ID: {self.email_id}")
        print(f"Department: {self.department}")
        print(f"Class: {self.student_class}")
        print(f"Phone No: {self.phone_no}")
        print(f"Address: {self.address}")
        print(f"Guardian Name: {self.guardian_name}")
        print(f"Guardian Phone: {self.guardian_phone}")


students = []


def is_duplicate_name(name):
    for s in students:
        if s.name.strip().lower() == name.strip().lower():
            return True
    return False


def show_student():
    if not students:
        print("No students found.")
        return
    for student in students:
        student.introduce()
        print()


def add_student():

    name = input("Enter student name: ")

    if is_duplicate_name(name):
        print("A student with this name already exists. Please check before adding.")
        return

    age = int(input("Enter age: "))
    email_id = input("Enter email id: ")
    department = input("Enter student department: ")
    student_class = input("Enter student class: ")
    phone_no = input("Enter phone number: ")
    address = input("Enter address: ")
    guardian_name = input("Enter guardian name: ")
    guardian_phone = input("Enter guardian phone number: ")

    new_student = Student(name, age, email_id, department, student_class,
                           phone_no, address, guardian_name, guardian_phone)
    students.append(new_student)
    print(f"Student added successfully with ID: {new_student.student_id}")


def search_student():
    search_id = input("Enter student ID: ")
    found = False
    for student in students:
        if student.student_id == search_id:
            student.introduce()
            found = True
            break
    if not found:
        print("Please enter a valid Student ID.")


def save_students():
    student_data = []
    for student in students:
        data = {
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "email_id": student.email_id,
            "department": student.department,
            "student_class": student.student_class,
            "phone_no": student.phone_no,
            "address": student.address,
            "guardian_name": student.guardian_name,
            "guardian_phone": student.guardian_phone
        }
        student_data.append(data)

    with open("data/students.json", "w") as file:
        json.dump(student_data, file, indent=4)
    print("Students saved successfully.")


def load_students():
    try:
        with open("data/students.json", "r") as file:
            student_data = json.load(file)

        students.clear()
        for data in student_data:
            student = Student(
                data["name"], data["age"], data["email_id"], data["department"],
                data["student_class"], data["phone_no"], data["address"],
                data["guardian_name"], data["guardian_phone"],
                assign_id=False
            )
            student.student_id = data["student_id"]
            students.append(student)

        if students:
            used_numbers = []
            for s in students:
                number_part = s.student_id.replace(Student.school_code, "")
                used_numbers.append(int(number_part))
            Student.next_number = max(used_numbers) + 1

        print("Students data loaded successfully.")

    except FileNotFoundError:
        print("students.json file not found.")
    except json.JSONDecodeError:
        print("students.json is empty or corrupted.")