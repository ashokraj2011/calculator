def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    print("Simple Calculator")
    print("-----------------")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition:       {a} + {b} = {add(a, b)}")
    print(f"Subtraction:    {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication: {a} x {b} = {multiply(a, b)}")

if __name__ == "__main__":
    main()
