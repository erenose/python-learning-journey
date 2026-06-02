
name = (input('Whats ur name?: '))   # write down name and code
code = (input('6 digit code: '))
if len(code) == 6:         # checks if equal to 6 
     name = name[0:3]      # takes letter from 1 to 3 word
     name = (name.upper())
     Last_three = code[-2:]
     result = int(Last_three) * 5  # converts to int(numbers)
     print(f'{name}{result}')   #prints it out
else:
    print('INVALID')  # if wrong not equal to 6 "INVALID"
