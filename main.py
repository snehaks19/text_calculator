
print("1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION\n")

print("Enter the operation you want to perfom : ")
operation=input()
if operation=="1":
    num1=input("Enter the first number :")
    num2=input("Enter the second number :")
    sum=str(int(num1)+int(num2))
    print("Answer is",sum)

elif operation=="2":
    num1=input("Enter the first number :")
    num2=input("Enter the second number :")
    difference=str(int(num1)-int(num2))
    print("Answer is",difference)

elif operation=="3":
    num1=input("Enter the first number :")
    num2=input("Enter the second number :")
    product=str(int(num1)*int(num2))
    print("Answer is",product)

elif operation=="4":
    num1=input("Enter the first number :")
    num2=input("Enter the second number :")
    quotient=str(int(num1)/int(num2))
    print("Answer is", quotient)
else:
    print("Enter valid number")





