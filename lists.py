# Lists in Python
friends = ["Bruce","Patrick","Tyler","John","Blake","Dom"]
trash = [1,True,False,3.4,"Random"]

# Printing list values using indexes
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

# Printing list values using negative indexing
print(friends[-1])
print(friends[-2])
print(friends[-3])
print(friends[-4])

# Selecting a portion from a list
print(friends[1:])
# Selecting a range from a list
print(friends[1:4])

# Updating a value of a list using its index
friends[1] = "Mike"
print(friends[1])