import student
import staff
import fee

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
student.load_students()
staff.load_staffs()
fee.load_fee_students()


# -----  DASHBOARD SECTION ----------#

@app.route("/")
def home():

    total_students = len(student.students)
    total_staff = len(staff.staffs)

    total_fee_collected = 0
    for fs in fee.fee_students:
        total_fee_collected += fs.paid_fee

    recent_students = student.students[-5:]
    recent_staff = staff.staffs[-5:]

    return render_template(
        "home.html",
        active_page="dashboard",  
        total_students=total_students,
        total_staff=total_staff,
        total_fee_collected=total_fee_collected,
        recent_students=recent_students,
        recent_staff=recent_staff
    )


#----------  FEE SECTION ----------#

@app.route("/fees", methods=["GET", "POST"])
def fees_page():

    message = ""

    if request.method == "POST":

        search_id = request.form["student_id"]
        total_fee = request.form.get("total_fee")

        matched_student = None
        for s in student.students:
            if s.student_id == search_id:
                matched_student = s
                break

        if matched_student:
            new_fee_student = fee.Fee(
                matched_student.name,
                matched_student.age,
                matched_student.email_id,
                matched_student.department,
                matched_student.student_class,
                matched_student.phone_no,
                matched_student.address,
                matched_student.guardian_name,
                matched_student.guardian_phone,
                float(total_fee)
            )
            new_fee_student.student_id = matched_student.student_id
            fee.fee_students.append(new_fee_student)
            fee.save_fee_students()
            message = f"Fee record created for {matched_student.name}"
        else:
            message = "No student found with that ID."

    return render_template(
        "fees.html",
        active_page="fees",
        fee_students=fee.fee_students,
        message=message
    )


@app.route("/pay-fee", methods=["POST"])
def pay_fee():

    search_id = request.form["student_id"]
    amount = float(request.form["amount"])

    for fs in fee.fee_students:
        if fs.student_id == search_id:
            fs.pay_fee(amount)
            fee.save_fee_students()
            break

    return redirect("/fees")


#---------  MANAGE STUDENT SECTION ------------#

@app.route("/students", methods=["GET", "POST"])
def students_page():

    message = ""

    if request.method == "POST":

        name = request.form["name"]

        if student.is_duplicate_name(name):

            message = "A student with this name already exists."

        else:

            age = int(request.form["age"])
            email_id = request.form["email_id"]
            department = request.form["department"]
            student_class = request.form["student_class"]
            phone_no = request.form["phone_no"]
            address = request.form["address"]
            guardian_name = request.form["guardian_name"]
            guardian_phone = request.form["guardian_phone"]

            new_student = student.Student(
                name, age, email_id, department, student_class,
                phone_no, address, guardian_name, guardian_phone
            )

            student.students.append(new_student)
            student.save_students()
            message = f"Student added successfully with ID: {new_student.student_id}"

    return render_template(
        "students.html",
        active_page="students",
        students=student.students,
        message=message
    )

#-------------- MANAGE STAFF SECTION --------------#

@app.route("/staff", methods=["GET", "POST"])
def staff_page():

    message = ""

    if request.method == "POST":

        name = request.form["name"]
        age = int(request.form["age"])
        gender = request.form["gender"]
        subject = request.form["subject"]
        position = request.form["position"]
        qualification = request.form["qualification"]
        email = request.form["email"]
        phone = request.form["phone"]
        address = request.form["address"]
        joining_date = request.form["joining_date"]
        salary = float(request.form["salary"])

        new_staff = staff.Staff(
            name, age, gender, subject, position, qualification,
            email, phone, address, joining_date, salary
        )

        staff.staffs.append(new_staff)
        staff.save_staff()
        message = f"Staff added successfully with ID: {new_staff.staff_id}"

    return render_template(
        "staff.html",
        active_page="staff", 
        staffs=staff.staffs,
        message=message
    )


#------------- STAFF SALARY SECTION -------------#

@app.route("/salary")
def salary_page():
    return render_template(
        "salary.html",
        active_page="salary",  
        staffs=staff.staffs
    )


@app.route("/pay-salary", methods=["POST"])
def pay_salary():

    search_id = request.form["staff_id"]
    amount = float(request.form["amount"])

    for st in staff.staffs:
        if st.staff_id == search_id:
            st.pay_salary(amount)
            staff.save_staff()
            break

    return redirect("/salary")



if __name__ == "__main__":
    app.run(debug=True)


#----  TO CHECK IN YOUR TERMINAL JUST COMMENT THE UPSIDE CODE

# while True:

#     print()
#     print("========== SCHOOL MANAGEMENT SYSTEM ==========")
#     print()

#     print("Press 1: Show Students")
#     print("Press 2: Add Student")
#     print("Press 3: Show Staff")
#     print("Press 4: Add Staff")
#     print("Press 5: Search Student")
#     print("Press 6: Search Staff")
#     print("Press 7: Save Students")
#     print("Press 8: Save Staff")
#     print("Press 9: Load Students")
#     print("Press 10: Load Staff")
#     print("Press 11: Total Fee Collection")
#     print("Press 12: Add Fee Student")
#     print("Press 13: Show Fee Students")
#     print("Press 14: Search Fee Student")
#     print("Press 15: Pay Fee")
#     print("Press 16: Save Fee Records")
#     print("Press 17: Load Fee Records")
#     print("Press 18: Pay Salary")
#     print("Press 19: Exit")

#     print()

#     choice = input("Enter your choice: ")
#     print()

#     if choice == "1":
#         student.show_student()

#     elif choice == "2":
#         student.add_student()

#     elif choice == "3":
#         staff.show_staff()

#     elif choice == "4":
#         staff.add_staff()

#     elif choice == "5":
#         student.search_student()

#     elif choice == "6":
#         staff.search_staff()

#     elif choice == "7":
#         student.save_students()

#     elif choice == "8":
#         staff.save_staff()

#     elif choice == "9":
#         student.load_students()

#     elif choice == "10":
#         staff.load_staffs()

#     elif choice == "11":
#         fee.total_fee_collection()

#     elif choice == "12":
#         fee.add_fee_student()

#     elif choice == "13":
#         fee.show_fee_students()

#     elif choice == "14":
#         fee.search_fee_student()

#     elif choice == "15":
#         fee.pay_fee_for_student()

#     elif choice == "16":
#         fee.save_fee_students()

#     elif choice == "17":
#         fee.load_fee_students()

#     elif choice == "18":
#         staff.pay_salary_for_staff()

#     elif choice == "19":
#         print("Have a good day buddy!")
#         break

#     else:
#         print("Invalid input!!!")