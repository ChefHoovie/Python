#Part 1
class SquareInfo:
    def calAvgArea(totalArea, totalCount):
         calAvgArea = totalArea / totalCount
         print("Square average Area is " + str(round(calAvgArea, 2)) + " square meter for " + str(totalCount) + " squares.")
totalArea = float(0)
totalCount = int(0)
names = []
areas = []
WaterBottle = float(0)
PlasticBottle = int(0)

file = open("listOfSquareArea.txt", "r")
for line in file:
      name, area = line.split()
      names.append(name)
      areas.append(float(area))
file.close()
print(names, areas)

file = open ("listOfSquareArea.txt", "r")
for area in areas:
    totalArea += area
    totalCount += 1

SquareInfo.calAvgArea(totalArea,totalCount)

#######################################################################################################################
#Part 2
Squarename = input("Enter new square name:")
names.append(Squarename)
print(names)

while True:
  try:
        Areaname = float(input("Please enter area in number: "))
        areas.append(Areaname)
        print(areas)
        break
  except ValueError:
         print("You have entered the wrong area, please re-enter the area in number.")
         continue

#######################################################################################################################
#Part 3
def calAvgArea(WaterBottle, PlasticBottle):
         calAvgArea = WaterBottle / PlasticBottle
         print("Square average Area is " + str(round(calAvgArea, 2)) + " square meter for " + str(PlasticBottle) + " squares.")

for area in areas:
    WaterBottle += area
    PlasticBottle += 1

SquareInfo.calAvgArea(WaterBottle,PlasticBottle)