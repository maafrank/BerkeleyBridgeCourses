 
"""
Write a script to compute how many unique prime factors an integer has.  For example, 12 = 2 x 2 x 3, so has two unique prime factors, 2 and 3. Use your script to compute the number of unique prime factors of 1234567890. 
"""

import tqdm

def generate_prime_numbers(num: int) -> list:
    prime_numbers = []
    
    for n in tqdm.tqdm(range(2, num+1)):

        is_prime = True
        for i in range(2, (n//2) + 1):
            if (n % i) == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(n)
            
    return prime_numbers

def unique_prime_factors(num: int) -> None:
    prime_numbers = generate_prime_numbers(num)
    print(prime_numbers)

    count = 0
    for prime in prime_numbers:
        if (num % prime) == 0:
            count += 1
    return count


print(unique_prime_factors(12))
print(unique_prime_factors(1234567890))
