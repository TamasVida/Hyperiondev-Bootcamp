age = int(input("Please enter your age: "))

if age >= 100:
    print("Sorry, you are dead!")
elif age>= 65:
    print("Enjoy your retirenment!")
elif age >= 40:
    print("You are over the hill.")
elif age == 21: 
    print("Congrat's on your 21st.")
elif age < 13:
    print("You qulify for the kiddie discount.")

else:
    print("Age is but a number!")
