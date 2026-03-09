def vi_du1():
    coordinatees = (10.0, 20.0)
    x, y = coordinatees
    print(f"{x}, Y:  {y}")
def vi_du2():
    # Represents a student with multiple variable
    name = input("Name: ")
    house = input("House: ")
    print(f"{name} from {house}")
def vi_du3():
    # Modularizes getting student's name and house
    def main():
        name = get_name()
        house = get_house()
        print(f"{name} from {house}")
    def get_name():
        name = input('Name:')
    def get_house():
        house = input('House:')
    if __name__ == '__main__':
        main()
def vi_du4():
    # Returns student as tuple, unpacking it
    def main():
        name, house = get_stdent()
        print(f"{name} from {house}")
    def get_stdent():
        name = input('Name:')
        house = input('House:')
        return name, house
    if __name__ == '__main__':
        main()
def vi_du5():
    # Stores student as (mutable) list
    def main():
        student = get_student()
        if student[0] == "Padma":
            student[1] = "Ravenlaw"
        print(f"{student[0]} from {student[1]}")
    def get_student():
        name = input('Name:')
        house = input('House:')
        return [name, house]
    if __name__ == '__main__':
        main()
def vi_du6():
    # Adds __init__
    class Stdent:
        def __init__(self, name, house):
            self.name = name
            self.house = house
    def main():
        student = get_student()
        print(f"{student.name} from {student.house}")
    def get_student():
        name = input('Name:')
        house = input('House:')
        student = student(name, house)
        return student
    if __name__ == '__main__':
        main()
vi_du6()