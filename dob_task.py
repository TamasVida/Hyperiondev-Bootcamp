"""
IO Operations - Input Task!

Create a dob_task.py
Read lines of the provided DOB.txt file
Print out the names only from each lines
Print out the birthdates from each lines

"""

f = open('DOB.txt', 'r+')
print("Name:" + "\n")
for name in f:
    print(" ".join(name.split()[:2]))
f.close()
print()  # added an empty line for nicer output
print("Date of Birth:" + "\n")
f = open('DOB.txt', 'r+')
for dob in f:
    print(" ".join(dob.split()[-3:]))
f.close()




