#Unpack siblings and parents from family_members
family_members = ('rishi', 'ricky', 'micky', 'sunitha', 'divya', 'prabhakar', 'sunitha')
parents, siblings = family_members[5:], family_members[0:5]
print(siblings)
print(parents)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('mango','apple','orange')
vegetables = ('tomato','ladies finger','potato')
animal_products = ('milk','meat')
food_stuff_tp = fruits+vegetables+animal_products
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
last_index = len(food_stuff_lt)-1
middle_index = int(last_index/2)
if len(food_stuff_lt)%2==0:
    print("middle items are",food_stuff_lt[middle_index],",",food_stuff_lt[middle_index+1])
else :
    print("middle item is",food_stuff_lt[middle_index])

#Slice out the first three items and the last three items from food_stuff_lt list
print("first 3 items are",food_stuff_lt[0:3])
print("last 3 items are",food_stuff_lt[5:])

#Delete the food_stuff_tp tuple completely
print(food_stuff_tp)
del food_stuff_tp

'''   Check if an item exists in tuple:

    Check if 'Estonia' is a nordic country

    Check if 'Iceland' is a nordic country

    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')'''
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


