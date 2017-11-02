"""

Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і
наступне значення за форматом:

The next number for the number 179 is 180.
The previous number for the number 179 is 178.

Вхідні дані: ціле число

Вихідні дані: два рядки за наведеним у завдання форматом.
"""
number1 = int(input("Enter a number:"))
number2 = number1 + 1
number3 = number1 -1
print(" The next number for the number", number1, "is",number2,"\n","The previous number for the number", number1,"is",number3)
