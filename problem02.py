#PROBLEM STATEMENT 02
# Write a program that uses a user defined function that accepts name and gender (as M for Male, F for Female) and prefixes Mr/Ms on the basis of the gender
def fun (name, gender):
    gender = gender.upper()
    if gender == "M":
        return f"Mr. {name}"
    elif gender == "F":
        return f"Ms. {name}"
    else:
        return f"Hello, {name}, (Gender identifier not recognized)"
    
name = input("Enter your name:")
gender = input("Select your gender (M/F):")
prefix = fun(name, gender)
print(prefix)