#PROBLEM STATEMENT 03
#Write a program that has a user defined function to accept the coefficients of a quadratic equation in variables 
# and calculates its determinant. 
# For example: if the coefficients are stored in the variables a,b,c then calculate determinant as b2 – 4ac. 
# Write the appropriate condition to check determinants on positive, zero and negative and output appropriate result.

def discriminants (a,b,c):
    determinant = (b ** 2) - (4 * a * c)
    
    print(f"\n The Determinant of [D] is: {determinant}")
    if determinant > 0:
        print("Result: The equation has 2 real distinct roots")
    elif determinant == 0:
        print("Result: The equation has only 1 real root")
    else:
        print("Result: The equation has no real roots")
        
print("EQUATION FOR: ax^2 + bx + c = 0")
coeff_a = float(input("Enter co-efficient a:"))
coeff_b = float(input("Enter co-efficient b:"))
coeff_c = float(input("Enter co-efficient c:"))

if coeff_a == 0:
    print("Co-efficient a cannot be 0 in a quadratic equation form")
else:
    discriminants (coeff_a, coeff_b, coeff_c)