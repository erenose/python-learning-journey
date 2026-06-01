import math

# Allows one to write inputs
name = input('What is ur name? ')
code = input('Ticket packaging code? ')
hrs = input('How many hrs ago u opened? ')
# if the characters don't equal 8 its prints "invalid"
if len(code) !=8:
    print('Please enter a valid code')
print(name[0:3] + code[-4:])
# hrs gotten by dividing inputed hr by 1
hrs = math.floor(float(hrs) / 1)
# set ticket price at $200
ticket_price = 200
# self explanitory
if hrs < 1:
    final_price = ticket_price - 50
    print(f'Ticket price is {final_price}$')
elif hrs >= 1 and hrs < 3:
    final_price = 200
    print(f'Ticket price is {final_price}$')
else:
    print('Sessions timed out. pls restart')
