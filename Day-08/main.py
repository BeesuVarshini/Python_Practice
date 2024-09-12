#Create an empty dictionary called dog
dog = {}
print(dog)

#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'snoopy'
dog['color'] = 'white'
dog['breed'] = 'samoyed'
dog['legs'] = '4'
dog['age'] = '1yr'
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 'sam'
student['last_name'] = 'balle'
student['gender'] = 'Female'
student['age'] = '23'
student['marital_status'] = 'single'
student['skills'] = ['Python','SQL','ML','DL']
student['country'] = 'India'
student['city'] = 'warangal'
student['address'] = 'shivanagar'
print(student)

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills')))

#Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('CSS')
print(student)

#Get the dictionary keys as a list
keys_list = list(student.keys())
print(keys_list) 

#Get the dictionary values as a list
values_list = list(student.values())
print(values_list)

#Change the dictionary to a list of tuples using items() method
print(student.items())

#Delete one of the items in the dictionary
student.popitem()
print(student)

#Delete one of the dictionaries
del dog 

























