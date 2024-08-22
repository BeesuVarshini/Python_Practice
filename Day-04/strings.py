#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string = 'Thirty'+' '+'Days'+' '+'Of'+' '+'Python'
print(string)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
s = 'coding'+' '+'For'+' '+'All'
print(s)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = s 

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())
 
#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
st = "Coding For All"
print(st.capitalize())
print(st.title())
print(st.swapcase())

#Cut(slice) out the first word of Coding For All string.
print(st[0:6])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(st.find('Coding'))

#Replace the word coding in the string 'Coding For All' to Python.
print(st.replace('Coding','Python'))

#Change Python for Everyone to Python for All using the replace method or other methods.
py = 'Python for All'
print(py.replace('Python','Everyone to Python'))

#Split the string 'Coding For All' using space as the separator (split()) .
print(st.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
f = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(f.split(','))

#What is the character at index 0 in the string Coding For All.
print(st[0])

#What is the last index of the string Coding For All.
print(len(st)-1)

#What character is at index 10 in "Coding For All" string.
print(st[10:11])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
P4E = 'Python For Everyone'
print(P4E)

#Create an acronym or an abbreviation for the name 'Coding For All'.
C4A = 'Coding For All'
print(C4A)

#Use index to determine the position of the first occurrence of C in Coding For All.
substring = 'C' 
print(st.index(substring))

#Use index to determine the position of the first occurrence of F in Coding For All.
substring = 'F'
print(st.index(substring))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
C = 'Coding For All People'
print(C.rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
bc = 'You cannot end a sentence with because because because is a conjunction'
print(bc.find('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(bc.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sen = 'because because because'
start_index = bc.find('because')
end_index = start_index + len(sen)
print(bc[start_index:end_index])

#Does ''Coding For All' start with a substring Coding?
print(st.startswith('Coding'))

#Does 'Coding For All' end with a substring coding?
print(st.endswith('Coding'))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string
cd = '   Coding For All      ' 
print(cd.strip())

#Which one of the following variables return True when we use the method isidentifier():
    #30DaysOfPython
    #thirty_days_of_python
d = '30DaysOfPython'
print(d.isidentifier())
t = 'thirty_days_of_python'
print(t.isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lib =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
r = ' # '.join(lib)
print(r)

#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
s1 = 'I am enjoying this challenge.'
s2 = 'I just wonder what is next.'
s3 = s1+'\n'+s2
print(s3)

#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Asabenesh\t250\tFinland\tHelsinki')

# Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14*radius**2
sen = 'The area of a circle with radius {} is {} meters square'.format(radius,area)
print(sen)

#Make the following using string formatting methods:

#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))





