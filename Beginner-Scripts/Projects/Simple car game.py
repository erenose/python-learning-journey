
print('>Car is stopped...')
car_stopped = True     # Set the strings and if they're true/false
car_running = False


while True:     # will always run this cause true is well true all the time

    text = input('')  # text box that shows up all the time

    if car_running == False and text == 'start': # if the car's not running and u type "start" the car will start
            print('Car Started...')
            car_running = True
            car_stopped = False
    elif text == 'help':              # type help for the menu
            print('start- to start the car\nstop- to stop the car\nquit- to exit')

    elif car_running == True and text == 'start': # if the car is running and u type start, it prints "car is alr running"
            print('Car is alr running...')

    elif text == 'quit':            # typing quit, quits the game and breaks/ends the code program
            print('Game over....')
            break

    elif car_stopped == True and text == 'stop':   # if is alr stopped and u type stop it'll print "car is alr stopped"
            print('Car is alr stopped...')

    elif car_stopped == False and text == 'stop': # if car is not stopped and type "stop" it stops the car
            print('Car has stopped...')
            car_running = False
            car_stopped = True
    else:
            print("I Don't understand that....") # if u don't type "start" or "stop" the program won't recognize it
