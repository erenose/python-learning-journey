
total_min = int(input('Total Mins worked today? '))
hour = total_min // 60 # divides min/60 for the hour
remaining_min = total_min % 60 # "//" gets the remaining units "min"
if hour < 4: # if hour is less than 4 hours
    print('Part-Time Short Shift')
elif 4 <= hour < 8: # if hour is greater than or equal to 4 and less than 8 
    print('Standard Full-Time Shift')
else:   # anything greater than 8 
    print('Overtime Shift detected')
print(f'{hour} hr and {remaining_min} minutes')

