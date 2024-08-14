#Write a python comment saying 'Day 2: 30 Days of python programming'
#Day 2: 30 days of python programming

#Declare a first name variable and assign a value to it
first_name = "Varshini"

#Declare a last name variable and assign a value to it
last_name = "Beesu"

#Declare a full name variable and assign a value to it
full_name = "Beesu Varshini"

#Declare a country variable and assign a value to it
country = "India"

#Declare a city variable and assign a value to it
city = "Warangal"

#Declare an age variable and assign a value to it
age = 21

#Declare a year variable and assign a value to it
year = 2003

#Declare a variable is_married and assign a value to it
is_married = False

#Declare a variable is_true and assign a value to it
is_true = "yes"

#Declare a variable is_light_on and assign a value to it
is_light_on = "yes"

#Declare multiple variable on one line
firstname,lastname,country = 'Varshini','Beesu','India'

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type({"firstname" : 'Varshini',"lastname" : 'Beesu','country' : 'India'}))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Compare the length of your first name and your last name
print(len(first_name) == len(last_name))

'''
Declare 5 as num_one and 4 as num_two
    Add num_one and num_two and assign the value to a variable total
    Subtract num_two from num_one and assign the value to a variable diff
    Multiply num_two and num_one and assign the value to a variable product
    Divide num_one by num_two and assign the value to a variable division
    Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    Calculate num_one to the power of num_two and assign the value to a variable exp
    Find floor division of num_one by num_two and assign the value to a variable floor_division
'''
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one*num_two
division = num_one/num_two
remainder = num_two%num_one
exp = num_one**num_two
floor_division = num_one//num_two
print("total : ",total)
print("diff :",diff)
print("product : ",product)
print("division : ",division)
print("remainder : ",remainder)
print("exp : ",exp)
print("floor_division : ",floor_division)

'''
The radius of a circle is 30 meters.
    Calculate the area of a circle and assign the value to a variable name of area_of_circle
    Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    Take radius as user input and calculate the area.
'''
r = 30
area_of_circle = 3.14*r*r
circum_of_circle = 2*3.14*r
print("area of circle :",area_of_circle)
print("circumference of circle :",circum_of_circle)
r = int(input("enter radius :"))
area_of_circle= 3.14*r*r
print("area of circle :",area_of_circle)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("enter first name :")
last_name = input("enter last name :")
country = input("enter country :")
age = input("enter age :")

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
