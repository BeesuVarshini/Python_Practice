#Create an empty tuple
t = ()
print(t)

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('rishi','ricky','micky')
sisters = ('sunitha','divya')
siblings = brothers+sisters
print(siblings)

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append('prabhakar')
siblings.append('sunitha')
print(siblings)
siblings = tuple(siblings)
family_members = siblings
print(family_members)






