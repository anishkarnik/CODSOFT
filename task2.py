#operation functions

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

#The Menue
print("Choose Operation:")
print("(1) Add")
print("(2) Subtract")
print("(3) Multiply")
print("(4) Divide")

x=input("Enter your choice:")

if x in ['1','2','3','4']:
    num1= float(input("Enter 1st number:"))
    num2= float(input("Enter 2nd number:")) 
    #converting to float to be able to operate on decimal values as well
else :
    print("Invalid Input")

if x == '1':
    print(num1,"+",num2,"=",add(num1,num2))

if x == '2':
    print(num1,"-",num2,"=",sub(num1,num2))

if x == '3':
    print(num1,"x",num2,"=",mul(num1,num2))

if x == '4':
    print(num1,"/",num2,"=",div(num1,num2))

