def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero"

if __name__ == "__main__":
    while True:
        print("\nOptions: + - * / or q to quit")
        op = input("Enter operation: ")
        if op == 'q':
            break
        if op in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if op == '+':
                    print("Result:", add(num1, num2))
                elif op == '-':
                    print("Result:", subtract(num1, num2))
                elif op == '*':
                    print("Result:", multiply(num1, num2))
                elif op == '/':
                    print("Result:", divide(num1, num2))
            except ValueError:
                print("Invalid input.")
        else:
            print("Invalid operation.")