class Calculator:
    def add(self, a, b):
        return a + b
    def ngurangin(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
    def modulo(self, a, b):
        return a % b
    def power(self, a, b):
        return a ** b
    

if name == "main":
    calc = Calculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.ngurangin(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))
    print("Modulo: ", calc.modulo(10, 5))
    print("Power: ", calc.power(10, 5))