# int data type
a = (8+2)
print(a)
print(type(a))
# float data type
b = (6-4)
print(type(b))
# boolean data type
a = True
b = False
print(a and b)
print(a or b)
print(not b)
# remove
list = [1,2,3,4,5,6]
print(list.pop(4))
print(list)
print(list.remove(4))
print(list)
a = int(input("enter a number 1: "))
b = int(input("enter a number 2: "))
print(a+b)
print(a-b)
print(a*b)
# if and else condition
number = int(input("enter the number"))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")

print("even") if number % 2 == 0 else print("odd")
# (or)
a = int(input())
if  a%2 == 0:
    print("even")
else:
    print("odd")
# if elif else while
while True:
    a = int(input())
    if a == 1:
        print("Monday")
    elif a == 2:
        print("Tuesday")
    elif a == 3:
        print("Wednesday")
    elif a == 4:
        print("Thursday")
    elif a == 5:
        print("Friday")
    elif a == 6:
        print("Saturday")
    elif a == 7:
        print("Sunday")
    else:
        print("Enter correct value")
#
while True:
    n = int(input())
    if 20 > n > 0 == n % 2:
        print("Wierd number")
    elif 20 > n > 0 != n % 2:
        print("Normal number")
    elif 30 > n >= 20:
        print("Normal Number")
    elif 30 <= n and n % 2 != 0:
        print("normal number")
    else:
        print("Wierd Number")
# exit method
while True:
    n = int(input())
    if 20 > n > 0 == n % 2:
        print("Wierd number")
    elif 20 > n > 0 != n % 2:
        print("Normal number")
    elif 30 > n >= 20:
        print("Normal Number")
    elif 30 <= n and n % 2 != 0:
        print("normal number")
    elif n == 0:
        exit()
    else:
        print("Wierd Number")
#
list = [1,2,3,4]
for i in list :
    print(i+i)
#
list = [X for X in range(0,10)]
print(list)
list = [num for num in range(0,51) if num%2 == 0]
print(list)
list = [num for num in range(0,51) if num%2 != 0]
print(list)
list = [num for num in range(1,101) if num%7 == 0 and num%11 == 0]
print(list)
#
list = [1,-29,3,-47,-52,-63]
sumOfPositives = 0
sumOfNegatives = 0
for i in range (len(list)):
    if list[i] >0:
        sumOfPositives = sumOfPositives+list[i]
    else:
        sumOfNegatives = sumOfNegatives+list[i]
print(sumOfPositives)
print(sumOfNegatives)
#
s1 = {
      'key 1': 'name',
      'key 2': 'sai'
}
print(s1['key 1'])
print(s1['key 2'])
print(s1)
# dictionary
l = []
d = {}
for i in range(2):
    d.update({
        'key1': input('enter key 1:'),
        'key2': input('enter key 2:')
    })
    l.append(d)

print(l)
#
db = [
        {'pragati@gmail.com': '123'} ,
        {'pragati1@gmail.com': '1212'} ,
        {'pragati2@gmail.com': '2023'}

     ]
print(db)
username = input("Enter username: ")
password = input("Enter password: ")
for i in (db):
    print(i)
#
db = [
        {'pragati@gmail.com': '123'} ,
        {'pragati1@gmail.com': '1212'} ,
        {'pragati2@gmail.com': '2023'}

     ]
print(db)
username = input("Enter username: ")
password = input("Enter password: ")
for i in (db):
    print(i.keys())
    print(i.values())
    print(i.items())
#
db = [
        {'pragati@gmail.com': '123'} ,
        {'pragati1@gmail.com': '1212'} ,
        {'pragati2@gmail.com': '2023'}

     ]
print(db)
username = input("Enter username: ")
password = input("Enter password: ")
temp = {
    username: password
}
if temp in db:
    print("found")
else:
    print("not found")
#
row = 3
col = 2
array1 = []
for i in range(row):
    temp = input("enter element in row: ").split(' ')
    ele = list(map(int, temp))
    array1.append(ele)
print(array1)
array2 = []
for i in range(row):
    temp = input("enter element in row: ").split(' ')
    ele = list(map(int, temp))
    array2.append(ele)
print(array2)

res = [[0 for j in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        res [i][j] = array1[i][j] + array2[i][j]
print(res)
#
row = 3
col = 4
array = [
            [1,2,3,10],
            [4,5,6,20],
            [7,8,9,30]
]
new_array=[]
for i in range(row):
    b = list(map(int, input('enter elements: ').split(' ')))
    new_array.append((b))
print(new_array)
#
col = 4
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l)
print(l[::-1])
#
s = "hello@world"
print(s)
res = s.split('@')
print(res)
#
s = "hello@world"
print(s)
res = s.split(' ')
print(res)
#
s = "hello@world"
print(s)
res = s.split()
print(res)
#
s = "hello world"
print(s)
res = s.split(' ')
print(res)
print('-'.join(res))
#
s = "hello world"
print(s.title())
#
s1 = "hello world"
s2 = "HI THERE"
print(s1.upper())
print(s2.lower())
#
s1 = "HEllo worLD"
s2 = "HI THERE"
res = s1.swapcase()
print(s1)
print(res)
#
first = "Mr mani is"
age = 20
last = "years old"

print("Mr mani is {} years old".format(age))

op = "Mr mani is 20 years old"
#
num = 3.14
print("the square of {} is {}".format(num, num*num))

op = "Mr mani is 20 years old"
#
num = 10
print("the square of {:.5f} is {:.6f}".format(num, num*num))

op = "Mr mani is 20 years old"
#
num = 10
print("the square of {:10} is {:.6f}".format(num, num*num))
#
num = 10
print(f"the square of {num} is {num*num:.5f}")
#
a = int(input('enter a: '))
b = int(input('enter b: '))
print(a/b)
# try and except
a = int(input('enter a: '))
b = int(input('enter b: '))
try:
    print(a/b)
except:
    print("b cannot be 0")
print("after the error")
# function
def addition(number1, number2):
    result = number1+number2
    return result

print(addition(10,20))

def multi(number1, number2):
    result = number1*number2
    return result

print(multi(10,2))
#
def prime(num):
    count = 0
    for i in range(1, num+1):
        if num%i == 0:
            count += 1
    if count == 2:
        print("prime")
    else:
        print("not prime")
print(23,24)
# line variables
def add(*abc):
    res1=1
    for i in abc:
        res1 *= i
    return res1

print(add(10,20,30,40,50))
#
def add(a,b, *abc):
    print(a)
    print(b)
    print(abc)

print(add(10,20,30,40,50))
# check function
def check(n):
    print(n)
    if n > 0:
        check(n-1)

check(5)
#
def f(a,b,c):
    print(a,b,c)
f(c=12,b=111,a=134)
#
def add_two_numbers(a,b):
    return a+b

def add_n_numbers(*arr):
    return sum(arr)
# import function
from ifelif import add_two_numbers
a= 113
b= 123
print(add_two_numbers(a, b))
#
class student:
    name = ""
    roll_number = ""
    branch = ""
    marks = 0
    attendence = 0.0
    is_using_transport = False
    def view_attendence(self):
        pass
    def view_marks(self):
        pass
    def view_name(self):
        pass
    def update_name(self, new_name):
        pass
#
class student:
    student_name="no name"
    def __init__(self, name):
        self.student_name = name

s1 = student("mukesh")
s2 = student("sai")
s3 = student("mowa")
print(s3.student_name)
# username
username = input()
password = input()
print("Hello, {0}! your password is {1}".format(username,password))
#
class Bank:
    Account_Number=""
    Name=""
    Bank_Branch=""
    def __init__(self,Account_Number,Name,Bank_Branch):
        self.Account_Number=Account_Number
        self.Name=Name
        self.Bank_Branch=Bank_Branch
    def __str__(self):
        return f"{self.Account_Number},{self.Name},{self.Bank_Branch}"
p1=Bank("1234","naveen","sbi")
p2=Bank("143","subhu","icici")
p3=Bank("768","Ali","pichi")
print()
#
class user:
    full_name = ""
    email = ""
    __password = ""
    moblie_number = ""
    def update_name(self, new_name):
        self.full_name = new_name
    def get_name(self):
        return self.full_name
    def update_password(self, new_password):
        self.__password = new_password
    def update_mobile_number(self, new_number):
        self.moblie_number = new_number
    def get_user_password(self):
        return self.__password
# multilevel inheritance
class veerraju:
    property1="village land"
    property2="house"
    property3="Dry_fish"
class jrveerraju(veerraju):
    property4="house"
    property5="land"
    property6="fishing boat"
class samith(jrveerraju):
    pass
obj=samith()
print(obj.property5)
# hierarical
class veerraju:
    property1="village land"
    property2="house"
    property3="Dry_fish"
class jrveerraju(veerraju):
    property4="house"
    property5="land"
    property6="fishing boat"
class samith(jrveerraju):
    pass

class aishwarya(jrveerraju):
    pass
obj = samith()
obj1=aishwarya()
print(obj.property5)
print(obj1.property2)
#
# add
# remove
# insert
# pop
# print
n=int(input())
l=[]
for i in range(n):
    read=input()
    k=read.split(" ")
    if k[0]=="add":
        A=int(k[1])
        l.append(A)
    elif k[0]=="insert":
        I=int(k[1])
        N=int(k[2])
        l.insert(N,I)
    elif k[0]=="remove":
        if len(l)>0:
            R=int(k[1])
            l.remove()
    elif k[0]=="pop":
        if len(l)>0:
            l.pop()
    elif k[0]=="print":
        print(*l,sep=' ')
# 4
# add 4
# add 6
# add 3
# print
# random
from random import random, randint

a = randint(1,10)
id = random()*1000
print(id)
# game
from random import choice
luck=input("enter your choice (rock,paper,scissors)\n")
l=["rock", "paper", "scissors"]
k=choice(l)
print(k)
if luck==k:
    print("both are same")
elif (luck=="paper" and k=="rock") or (luck=="scissors" and k=="paper") or (luck=="rock" and k=="scissors"):
    print("You won the game")

elif (k=="paper" and luck=="rock") or (k=="scissors" and luck=="paper") or (k=="rock" and luck=="scissors"):
    print("you loose the game")
#
from random import choice
while True:
    luck=input("enter your choice (rock,paper,scissors)\n")
    l=["rock", "paper", "scissors"]
    k=choice(l)
    print(k)
    if luck==k:
        print("both are same")
    elif (luck=="paper" and k=="rock") or (luck=="scissors" and k=="paper") or (luck=="rock" and k=="scissors"):
        print("You won the game")

    elif (k=="paper" and luck=="rock") or (k=="scissors" and luck=="paper") or (k=="rock" and luck=="scissors"):
        print("you loose the game")
# game with score
from random import choice
luck_score=0
kick_score=0
num=int(input("number of times you want to play\n"))
for i in range(num):
    luck=input("enter your choice (rock,paper,scissors)\n")
    l=["rock", "paper", "scissors"]
    k=choice(l)
    print(k)
    if luck==k:
        print("both are same")
    elif (luck=="paper" and k=="rock") or (luck=="scissors" and k=="paper") or (luck=="rock" and k=="scissors"):
        luck_score +=1

    elif (k=="paper" and luck=="rock") or (k=="scissors" and luck=="paper") or (k=="rock" and luck=="scissors"):
        kick_score +=1
print("your score is ",luck_score)
print("computer score is ",kick_score)
if luck_score > kick_score:
    print("You won the game")
elif luck_score < kick_score:
    print("You loose the game")
elif luck_score == kick_score:
    print("You got draw")
#
