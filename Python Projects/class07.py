# calculator

print("mini calculator")
num1=float(input("Enter a first number here:"))
num2=float(input("Enter a second number here:"))

choice=int(input("Enter nnumber between 1-4"))

print("""
    press 1 for addition
    press 2 for subtraction
    press 3 for multiplicatuion
    press 4 for division
""")

if choice==1:
sum=num1+num2
print("the addition of two given number is",sum)
elif choice==2:
print("the subtraction of two given number is",num1-num2)
elif choice==3:
print("the multiplication of two given number is",num1*num2)
elif choice==4:
print("the division of two given number is",num1/num2)
else("invalid input bhai sahi number select ker")
else:
    