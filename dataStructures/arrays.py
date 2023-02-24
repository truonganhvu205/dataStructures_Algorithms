# LIST - is a collection which is ordered & changeable. Allows duplicate members.
lst = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)

print(lst[:]) # ordered

lst1 = lst[:] # changeable
lst1[0] = 0
print(lst1)

# TUPLE - is a collection which is ordered & unchangeable. Allows duplicate members.
tple = (1, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tple)

print(tple[:]) # ordered

# tple1 = tple[:] # changeable -> ERROR
# tple1[0] = 0
# print(tple1)

# SET - is a collection which is unordered & unchangeable. No duplicate members.
st = {'apple', 'banana', 'cherry', 'apple'}
print(st) # when run again -> reset order

# print(st[:]) # unordered -> ERROR

# st1 = st[:] # changeable -> ERROR
# st1[0] = 0
# print(st1)

# DICTIONARY - is a collection which is ordered & changeable. No duplicate members.
dct = {
    'name':'Vu',
    'age':18,
    'sex':'male'
    }

print(dct)

for i in dct.items(): # ordered
    print(i)

dct1 = dct.copy() # changeable
dct1['age'] = 20
print(dct1)
