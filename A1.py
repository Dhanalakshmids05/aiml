num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")
print()


def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

greatest = find_greatest(num1, num2, num3)
print(f"The greatest number is: {greatest}")
print()



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator! Please use +, -, *, or /.")
print(f"Result:{result}")