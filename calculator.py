class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        if b< 0:  return a+abs(b)
        else: return a-b


    def multiply(self, a, b):
        result = 0
        if a==0 or b==0:
            return 0
        if b < 0 or a < 0:
            a,b = -a,-b
        for i in range (abs(b)):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        subsign=1
        if b==0:
            return "Undefined"
        if a==0:
            return 0
        if b < 0 or a < 0:
            subsign=-1
            a,b=abs(a),abs(b)
        while a > 1:
            a = self.subtract(a, b)
            result += 1
        return result*subsign
    
    def modulo(self, a, b):
        if b==0:
            return "Undefined"
        if a==0:
            return 0
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(0, -3))
    print("Example: division: ", calc.divide(9, 10))
    print("Example: modulo: ", calc.modulo(10, 3))
   
    