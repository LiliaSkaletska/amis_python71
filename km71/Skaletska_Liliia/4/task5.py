number1 = int(input("enter number 1"))
number2 = int(input("enter number 2"))
number3 = int(input("enter numer3"))
if number1==number2==number3:
    result=3
elif number1==number2 or number2==number3 or number1==number3:
    result=2
else:
    result=1
print(result)