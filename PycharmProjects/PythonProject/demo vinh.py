def vi_du1():
    s1 = 'Hello Gà Rán'
    s2 = "Hello Trà Sữa"
    s3 = """Hôm qua tát nước đầu đình 
    Gặp cô em gái đẹp xinh mỉm cười 
    Tôi về thẫn thờ cả người 
    Quên luôn lối rẽ, quên lời mẹ răn"""
    s4  = '''Cha mẹ thói đời ăn ở bạc 
    có chồng hờ hững cũng như không'''
    print(s1)
    print(s2)
    print(s3)
    print(s4)
def vi_du2():
    name ="lE quanG vinh"
    print(name.upper())
    name2="Le quanG vinh"
    print(name2.lower())
def vi_du3():
    word ="ABCD"
    print(word.rjust(10,"*"))
    print(word.rjust(3,"*"))
    print(word.rjust(15,"*"))
    print(word.ljust(10))
def vi_du4():
    word="RONALDO"
    print(word.ljust(10))
    print(word.ljust(10,"*"))
    print(word.ljust(15,"*"))
    print(word.ljust(5))
def vi_du5():
    word="VINH"
    print(word.center(10))
    print(word.center(10,"*"))
    print(word.center(21,"*"))
    print(word.center(2))
def vi_du6():
    s=" My school is CMC Uni "
    print(s)
    print(s.__len__())
    s=s.strip()
    print(s)
    print(s.__len__())
def vi_du7():
    s= "#hello Python*"
    print(s.startswith("#"))
    print(s.startswith("*"))
    print(s.endswith("*"))
    print(s.endswith("#"))
def vi_du8():
    s="hello hello hello"
    x1=s.find('o')
    print(x1)
    x2=s.rfind('o')
    print(x2)
    x3=s.find('x')
    print(x3)
    x4=s.rfind('h')
    print(x4)
def vi_du9():
    s = "Zelenskyy likes Putin, Putin likes Trump"
    c1 = s.count("Putin")
    print(c1)
    c2 = s.count("Trump")
    print(c2)
    c3=s.count("Kim Jong Un")
    print(c3)
def vi_du10():
    a=5
    b=9
    c=a/b
    s="{0}/{1}={2}".format(a,b,c)
    print(s)
def vi_du11():
    x = "Hello Word!"
    print(x[2:])
    print(x[:2])
    print(x[:-2])
    print(x[-2:])
    print(x[2:-2])
    print(x[6:11])
def vi_du12():
    s= "BIT250389 ;Le Quang Vinh ;28/01.2007"
    arr = s.split(";")
    for x in arr:
        print(x)
def vi_du13():
    s = "BIT250389 ;Le Quang Vinh ;28/01.2007"
    arr = s.split(";")
    for x in arr:
        print(x)
    s2 = ","
    s2 = s2.join(x)
    print(s2)
def vi_du14():
    lst = [5, -3, 12]
    print(lst[0])
    print(lst)
    print(len(lst))
def vi_du15():
    print("*"*35)
    lst =[5, 7,  2, 9, 6, 3, 10, 17, 16]
    for x in lst:
        print(x, end='\t')
    print()
    print("*"*35)
    for i in range(len(lst)):
        x = lst[i]
        print(x, end='\t')
    print()
    print("*"*35)
    for i in range(len(lst))-1, -1, -1:
        x = lst[i]
        print(x, end='\t')
def vi_du16():
    lst = [1, 2, 3,]
    print(lst)
    lst.insert(2, 9)
    print(lst)
    lst.insert(0,17)
    print(lst)
def vi_du17():
    lst = [1, 2, 3]
    lst.append(-113)
    print(lst)
def vi_du18():
    lst = [1, 0, 6, 3, 2, 3]
    del lst[2]
    print(lst)
def vi_du19():
    lst = [1, 0, 6, 3, 2, 3]
    lst.remove(3)
    print(lst)
def vi_du20():
    lst = [8, 1, 0, 2]
    print(lst)
    lst.sort()
    print(lst)
def vi_du21():
    lst = [8, 1, 0, 2]
    print(lst)
    lst=sorted(lst)
    print(lst)
def vi_du22():
    lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    print(lst) #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    print(lst[0:3]) # [10, 20, 30]
    print(lst[4:8]) # [50, 60, 70, 80]
    print(lst[2:5]) # [30, 40, 50]
    print(lst[-5:-3]) # [80, 90]
    print(lst[:3]) # [10, 20, 30]
    print(lst[:]) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    print(lst[-100:3]) # [10, 20, 30]
    print(lst[4:100]) # [50, 60, 70, 80, 90, 100, 110, 120]
    print(lst[2:-2:2]) # [10, 30, 50, 70, 90]
    print(lst[::2]) # [10, 30, 50, 70, 90, 110]
    print(lst[::-1]) # [120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
def vi_du23():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
def vi_du24():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in matrix: # duyệt từng dòng
        for elem in row: # Lấy từng phần tử trên mỗi dòng
            print('{:>4}'.format(elem), end=' ')
            print()


def vi_du25():
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            # Find the index of the minium element in the remaining unsorted array
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            # Swap the found minium element with the first unsorted element
            arr[i], arr[min_index] = arr[min_index], arr[i]
    # Examble
    arr1 = [1, 8, 3, 6, 4, 5, 7, 2, 9]
    selection_sort(arr1)
    print("Selection Sort:", arr1)
vi_du25()

