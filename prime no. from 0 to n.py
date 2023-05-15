def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_prime_numbers(n):
    print("prime numbers from 0 to", n, ":")
    for number in range(n + 1):
        if is_prime(number):
            print(number)
# Example usage
n = 3000
print_prime_numbers(n)


