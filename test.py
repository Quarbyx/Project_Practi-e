import unittest
from calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add_positive_numbers(self):
        self.assertEqual(self.calculator.add(2, 3), 5) #Проверка сложения положительных чисел
    def test_add_negative_numbers(self):
        self.assertEqual(self.calculator.add(-2, -3), -5) #Проверка сложения отрицательных чисел
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calculator.subtract(5, 2), 3) #Проверка разности положительных чисел
    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calculator.subtract(-2, -3), 1) #Проверка разности отрицательных чисел
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6) #Проверка умножения положительных чисел
    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calculator.multiply(-2, -3), 6) #Проверка умножения отрицательных чисел
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calculator.divide(6, 3), 2) #Проверка деления положительных чисел
    def test_divide_negative_numbers(self):
        self.assertEqual(self.calculator.divide(-6, -3), 2) #Проверка разности отрицательных чисел
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(6, 0) #Проверка ошибки при делении на 0
if __name__ == '__main__':
    unittest.main()
