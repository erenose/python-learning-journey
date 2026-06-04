
# numbers in List
List = [2, 2, 4, 6, 3, 4, 6, 1]
# Assigning a blank spot for future numbers
unique = []
# for the numbers in the list
for number in List:
# if the number is not assigned to a blank spot in "unique"
    if number not in unique:
    # Adds the number
        unique.append(number)
# Then prints it out
print(unique)
