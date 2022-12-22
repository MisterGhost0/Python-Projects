# Task 1 - Calorie Counting
# Solution by Batuhan Sazak
import os

print("Start!")

def findTheElfWithMostCalories():
    print("Hello from function!")
    with open("calorie_list.txt","r") as fileHandler:
        file_content = fileHandler.read()
        list_content = file_content.split("\n")
    fileHandler.close()

    #list_content.count('\n\n')
    #for counter in range(len(list_content)):
    #    counter += 1
    #    print (counter, "counted elements\n")
    #    if list_content[counter] == " ":
    #        #print(list_content[counter])
    #        break
    #    #print(len(list_content))

    i = 0
    while i < len(list_content):
        #if list_content[i].strip() == "":
        #    break

        print(i, " = ", list_content[i])
        i = i + 1

    
findTheElfWithMostCalories()