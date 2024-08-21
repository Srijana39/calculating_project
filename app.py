def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Simple Addition and Subtraction Program")

    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform addition
    sum_result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {sum_result}")

    # Perform subtraction
    subtract_result = subtract(num1, num2)
    print(f"The difference when {num2} is subtracted from {num1} is: {subtract_result}")

if __name__ == "__main__":
    main()
