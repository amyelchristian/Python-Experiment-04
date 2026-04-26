#PROBLEM STATEMENT 01
#Write a program to check the divisibility of a number by 7 is passed as a parameter to the user defined function.
def check_divisibility(number):
    if number % 7 == 0:
        return True
    else:
        return False
    
num = int(input("Enter a number to check:"))
if check_divisibility(num):
    print("Yes, is divisible by 7")
else:
    print("No, it is not divisible by 7")