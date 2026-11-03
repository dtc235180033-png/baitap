
students = []

def add_student(student_id, name):
    student = {
        "id": student_id,
        "name": name
    }

    students.append(student)
    print("Them sinh vien thanh cong!")

add_student("SV001", "Nguyen Van A")
add_student("SV002", "Tran Thi B")

print("Danh sach sinh vien:")
for student in students:
    print(student)
