def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

print(is_perfect(6)) 
print(is_perfect(28)) 
print(is_perfect(8128)) 
print(is_perfect(10)) 
