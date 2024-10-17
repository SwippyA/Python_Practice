def simple_interest(P, I, N):
    return P * I * N
def compound_interest(P, r, n, t):
    return P * ((1 + r / n) ** (n * t)) - P
# Taking inputs for simple interest
P = float(input("Enter the principal amount: "))
I = float(input("Enter the interest rate for the period: "))
N = float(input("Enter the tenure: "))

# Calculate and print simple interest
SI = simple_interest(P, I, N)
print(f"Simple Interest: {SI}")

# Taking inputs for compound interest
r = float(input("Enter the rate of interest: "))
n = int(input("Enter the number of compounding periods: "))
t = int(input("Enter the number of years: "))

# Calculate and print compound interest
CI = compound_interest(P, r, n, t)
print(f"Compound Interest: {CI}")
