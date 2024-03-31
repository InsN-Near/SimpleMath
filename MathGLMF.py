def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
def modular_exponentiation(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
while True:
    print("\nMathematical Functions Menu:")
    print("1. Greatest Common Divisor (GCD)")
    print("2. Least Common Multiple (LCM)")
    print("3. Modular Exponentiation")
    print("4. Factorial")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("GCD:", gcd(num1, num2))
    elif choice == '2':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("LCM:", lcm(num1, num2))
    elif choice == '3':
        base = int(input("Enter the base: "))
        exponent = int(input("Enter the exponent: "))
        modulus = int(input("Enter the modulus: "))
        print("Result:", modular_exponentiation(base, exponent, modulus))
    elif choice == '4':
        num = int(input("Enter a number: "))
        print("Iterative Factorial:", factorial_iterative(num))
        print("Recursive Factorial:", factorial_recursive(num))
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
