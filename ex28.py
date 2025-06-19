def Div(num1, num2):
    result=0
    try:
        result = num1/num2
        print(f"The result is {result}")
    except:
        print("Divsion by zero!")


num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

Div(num1, num2)
