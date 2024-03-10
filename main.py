import math
import sys
sys.set_int_max_str_digits(32768)
number = int(input("Введите число: "))
result = math.factorial(number)
print(f"Факториал числа {number} равен {result}")
