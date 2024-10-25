print("Welcome to Mini Calculator")
print("Choose an option")
print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
option=input("Enter your option : ")
def add():
    print("You have chosen addition")
    num1=int(input("Enter your first number : "))
    num2=int(input("Enter your second number : "))
    print("The sum is :" , (num1+num2))
def sub():
    print("You have chosen subraction")
    num1=int(input("Enter your first number : "))
    num2=int(input("Enter your second number : "))
    print("The diffirence is : " , (num1-num2))
def multiplication():
    print("You have chosen multiplication")
    num1=int(input("Enter your first number :"))
    num2=int(input("Enter your second number :"))
    print("The product is : " , (num1*num2))

if (option=="1"):
    add()
elif (option=="2"):
    sub()
elif (option=="3"):
    multiplication()
else:
    print("You have chosen a none existing option")
