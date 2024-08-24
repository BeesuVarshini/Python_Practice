ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
print(ages)
min = min(ages)
max = max(ages)
print("min age is ",min)
print("max age is ",max)

#Add the min age and the max age again to the list
ages.append(min)
ages.append(max)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(ages)
last_index = len(ages)-1
middle_index = int(last_index/2)
if last_index%2 !=0:
    median = ages[middle_index]
    print("median age is ",median)
else:
    median = int((ages[middle_index] + ages[(middle_index+1)])/2)
    print("median is ",median)

#Find the average age (sum of all items divided by their number )
i =0
sum =0
for i in range(0,len(ages)):
    sum = sum+ages[i]
    i = i+1
print(sum)
avg_age = sum/len(ages)
print("avg age is ",avg_age)
    #(or)

#avg_age = sum(ages)/len(ages)
#print("avg age is ",avg_age)

#Find the range of the ages (max minus min)
range = max - min
print(range)

#Compare the value of (min - average) and (max - average), use abs() method
abs_min = abs(min - avg_age)
abs_max = abs(max - avg_age)
print("absolute difference between min and avg :",abs_min)
print("absolute difference between max and avg :",abs_max)
if abs_min > abs_max:
    print("The absolute difference between min and average is greater.")
elif abs_min < abs_max:
    print("The absolute difference between max and average is greater.")
else:
    print("The absolute differences are equal.")

#Find the middle country(ies) in the countries list
from countries1 import countries
last_index = len(countries)-1
print(last_index)
middle_index = int(last_index/2)
print(middle_index)
if last_index%2 !=0:
    middle_country = countries[middle_index]
    print("middle country is ",middle_country)
else:
    middle_country = countries[middle_index]
    mid = countries[middle_index+1]
    print("middle countries are",middle_country,",",mid)

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[0:96]
print("first half = ", first_half)
second_half = countries[97:]
print("second half =",second_half)
print(len(first_half))
print(len(second_half))

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countriess = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch,R,U,*scandic = countriess
print(ch)
print(R)
print(U)
print(scandic)



