# This is a tuple. (tup-el)  you can't change anything about it. It uses (parenthensees).Not [brackets] like lists.
coordinates = (4,5)
# We can access the elements in the tuple like this
print(coordinates[1])
# RESULT 5
print(coordinates[0])
# RESULT 4
# Let's try to access something thats's outside the range. There is no 4 index in this example.
print(coordinates[4])
# RESULT IndexError: tuple index out of range
#Lets make a LIST of TUPLES
coordinates = [(4,5), (6,7), (80,43)]
print(coordinates)
# RESULT [(4, 5), (6, 7), (80, 43)]
# TEST TEST TEST
#TEST TEST