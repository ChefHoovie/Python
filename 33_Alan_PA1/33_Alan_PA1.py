#Part 1

class CalUtils: #To create an object
    def calAveHeight(totalStudentHeight, totalStudentCount): #Function
        calAveHeight = totalStudentHeight/totalStudentCount #Formula of area
        print("Student average height is " + str(round(calAveHeight, 2)) + " m for " + str(totalStudentCount) + " students.") #Result
        #Student average height is 1.72 m for 7 students.
#Variables
totalStudentHeight = float(0)
totalStudentCount = int(0)
names = []
heights = []
newTotalStudentHeight = float(0)
newTotalStudentCount = int(0)

file = open("listOfStudentHeight.txt", "r")
for line in file: #To seperate the areas and names
      name, height = line.split()
      names.append(name)
      heights.append(float(height))
file.close()
print(names, heights)
#['Thomas', 'Peter', 'William', 'Patrick', 'May', 'June', 'Linda']

file = open ("listOfStudentHeight.txt", "r")
for height in heights:
    totalStudentHeight += height
    totalStudentCount += 1

CalUtils.calAveHeight(newTotalStudentCount,totalStudentCount)

#Part 2

Squarename = input("Enter new student name: ")
names.append(Squarename)
print(names)

while True: #while loop for inputing the new height, if the height input contains anything but string then it will have error
  try:
        Heightened = float(input("Enter student height (in meters): ")) #Enter student height (in meters): 1.9
        heights.append(Heightened)
        print(heights)
        break
  except ValueError: #Enter student height (in meters): alan
         print("You have not correctly entered the height, please re-enter in number only.") #You have not correctly entered the height, please re-enter in number only.
         continue

#Part 3

def calAvgHeight(newTotalStudentHeight, newTotalStudentCount): #For new inputs
         calAvgHeight = newTotalStudentHeight / newTotalStudentCount
         print("Student average height is " + str(round(calAvgHeight, 2)) + "for" + str(newTotalStudentCount) + " students.")
         #Student average height is 1.74 m for 8 students.

for height in heights:
    newTotalStudentHeight += height
    newTotalStudentCount += 1

CalUtils.calAveHeight(newTotalStudentHeight, newTotalStudentCount)

