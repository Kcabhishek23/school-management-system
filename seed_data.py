import student
import staff
import fee

# ---------------- SAMPLE STUDENTS ----------------

student.Student.next_number = 1

s1 = student.Student("Antti Kokala", 24, "aamk05@student.hamk.fi", "ICT Robotics",
                      "3rd Year", "0449841234", "Riihimaki",
                      "Lindu Kokala", "0667598123")
student.students.append(s1)

s2 = student.Student("Alexi Rawat", 26, "amk078@student.hamk.fi", "ICT Robotics",
                      "3rd Year", "0449842345", "Hameenlinna",
                      "Sita Rawat", "0667598234")
student.students.append(s2)

s3 = student.Student("Maria Silva", 22, "msilva@student.hamk.fi", "Business",
                      "2nd Year", "0449843456", "Helsinki",
                      "Carlos Silva", "0667598345")
student.students.append(s3)

s4 = student.Student("John Doe", 21, "jdoe@student.hamk.fi", "IT",
                      "1st Year", "0449844567", "Tampere",
                      "Jane Doe", "0667598456")
student.students.append(s4)

s5 = student.Student("Priya Sharma", 23, "psharma@student.hamk.fi", "ICT Robotics",
                      "3rd Year", "0449845678", "Espoo",
                      "Raj Sharma", "0667598567")
student.students.append(s5)

student.save_students()
print("Sample students saved.")


# ---------------- SAMPLE STAFF ----------------

staff.Staff.next_number = 1

st1 = staff.Staff("Randu Subedi", 35, "Male", "Robotics", "Teacher",
                   "M.Sc Robotics", "ram@school.fi", "0501112233",
                   "Riihimaki", "2018-06-01", 3500)
staff.staffs.append(st1)

st2 = staff.Staff("Jesi Pinkman", 37, "Male", "Mathematics", "Teacher",
                   "M.Sc Mathematics", "fernando@school.fi", "0501112244",
                   "Hameenlinna", "2017-08-15", 3600)
staff.staffs.append(st2)

st3 = staff.Staff("Anna Korhonen", 40, "Female", "English", "Head Teacher",
                   "M.A English", "anna@school.fi", "0501112255",
                   "Helsinki", "2015-01-10", 4200)
staff.staffs.append(st3)

st4 = staff.Staff("Mikko Virtanen", 29, "Male", "Physical Education", "Teacher",
                   "B.Sc Sports Science", "mikko@school.fi", "0501112266",
                   "Tampere", "2021-09-01", 3100)
staff.staffs.append(st4)

st5 = staff.Staff("Sara Lindholm", 33, "Female", "Administration", "Admin Staff",
                   "B.Com", "sara@school.fi", "0501112277",
                   "Espoo", "2019-03-20", 2800)
staff.staffs.append(st5)

staff.save_staff()
print("Sample staff saved.")


# ---------------- SAMPLE FEE RECORDS ----------------

fee1 = fee.Fee(s1.name, s1.age, s1.email_id, s1.department, s1.student_class,
               s1.phone_no, s1.address, s1.guardian_name, s1.guardian_phone,
               9800, 5000)
fee1.student_id = s1.student_id
fee.fee_students.append(fee1)

fee2 = fee.Fee(s2.name, s2.age, s2.email_id, s2.department, s2.student_class,
               s2.phone_no, s2.address, s2.guardian_name, s2.guardian_phone,
               9800, 9800)
fee2.student_id = s2.student_id
fee.fee_students.append(fee2)

fee3 = fee.Fee(s3.name, s3.age, s3.email_id, s3.department, s3.student_class,
               s3.phone_no, s3.address, s3.guardian_name, s3.guardian_phone,
               8500, 0)
fee3.student_id = s3.student_id
fee.fee_students.append(fee3)

fee.save_fee_students()
print("Sample fee records saved.")

print("\nAll sample data created successfully!")