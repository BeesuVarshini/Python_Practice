age = [22, 19, 24, 25, 26, 24, 25, 24]
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
s = set(age)
print(s)
print(len(age))
print(len(s))
if len(age)>len(s):
    print("length of list(age) is bigger than set(age)")
elif len(age)>len(s):
    print("length of set(age) is bigger than list(age)")
else :
    print("length of set(age) is equal to list(age) ")

#Explain the difference between the following data types: string, list, tuple and set
'''String: Immutable sequence of characters and used for text manipulation and storage.
   List: Mutable ordered collection of elements and used to store collections of items
   Tuple: Immutable ordered collection of elements and used when you need an ordered collection of items that should not change throughout the program.
   Set: Mutable unordered collection of unique elements and useful for storing unique items '''

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
p = sentence.split(" ")
print(p)
t = set(p)
print(t)
total_unique_words = len(t)
print(total_unique_words)
print("unique words have been used in the sentence :",t)


