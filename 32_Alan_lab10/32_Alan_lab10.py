import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
ps1 = pd.Series([1,3,5,7,9])
ps2 = pd.Series([2,4,6,8,10])
print(ps1)
print(ps2)

#Qn4
ps = ps1 + ps2
ps = ps2 - ps1
ps = ps2 * ps1
ps = ps2 / ps1
print (ps)

#Qn5
print (ps2 == ps1)
print (ps2 > ps1)
print (ps2 < ps1)

#Qn6
dict = {'a': 10, 'b': 20, 'c':30, 'd':40, 'e':50}
psd = pd.Series(dict)
print (psd)

#Qn7
np_array = np.array([10,20,30,40,50])
ps_numArray = pd.Series(np_array)
print(ps_numArray)

#Qn8
s1 = pd.Series([10,'20','python','40','50'])
print(s1)
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)

#n9
s2 = s2.append(pd.Series([60,70]))
print(s2)

#Qn10
sorted_s2 = s2.sort_values()
print(sorted_s2)

#Qn11
sorted_s2.index =[1,2,3,4,5,6,7]
print(sorted_s2)

#Qn12
sorted_s2.mean()
roa = round(sorted_s2.mean())
print(roa)
sorted_s2.median()
roa2 = round(sorted_s2.median())
print(roa2)
sorted_s2.std()
roa3 = round(sorted_s2.std())
print(roa3)

#Qn13
var1 = s2.values.tolist()
print(var1)
type(var1)

#Qn14
npArray = np.array(var1)
print(npArray)
type(npArray)

#Qn15
import pandas as pd
colorList = pd.Series([
    ['Red','Blue','Yellow'],
    ['Red', 'White'],
    ['Black']])
print(colorList)
s = colorList.apply(pd.Series).stack().reset_index(drop=True)
print(s)

#Qn16
list = [1,2,3,4,5]
df = pd.DataFrame(list)
print(df)

import pandas as pd
listofList = [['Mike',5],['Peter',10],['Thomas',15]]
df = pd.DataFrame(listofList,columns=['Name','Age'])
print(df)

#Qn17
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"], "capital": ["Brasilia", "Moscow", "New Dehil", "Beijing", "Bloemfontein"], "area": [8.516, 17.10, 3.286, 9.597, 1.221], "population": [200.4, 143.5, 1252, 1357, 52.98]}
brics = pd.DataFrame(dict)
print(brics)

#Qn18
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

#Qn19
cars = pd.read_csv('mtcars.csv')
print(cars)

#Qn20
cars.head()
print(cars.head())
cars.tail()
print(cars.tail())

#Qn21
cars.columns
print(cars.columns)

#Qn22
cars.index
print(cars.index)

#Qn23
car = cars['model'].str.split(' ', n = 1, expand = True)
car.head()
print(car.head())

#Qn24
cars = cars.assign(car_brand=car[0])
cars = cars.assign(car_model=car[1])
print(cars[cars['car_brand'] == 'Mazda'])

#Qn25
cars.index = cars['model']
del cars['model']
print(cars.index)

#Qn26
print(cars.iloc[:,:6].describe())

#Qn27
print(cars.head(10))

#Qn28
print(cars.mean())

#Qn29
plt.scatter(cars['mpg'], cars['hp'])
plt.show();

#Qn30
ax = cars[['car_model','hp']].plot(kind='bar' , title ="Horse power comparison", figsize=(10,10), legend=True, fontsize=12)
plt.show();

#Qn31
ax = cars['hp'].plot(kind='hist', title="Range in HP" , figsize=(10,10), legend=True, fontsize=12)
plt.show();

#Qn32
my_fig = ax.get_figure()
my_fig.savefig("Car_Range_HP.png")

#Qn33
ps = cars['mpg'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Models', fontsize=5)
plt.ylabel('Miles per gallon', fontsize=10)
plt.xticks(index,ps.index, fontsize=10, rotation=90)
plt.title('Miles per gallon of Cars')
plt.bar(ps.index, ps.values)
plt.show();

#Qn38
plt.scatter(cars['mpg'], cars['hp'])
plt.savefig("scatterDiagram_mpg_hp.png")
ax = cars[['car_model', 'hp']].plot(kind='bar', title="Horse Power Comparsion", figsize=(15, 15), legend=True, fontsize=12)
my_fig = ax.get_figure()
my_fig.savefig("Horse_power_comparsion.png")

#Qn40
stats = linregress(cars['mpg'], cars['hp'])
m = stats.slope
b = stats.intercept
plt.figure(figsize=(5,5))
plt.scatter(cars['mpg'], cars['hp'])
plt.plot(cars['mpg'], m * cars['mpg'] + b, color="red", linewidth=3)
plt.savefig("PlotScatterDiagram.png")
plt.show();