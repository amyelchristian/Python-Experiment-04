#PROBLEM STATEMENT 04
#ABC School has allotted unique token list from (1 to 600) open to all the parents 
#for facilitating a lucky draw on the day of the annual Day function. 
# The winner would receive a special prize. 
# Write a program using python that helps to automate task. (Hint: Use Random module)

import random
import time
def winner (start, end):
    return random.randint(start, end)

print("--- ABC SCHOOL ANNUAL DAY LUCKY DRAW ---")
print("\n THE TOKENS ARE FROM 1 TO 600")
print (input(("PRESS ENTER TO START THE DRAW")))

print("\n SHUFFLING TOKENS...")
time.sleep(1)

print("SELECTING THE WINNER...")
time.sleep(1)
token = winner(1,600)
print("--------------------------------------------")
print(f"🎉 CONGRATULATIONS 🎉")
print("--------------------------------------------")
print(f"THE WINNING TOKEN NUMBER IS: {token}")