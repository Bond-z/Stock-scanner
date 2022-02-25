import talib
import numpy as np
import yfinance as yf 



data = [23, 30, 44, 7, 48, 80, 6, 32, 96, 79, 67, 7, 17, 10, 66, 73, 21, 39, 36, 51, 98, 44, 16, 96, 100, 99, 72, 46, 41, 30,3] 


def mean():
    first = data[0]
    Sum = 0
    qty = len(data)
    for i in data:
            
        Sum += i

        print("{} + {} = {}  ".format(first,i,first+i))
    print('total of all number : ',Sum)
    mean = float("{:.2f}".format(Sum//qty))
    print(f"Mean = ", mean)
    # print(sum(data))
     


def tree():
    odd = 0

    for i in range(11,99,2):
        odd = odd + i
    print("Sum odd = ", odd) 


def multiply():
    i = 45
    sum = 0
    for i in range(45,116,2):
        print("{}*{}".format(i,i+1))

    print("Sum of 45-115 :", sum)

def combination():
    i = 0
    count = 0
    for i in data:
        for y in data:
            if i + y == 143 \
            and i != y: 
                print("{}+{} = {} ".format(i,y,i+y))
                count += 1

    print("how many number :",len(data))
    print("the result =", count//2)

# multiply()
# tree()
# combination()





#Question
# ratbit_jump = [0,3,6,9,12]     jump 1 ครั้ง ไป 3 ก้าว แต่เร่ิม jump ตั้งแต่ 0
# rat_jump = [4,6,8,10,12]       jump 1 ครั้ง ไป 2 ก้าว แต่เร่ิม jump ตั้งแต่ step ที่ 4
# rabbit and rat ต้อง jump กี่ครั้งถึงจะได้ระยะที่เท่ากัน

rabbit_start_at = 0
rat_start_at = 4

def rabbit_jump():
    i = 2
    y = 4
    count_rabbit = 0
    count_rat = 0
    while i <= 50:
        i = i + 3
        count_rabbit += 1

        y = y + 2
        count_rat += 1

        if count_rabbit == count_rat \
        and i == y:
            # print("rabbit jump : {} step = {}".format(count,i))
            print("Rabbit jump : {} times and got step = {}".format(count_rabbit,i))
            print("Rat jump : {} times and got step = {}".format(count_rat,y))
            print("Rabbit and Rat needs to jump {} times".format(count_rabbit))
            break
        else:
            print("Never meet each other")
       
rabbit_jump()




            



