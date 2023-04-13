# Using functions with lists in python
lucky_numbers = [7,3,65,76,223]
friends = ["Bruce","Patrick","Tyler","John","Blake","Dom","Dom"]

# Append a list
# friends.extend(lucky_numbers)

# Append an element to a list
friends.append("Sean")

# Insert an element on a particular index
friends.insert(1,"Sam")

# Remove an element using its value from a list
friends.remove("Sam")

# Clear a list
# friends.clear()

# Pop from list
friends.pop()

# Find index using value
print(friends.index("Tyler"))

# Count the number of similar elements
print(friends.count("Dom"))

# Sort a list in ascending order
lucky_numbers.sort()

# Reverse a list
lucky_numbers.reverse()

# Copy a list
friends2 = friends.copy()

print(friends)
