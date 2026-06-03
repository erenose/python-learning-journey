
# Practicing methods of Lists

# Stores these numbers and assigns them to List
List = [5, 5, 2, 1, 7, 4]

# Adds 10 to the end of the list
List.append(10)

# Adds 10 as the 3rd number in the list
List.insert(3, 10)
print(List)

# Removes one of the 5's from the list
print(List.remove(5))
print(List)

# Removes Last item from list  "10"
print(List.pop())
print(List)

# Counts how many times 5 is in the List
print(List.count(5))
# Counts what order in number 2 is
print(List.index(2))

# Looks if 5 is in the List and responds with true/false
print(5 in List)

# Sort out the List from  least to greatest
List.sort()
print(List)

# Sorts out the List from greatest to least
List.reverse()
print(List)

# Copies the Original List
List2 = List.copy()
print(List2)
