
# numbers from 1 to 3
for x in range (4):
# numbers from 1 to 2
    for y in range (3):
# then prints out all the variations
        print(f'({x},{y})')

# practice - draw shapes with numbers in a List 

# the list 
numbers = [1, 1, 1, 2, 5]
# for the integers in the list
for x_count in numbers:
# save a text as an output
    output = ''
# counts/sees the numbers and how long they are
    for count in range (x_count):
# however long the number's space is it turns to *
        output += '*'
# prints out the final *
    print(output)

# or could do it this way

number = [1, 1, 1, 2, 5]
for x_count in number:
    print('*' * x_count)
