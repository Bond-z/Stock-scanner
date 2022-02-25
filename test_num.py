import talib
import numpy as np
import yfinance as yf 



data = [1,3,5,7,9,11,13,15,17,19,20]    

# data = [1,3]


sumary = []
a = 0
b = 0
count = 0
# def calculate(from_n, to_n):
        
#     for i in range(from_n, to_n + 1):
#         for j in range(1, 11):
#             print("{} + {} = {}".format(i,j, i+j))


# calculate(1,5)
def find_sum(i,b):

    return (i+b)

def total(data):
    r = len(data)
    print("total number : ",r)
    for i in data:
        for b in data:
          
            print("{}+{}={}".format(i,b,i+b))
            if i + b == 20 \
                and i != b:
                sumary.append("{}+{}".format(i,b))
            

def twenty(sumary):
    l = len(sumary)
   
    return l/2    


total(data)
print(sumary)
print("The total of sum equal to 20 is : ", twenty(sumary))
