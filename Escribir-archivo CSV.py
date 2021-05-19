import csv

myData=[["first name", "second name", "Grade"],
         ['Alex', 'Brian', 'A'],
         ['Tom', 'Smith', 'B']]
 
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")
