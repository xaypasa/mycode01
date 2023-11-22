"""
ໄປເຮັດຄະແນນເກຼດ
91-100 = A
81-90 = B+
70-80 = B
65-69 = C+
60-64 = C
55-59 = D+
50-54 = D
0-49 = F
ຖ້າປ້ອນເປັນຕົວອັກສອນໃຫ້ມັນຂຶ້ນວ່າ Please input number only
ຖ້າປ້ອນຕົວເລກກາຍ 100 ຫຼື ປ້ອນຄ່າລົບເຂົ້າມາໃຫ້ມັນຂຶ້ນ Please input 0-100
"""
while True:
    try:
        A = int(input("Your score: "))
        break
    except:
        print("Please input number only ")

if (A)>100 or (A)<0:
    print("Please input 0-100")
elif (A) == str:
    print("Please input number only")
elif (A) >=90 and (A)<=100:
    print("Your grade is = A")
elif (A) >=81 and (A)<=90:
    print("Your grade is : B+")
elif(A)>=70 and (A)<=80:
    print("your grade is : B")
elif(A)>=65 and (A)<=69:
    print("your grade is : C+")
elif(A)>=60 and (A)<=64:
    print("your grade is : C")
elif(A)>=55 and (A)<=59:
    print("your grade is : D+")
elif(A)>=50 and (A)<=54:
    print("your grade is : D")
elif(A)>=0 and (A)<=49:
    print("your grade is : F")