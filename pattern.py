"""
The aim of the code is to draw a pattern using a single for loop
"""

for i in range(1, 10): # Difine the range to use for the if - else statement
    if i < 6: 
        print("* " * i) # if i is less than 6, we pring i * "*"
    else:                # otherwise we use the below statement
        print("* "* ((i * -1) + 10))