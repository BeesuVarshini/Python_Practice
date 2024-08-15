# Declare your age as integer variable
age = 21

# Declare your height as a float variable
height = 5.2

# Declare a variable that store a complex number
a = 5+3j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
  #  Enter base: 20
  # Enter height: 10
  #The area of the triangle is 100
base = int(input("Enter base :"))
h = int(input("Enter height :"))
aot = 0.5*base*h
print("The area of the triangle is ",aot)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
   #Enter side a: 5
   #Enter side b: 4
   #Enter side c: 3
   #The perimeter of the triangle is 12
A = int(input("Enter side a:"))
B = int(input("Enter side b:"))
C = int(input("Enter side c:"))
pot = A+B+C 
print("The perimeter of the triangle is",pot) 

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
l = int(input("Enter length:"))
b = int(input("Enter width :"))
area = l*b 
perimeter = 2*(l+b)
print("The perimeter of the rectangle is",perimeter)
print("The area of the rectangle is",area)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("enter radius :"))
aoc = 3.14*r*r 
coc = 2*3.14*r 
print("The circumference of the circle is",coc)
print("The area of the circle is",aoc)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2
c = -2
slope = m
print("slope is ",slope)
#y-intercept(x=0)
y_intercept = (0,c)
#x-intercept(y=0)
x_intercept = (-c/m,0)
print("x-intercept :",x_intercept)
print("y-intercept :",y_intercept)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1,x2,y1,y2 = 2,6,2,10
s = (y2-y1)/(x2-x1)
euclidean_dist = ((x2-x1)**2+(y2-y1)**2)**0.5
print("slope is ",s)
print("euclidean distance is ",euclidean_dist)

#Compare the slopes in tasks 8 and 9.
print(slope == s)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
#y = ((x)**2+6*x+9) # y= a(x)**2+b*x+c
a,b,c = 1,6,9
discriminent = b**2 - 4*a*c
if discriminent == 0:
    x = -b/(2*a)
    print("the value of x where y=0 :",x)
elif discriminent >0:
    x2= (-b+(discriminent)**0.5)/2*a
    x1= (-b-(discriminent)**0.5)/2*a
    print("the values of x2 :",x2,"and x1",x1,"where y=0")
else:
    print("no real solns exist for y=0")
x=0
for n in range(-4,0):
   y3= (x)**2+6*(x)+9
   if y3==0 :
    print("value of x where y =0 is",x)
   x=x+1

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
a =print(len('python'))
b= print(len('dragon'))
print(a!=b)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print("yes on is present in both python and dragon")

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
j = 'I hope this course is not full of jargon.'
if 'jargon' in j:
    print('yes jargon is in sentence')

#Find the length of the text python and convert the value to float and convert it to string
print(len('python'))
print(float(len('python')))
print(str(len('python')))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
n = int(input("enter num :" ))
if n%2==0:
    print(n,"is even number")
else:
    print(n,"is odd number")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
d = 7//3
e = int(2.7)
print(d==e)

#Check if type of '10' is equal to type of 10
print(type('10')==type(10))

#Check if int('9.8') is equal to 10
i = int(float('9.8'))
print(i==10)

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
    #Enter hours: 40
    #Enter rate per hour: 28
    #Your weekly earning is 1120
h = int(input("enter hours :"))
rate = int(input("enter rate per hour: "))
earning = h*rate
print("your weekly earning is ",earning)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
    #Enter number of years you have lived: 100
    #You have lived for 3153600000 seconds.
years = int(input("Enter number of years you have lived:"))
total_days = 365
sec = 365*24*60*60 
print("total seconds in a year is ",sec)
total_sec = sec*years
print("You have lived for",total_sec,"seconds")

# Write a Python script that displays the following table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125
m = int(input("enter num :"))
for n in range(1,m+1):
    print(n*1," ",n**0," ",n**1," ",n**2," ",n**3)
    n=n+1






 





