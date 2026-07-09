# Required arguments
def addition(a,b):
    print  (a + b)
addition(int(input("Enter the value of a : ")),int(input("Enter the value of b : ")))

def name(name,mob_no):
    print (f"The name of the person is {name} and mobile number of the number is {mob_no}")
name(mob_no = int(input("Enter your mobile number : ")),name = str(input("Enter your name : ")))

def name(name,mob_no):
    print (f"The name of the person is {name} and mobile number of the number is {mob_no}")
name(str(input("Enter your name : ")),int(input("Enter your mobile number : ")))

def subject(*sub):
    print(sub)
subject("Mathematics")

mylist = []
n = 4
for i in range(n):
    sub = input("Enter the subjects : ")
    mylist.append(sub)
    
subject(mylist)