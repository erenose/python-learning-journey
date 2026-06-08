
customer = {
    'name': 'John Smith',
    'age': 30,
    "is_verified": True
}
print(customer['name'])

print(customer.get('b-day', 'Jan 1st 1980'))


# practice
phone = input('Phone: ')
digits_mapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}
output = ""
for character in phone:
    output += digits_mapping.get(character, '!') + " "
print(output)
