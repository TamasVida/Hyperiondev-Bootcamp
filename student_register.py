"""
Practical Task - Register students for an exam venue
1. Ask how many students are attending
2. Create a for loop, that runs for the number of students, and each time the loop runs: ask "Please enter next studend ID
3. Write each of the ID number to reg_form.txt 
4. Inclued a dotted line after each ID, for students to sing
"""

students = int(input("Please enter how many students are attending the exam: "))
student_id = ""

for a in range (0, students):
    student_id = (int(input("Enter Student ID number:")))
    student_id = student_id
    with open('reg_form.txt', 'a') as file:
        file.write("Student ID number: " + str(student_id) + "  " + "............................, \n")

