class Calculator:
    def add(self, a, b):
        return a + b   #Операция сложения
    def subtract(self, a, b):
        return a - b    #Операция разности
    def multiply(self, a, b):
        return a * b    #Операция умножения
    def divide(self, a, b):
        if b == 0:
            raise ValueError("IllegalArgumentException")    #Возврат ошибки при попытке деления на 0
        return a / b        #Операция деления
