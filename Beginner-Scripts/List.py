
# with only 2 in print, grabs 3rd name through the end
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# can change list of name whenever we want with bracket
names[0] = 'Theodore'
print(names[2:])
# still keeps original list's of name "Non destructable"
print(names)

#practice - wrote a program to find largest number in a list

# The list
number = [1, 2, 3, 4, 5]
# Sets a starting point, max is currently 1
max = number[0]
for number in number:
# if loop finds a new number greater than our "max"
    if number > max:
# The max becomes that new number
        max = number
# this continues until it sweeps the whole list, and then prints the largest number.
print(max)
