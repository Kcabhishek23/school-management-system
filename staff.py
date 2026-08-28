import json

class Staff:

    school_code = "0068"
    next_number = 1

    def __init__(self, name, age, gender, subject, position, qualification,
                 email, phone, address, joining_date, salary, paid_salary=0):

        self.staff_id = "S" + Staff.school_code + str(Staff.next_number)
        Staff.next_number += 1

        self.name = name
        self.age = age
        self.gender = gender
        self.subject = subject
        self.position = position
        self.qualification = qualification
        self.email = email
        self.phone = phone
        self.address = address
        self.joining_date = joining_date
        self.salary = salary
        self.paid_salary = paid_salary

    @property
    def due_salary(self):
        return self.salary - self.paid_salary

    @property
    def salary_status(self):
        if self.paid_salary == 0:
            return "Not Paid"
        elif self.paid_salary < self.salary:
            return "Partially Paid"
        else:
            return "Fully Paid"

    def pay_salary(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.due_salary:
            print(f"Amount exceeds due salary. Due: {self.due_salary}")
        else:
            self.paid_salary += amount
            print(f"Payment successful. Remaining due: {self.due_salary}")

    def introduce_staff(self):
        print(f"Staff ID: {self.staff_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Subject: {self.subject}")
        print(f"Position: {self.position}")
        print(f"Qualification: {self.qualification}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"Joining Date: {self.joining_date}")
        print(f"Salary: {self.salary}")
        print(f"Paid Salary: {self.paid_salary}")
        print(f"Due Salary: {self.due_salary}")
        print(f"Salary Status: {self.salary_status}")
        print()


staffs = []


# SHOW STAFF

def show_staff():
    if not staffs:
        print("No staff found.")
        return
    for staff in staffs:
        staff.introduce_staff()


# ADD STAFF

def add_staff():
    name = input("Enter staff name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    subject = input("Enter subject: ")
    position = input("Enter position: ")
    qualification = input("Enter qualification: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    joining_date = input("Enter joining date: ")
    salary = float(input("Enter salary: "))

    new_staff = Staff(name, age, gender, subject, position, qualification,
                       email, phone, address, joining_date, salary)

    staffs.append(new_staff)
    print(f"Staff added successfully with ID: {new_staff.staff_id}")


# SEARCH STAFF (by ID, not name — same reasoning as Student)

def search_staff():
    search_id = input("Enter staff ID: ")
    found = False

    for staff in staffs:
        if staff.staff_id == search_id:
            staff.introduce_staff()
            found = True
            break

    if not found:
        print("Please enter a valid staff ID.")


# PAY SALARY FOR STAFF

def pay_salary_for_staff():
    search_id = input("Enter staff ID: ")

    for staff in staffs:
        if staff.staff_id == search_id:
            amount = float(input("Enter payment amount: "))
            staff.pay_salary(amount)
            return

    print("Please enter a valid staff ID.")


# SAVE STAFF

def save_staff():
    staff_data = []

    for staff in staffs:
        data = {
            "staff_id": staff.staff_id,
            "name": staff.name,
            "age": staff.age,
            "gender": staff.gender,
            "subject": staff.subject,
            "position": staff.position,
            "qualification": staff.qualification,
            "email": staff.email,
            "phone": staff.phone,
            "address": staff.address,
            "joining_date": staff.joining_date,
            "salary": staff.salary,
            "paid_salary": staff.paid_salary
        }
        staff_data.append(data)

    with open("data/staffs.json", "w") as file:
        json.dump(staff_data, file, indent=4)

    print("Staff saved successfully.")


# LOAD STAFF

def load_staffs():
    try:
        with open("data/staffs.json", "r") as file:
            staff_data = json.load(file)

        staffs.clear()

        for data in staff_data:
            staff = Staff(
                data["name"], data["age"], data["gender"], data["subject"],
                data["position"], data["qualification"], data["email"],
                data["phone"], data["address"], data["joining_date"],
                data["salary"], data["paid_salary"]
            )
            staff.staff_id = data["staff_id"]
            staffs.append(staff)

        if staffs:
            used_numbers = []
            for s in staffs:
                number_part = s.staff_id.replace("S" + Staff.school_code, "")
                used_numbers.append(int(number_part))
            Staff.next_number = max(used_numbers) + 1

        print("Staff data loaded successfully.")

    except FileNotFoundError:
        print("staffs.json file not found.")