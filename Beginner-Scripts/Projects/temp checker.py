
temps = [21,23,32,24,19]

for degree in temps:
    if degree > 30:
        print(f'[DANGER] Server overheating at', degree, 'C!')
    elif 22 <= degree <= 30:
        print('[DANGER] Temperature rising at', degree, 'C')
    else:
        print('[OK] temperature normal:', degree, 'C')



