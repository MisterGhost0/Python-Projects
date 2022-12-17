# Task 1 - Calorie Counting
# Solution by Batuhan Sazak

import os

print("Start!")

def findTheElfWithMostCalories():
    print("Hello from function!")
    with open("calorie_list.txt","r") as fileHandler:
        file_content = fileHandler.read()
        #print("File Content:\n", file_content)

        list_content = file_content.split("\n")
    
    fileHandler.close()

    print("List Content:\n", list_content)

    list_content.count('\n\n')
    

findTheElfWithMostCalories()