
one = 1
two = 2
three = one + two

# print(three) 
# print(type(three))
 
# comp = 3.43j
# print(type(comp))   #Complex

mylist = ['Rhino', 'Grasshopper', 'Flamingo', 'Bongo']
B = len(mylist) # This will return the length of the list which is 3. The index is 0, 1, 2, 3.
print(mylist[1]) # This will return the value at index 1, which is 'Grasshopper'
print(mylist[0:1]) # This will return the first 3 elements in the list.
print(mylist[1:]) # is equivalent to "1 to end"
print(len(mylist)) 

# Example:
# [1:5] is equivalent to "from 1 to 5" (5 not included)
# [1:] is equivalent to "1 to end"
# [len(a):] is equivalent to "from length of a to end"


#---------

tups  = ('TupName', 'TupsAddress', 'TupsContact') #@TUPLE
listo = ['ListName', 'Address', 'Contact']
print(type(tups))
print(type(listo))

print(tups[0], tups[2] ) #tups[3] is out of range
print(listo[0])

#--------- 