import json
from student import Student, students


class Fee(Student):

    def __init__(self, name, age, email_id, department, student_class,
                 phone_no, address, guardian_name, guardian_phone,
                 total_fee, paid_fee=0):

        super().__init__(name, age, email_id, department, student_class,
                          phone_no, address, guardian_name, guardian_phone,
                          assign_id=False)

        self.total_fee = total_fee
        self.paid_fee = paid_fee

    @property
    def due_fee(self):
        return self.total_fee - self.paid_fee

    def pay_fee(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.due_fee:
            print(f"Amount exceeds due fee. Due: {self.due_fee}")
        else:
            self.paid_fee += amount
            print(f"Payment successful. Remaining due: {self.due_fee}")

    def show_fee_status(self):
        self.introduce()
        print(f"Total Fee: {self.total_fee}")
        print(f"Paid Fee: {self.paid_fee}")
        print(f"Due Fee: {self.due_fee}")
        if self.paid_fee == 0:
            print("Status: Not Paid")
        elif self.paid_fee < self.total_fee:
            print("Status: Partially Paid")
        else:
            print("Status: Fully Paid")
        print()


fee_students = []


def add_fee_student():
    search_id = input("Enter student ID: ")
    for student in students:
        if student.student_id == search_id:
            total_fee = float(input("Enter total fee: "))
            new_fee_student = Fee(
                student.name, student.age, student.email_id, student.department,
                student.student_class, student.phone_no, student.address,
                student.guardian_name, student.guardian_phone, total_fee
            )
            new_fee_student.student_id = student.student_id
            fee_students.append(new_fee_student)
            print(f"Fee record created for {student.name} (ID: {student.student_id})")
            return
    print("Please enter a valid student ID.")


def show_fee_students():
    if not fee_students:
        print("No fee records found.")
        return
    for student in fee_students:
        student.show_fee_status()


def search_fee_student():
    search_id = input("Enter student ID: ")
    for student in fee_students:
        if student.student_id == search_id:
            student.show_fee_status()
            return student
    print("Please enter a valid student ID.")
    return None


def pay_fee_for_student():
    student = search_fee_student()
    if student is not None:
        amount = float(input("Enter payment amount: "))
        student.pay_fee(amount)


def get_fee_status_for(student_id):
    for fee_student in fee_students:
        if fee_student.student_id == student_id:
            if fee_student.paid_fee == 0:
                return "Not Paid"
            elif fee_student.paid_fee < fee_student.total_fee:
                return "Partially Paid"
            else:
                return "Fully Paid"
    return "No fee record"


def save_fee_students():
    fee_data = []
    for student in fee_students:
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
            "guardian_phone": student.guardian_phone,
            "total_fee": student.total_fee,
            "paid_fee": student.paid_fee
        }
        fee_data.append(data)

    with open("data/fees.json", "w") as file:
        json.dump(fee_data, file, indent=4)
    print("Fee records saved successfully.")


def load_fee_students():
    try:
        with open("data/fees.json", "r") as file:
            fee_data = json.load(file)

        fee_students.clear()
        for data in fee_data:
            student = Fee(
                data["name"], data["age"], data["email_id"], data["department"],
                data["student_class"], data["phone_no"], data["address"],
                data["guardian_name"], data["guardian_phone"],
                data["total_fee"], data["paid_fee"]
            )
            student.student_id = data["student_id"]
            fee_students.append(student)

        print("Fee data loaded successfully.")

    except FileNotFoundError:
        print("fees.json file not found.")
    except json.JSONDecodeError:
        print("fees.json is empty or corrupted.")


def total_fee_collection():
    total = 0
    for student in fee_students:
        total += student.paid_fee
    print(f"Total Fee Collected: {total}")