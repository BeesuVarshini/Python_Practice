it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['TCS','Infosys','Wipro'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Amazon')
print(it_companies)

#What is the difference between remove and discard
'''if the element is not found in the set then remove() raises a 'key error' but discard() doesn't raise an error and does nothing'''




