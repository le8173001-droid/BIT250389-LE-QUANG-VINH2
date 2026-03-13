class Student:
    def __init__(self, ten, diem):
        self.ten = ten

        if 0 <= diem <= 10:
            self.diem = diem
        else:
            raise ValueError("Điểm phải nằm trong khoảng 0–10")

    def display(self):
        print(f"Sinh viên {self.ten} có điểm là {self.diem}")
hoc_sinh1 = Student("VŨ", 5)
hoc_sinh2 = Student("CHÂU", 8)

print(hoc_sinh1.ten, hoc_sinh1.diem)
print(hoc_sinh2.ten, hoc_sinh2.diem)
hoc_sinh1.display()
hoc_sinh2.display()