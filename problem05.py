#PROBLEM STATEMENT 05
#Write a program that implements a user defined function that accept principal rate time number of times. 
# The interest is compounded to calculate in display compound interest (Hint: CI = P*(1+r/n)**nt)

def ci (p,r,t,n):
    r = r / 100
    amount = p * (1+r / n) ** (n*t)
    return amount

p = float(input("Enter Principal Amount:"))
r = int(input("Enter the Rate of Interest(%) per year:"))
t = int(input("Enter time in years:"))
n = int(input("Enter compounding per year:"))

amount = ci(p,r,t,n)
compound_interest = amount - p

print("Total Amount:", round(amount,2))
print("Compound Interest:", round(compound_interest, 2))