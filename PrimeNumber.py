def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    div_limit = int(num ** 0.5) + 1 
    for i in range(2, div_limit):
        if num % i == 0:
            return False
    return True
number = int(input("Número: "))
if is_prime(number):
    print(number, "é primo")
else:
    print(number, "não é primo")
