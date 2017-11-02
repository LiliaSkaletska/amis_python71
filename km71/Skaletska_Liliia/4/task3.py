number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number"))
number3 = int(input("Enter the third number"))
if (number1 < number2) and (number2 < number3):
    print(number1)
elif (number1 < number3) and (number3 < number2):
    print(number1)
elif (number2 < number1) and (number1 < number3):
    print(number2)
elif (number2 < number3) and (number3 < number1):
    print(number2)
elif (number3 < number1) and (number1 < number2):
    print(number3)
elif (number3 < number2) and (number2 < number1):
    print(number3)
elif (number1 == number2) and (number1 < number3):
    print(number1)
elif (number1 == number3) and (number1 < number2):
    print(number1)
elif (number3 == number2) and (number3 < number1):
    print(number2)
else:
    print(number1)

