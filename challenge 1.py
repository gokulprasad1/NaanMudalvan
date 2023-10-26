def fac_rec(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac_rec(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {fac_rec(n)}")