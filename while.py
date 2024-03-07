"""
Start
Ask user to input a number
As soon as -1 is entered the program should stop
Otherwise we calculate the average of the numbers entered, excluding -1
"""



number = 0
lst = []

def average():
    while True:
        number = int(input("Please enter a number :"))
        if number != -1:
            lst.append(number)
            continue

        avg = (sum(lst))/(len(lst))
        return (f"The average is {avg}")
    
print(average())