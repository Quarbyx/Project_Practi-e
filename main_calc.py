from calculator import Calculator
class Main:
    def main(self):
        calculator = Calculator()
        print("Сумма:", calculator.add(5, 3))
        print("Разность:", calculator.subtract(5, 3))
        print("Умножение:", calculator.multiply(5, 3))
        print("Деление:", calculator.divide(6, 3))
if __name__ == "__main__":
    main = Main()
    main.main()
