"""
Design a program that determines the award a person competing in a triathlon will receive.
The program should read in the times for all three events (swimming, cycling, running) and calculate and display the total completion time.

"""



swimming_time = input("Time to complete swimming task: ")
cycling_time = input("Time to complete cycling task: ")
running_time = input("Time to complete running task: ")

total_time = (int(swimming_time) + int(cycling_time) + int(running_time))
print("Total time to complete the triathlon: " + str(total_time))


if total_time <= 100:
    print("Congratulations, you have received a Provincial Colours award!")

if total_time <= 105 and total_time >= 101:
    print("Congratulations, you have received the Provincial Half Colours award!")

if total_time <= 110 and total_time >= 106:
    print("Congratulations, you have received the Provincial Scroll award!")
   
if total_time >= 111:
    print("Well done for trying, but no award this time!")