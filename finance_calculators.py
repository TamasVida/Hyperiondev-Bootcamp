"""
start
define investment and bond and ask user to choose what would they like to calculate
when user decide what they would like to do, ask them to input 
amount of money
interest rate
number of years
chose between simple or compound interest 
Define the formula to calculate simple interest
Define the formula to calculate compound interest
print out the answer
if user chooses bond ask them to input
present value
interest rate
number of months to repay
Define the formula to calculate bond repayment
print out the answer
"""
import math

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

full_name = (f"{first_name} {last_name}")
print("Welcome" , full_name + "!")

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

calculation = input(str("Please enter What would you like to calculate investment or bond? "))

      
inv = "investment"
bond = "bond"
if calculation.lower () == inv:
    print ("Let's calculate your investment!")
    operation = str(input("Please enter 'simple' to calculate simple interest or 'compound' to calculate compound interest: ,or 'bond' to calculate the repayment: "))

    if "simple" in operation:

        # To calculate simple interest
        deposit = float(input("Please enter the amount of money you wish to deposit: "))
        time = float(input("Please enter the number of years you wish to invest for: "))
        int_rate = float(input("Please enter the interest rate: "))
        

        simple_interest = deposit * (1+(int_rate/100) * time)
        simple_interest = round (simple_interest, 2)
        print("The return of your simple interest is: " , simple_interest)

    elif "compound" in operation:
        # To calculate compound interest

        deposit = float(input("Please enter the amount of money you wish to deposit: "))
        time = float(input("Please enter the number of years you wish to invest for: "))
        int_rate = float(input("Please enter the interest rate: "))
        compound_interest = deposit * math.pow(1 + (int_rate/100), time)
        compound_interest = round (compound_interest, 2)
        print("The return of your compound interest: ", compound_interest)

if calculation.lower() ==  bond:
    print("Let's calculate your repayment: ")
# To calculate bond repayment 
    current_value = float(input("Please enter the current value of your propety: "))
    time_period = float(input("Please enter the number of months you plan to repay the bond: "))
    interest_rate = float(input("Please enter the interest rate: "))
   # monthly_int_rate = (interest_rate/100)/12
   # bond_repayment = ((monthly_int_rate * current_value)/(1 + monthly_int_rate)**(-time_period))
    bond_repayment = (((interest_rate/100)/100) * current_value)/((1 + interest_rate/100)**(-time_period))
    bond_repayment = round (bond_repayment, 2)
    print("The total amount you will have to pay back is: " , bond_repayment)
