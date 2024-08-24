#Declare an empty list
E = []
print(len(E))

#Declare a list with more than 5 items
colors = ['black','blue','green','pink','white','maroon','purple']
print("colors :",colors)

#Find the length of your list
print(len(colors))

#Get the first item, the middle item and the last item of the list
first_item = colors[0]
print("first item :",first_item)
last_index = len(colors)-1 
last_item = colors[last_index]
print("last item :",last_item)
middle_index = int(last_index/2)
middle_item = colors[middle_index]
print("middle item:",middle_item)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['varshini',21,5.2,'single','Fort road warangal']
print(mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#Print the list using print()
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
first_company = it_companies[0]
print("first company :",first_company)
last_index = len(it_companies)-1 
last_company = it_companies[last_index]
print("last company :",last_company)
middle_index = int(last_index/2)
middle_company = it_companies[middle_index]
print("middle company:",middle_company)

#Print the list after modifying one of the companies
it_companies[0] = 'AU'
print(it_companies)

#Add an IT company to it_companies
it_companies.append('Facebook')
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(4,'TATA')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()
print(it_companies)

#Join the it_companies with a string '#;  '
s = ['#; ']
it_companies.extend(s)
print(it_companies)

#Check if a certain company exists in the it_companies list.
print(it_companies.index('Apple'))

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
ic = it_companies[:3]
print(ic)

#Slice out the last 3 companies from the list
lc = it_companies[-4:-1]
print(lc)

#Slice out the middle IT company or companies from the list
mc = it_companies[4:6]
print(mc)

#Remove the first IT company from the list
it_companies.remove('TATA')
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies.pop(4)
print(it_companies)

#Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

#Remove all IT companies from the list
del it_companies[:]
print(it_companies)

#Destroy the IT companies list
it_companies.clear()
print(it_companies)

#Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fb = front_end + back_end
print(fb)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = fb.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)
    


