"""

Write a program that reads in a string and makes each alternate character into an upper case character and each other alternate character 
other character into a lower case character .e.g. The string “Hello World” would become “HeLlO WoRlD”

Once that is done, using the same string but this time making each alternative word lower and uppercase.
e.g. The string: "I am learning to code" would become "i AM learning TO code".

Tips: Using the split() and join() functions will help you here.

"""
# *********    Part 1    ********

# #define original quote as string, and print it for user to see:

string = "My favourite quote from Yoda - Star Wars is: \n ""Fear is the path to the dark side. \n Fear leads to anger. \n Anger leads to hate. \n Hate leads to suffering"
print(string)
upper = True
new_string = []  #creating a list of the original string
for i in string:  #using a for loop to iterate over the charachters
    if upper:
        new_string.append(i.lower())
        upper = False
    else:
        new_string.append(i.upper())
        upper = True
new_string = "".join(new_string) 

print(new_string)  #print the new string that prints out the original statement using alternating upper and lower case characters


# ****** Part 2 *******

# the aim is to alternate each word in upper and lower case letters


string = "My favourite quote from Yoda - Star Wars is: \n ""Fear is the path to the dark side. \n Fear leads to anger. \n Anger leads to hate. \n Hate leads to suffering"
split_string = string.split()                         #to create a list
final_string = ""                                     
for i in range(len(split_string)):                      #for loop to iterate over the words
     if i % 2 == 0:
        final_string += split_string[i].upper() + " "   #if item index divides by 2 then convert to uppercase
    else:
        final_string += split_string[i].lower() + " "   #otherwise convert to lowercase

print(final_string) # print out each word in the chosen quote in alternating cases