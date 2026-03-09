def vi_du1():
    # Tạo tuple thông tin sinh viên
    student = ("VINH", 19, 8.5)

    # Unpack tuple
    name, age, gpa = student

    print("Tên:", name)
    print("Tuổi:", age)
    print("Điểm trung bình:", gpa)
def vi_du2():
    # Dictionary lưu tên và điểm
    scores = {
        "vinh": 8,
        "vuong": 7,
        "vu": 9
    }

    def average_score(score_dict):
        return sum(score_dict.values()) / len(score_dict)

    print("Điểm trung bình:", average_score(scores))
def vi_du3():
    class Car:
        def __init__(self, brand, year):
            self.brand = brand
            self.year = year

    # Tạo đối tượng
    car1 = Car("honda", 2026)

    print("Hãng xe:", car1.brand)
    print("Năm sản xuất:", car1.year)
def vi_du4():
    class Student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

    # Tạo 2 sinh viên
    s1 = Student("Vinh", 8.5)
    s2 = Student("Vu", 7.5)

    # In sinh viên có điểm cao hơn
    if s1.score > s2.score:
        print("Sinh viên điểm cao hơn:", s1.name)
    else:
        print("Sinh viên điểm cao hơn:", s2.name)
def vi_du5():
    class Student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

        def display(self):
            print(f"Tên: {self.name}, Điểm: {self.score}")

    # Ví dụ
    s1 = Student("Vinh", 8.5)
    s2 = Student("Vu", 7.5)

    s1.display()
    s2.display()
def vi_du6():
    class Student:
        def __init__(self, name, score):
            if score < 0 or score > 10:
                raise ValueError("Điểm phải nằm trong khoảng 0–10")
            self.name = name
            self.score = score

        def display(self):
            print(f"Tên: {self.name}, Điểm: {self.score}")

    # ví dụ
    s1 = Student("Vinh", 8.5)
    s1.display()

    # dòng lỗi
    # s2 = Student("Vu", 11)
def vi_du7():
    class Person:
        def __init__(self, age):
            if age <= 0:
                raise ValueError("Tuổi phải lớn hơn 0")
            self.age = age

    # Ví dụ
    p1 = Person(19)
    print("Tuổi:", p1.age)

    # Dòng này sẽ gây lỗi
    # p2 = Person(-3)
vi_du1()
vi_du2()
vi_du3()
vi_du4()
vi_du5()
vi_du6()
vi_du7()





