def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  
    primes[0] = primes[1] = False   
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for multiple in range(p * p, n + 1, p):
                primes[multiple] = False
    return [p for p in range(n + 1) if primes[p]]
limit = 100
prime_numbers = sieve_of_eratosthenes(limit)
print(f"Prime numbers up to {limit}:")
print(prime_numbers) 
