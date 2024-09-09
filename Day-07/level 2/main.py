A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#Join A and B
c = A.union(B)
print(c)

#Find A intersection B
I = A.intersection(B)
print(I)

#Is A subset of B
S = A.issubset(B)
print(S)

#Are A and B disjoint sets
D = A.isdisjoint(B)
print(D)

#Join A with B and B with A
J = A.union(B)
O = B.union(A)
print(J)
print(O)

#What is the symmetric difference between A and B
s = A.symmetric_difference(B)
print(s)

#Delete the sets completely
del A 
del B 

