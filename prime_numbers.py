def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
limit = int(input("Enter the limit up to which you want to print prime numbers: "))
print(f"Prime numbers up to {limit} are:")
for number in range(2, limit + 1):
    if is_prime(number):
        print(number, end=' ')
print()