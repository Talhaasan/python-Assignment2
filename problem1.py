import os
from glob import glob

givenString = input("Enter string: ") #input string
PATH = "C:\src\python_projects" #define path.
files = [b for a in os.walk(PATH) for b in glob(os.path.join(a[0], '*'))] #give all file

takenString = givenString
givenString = givenString.lower()#for discriminating uppercase and lowercase
count = 0

for i in files:
   if i.lower().find(givenString) != -1: #finding file with the same name as input
       count = count+1

print("{} occurences for string {} ".format(count,takenString))#printing the number of files with the same name as input.




