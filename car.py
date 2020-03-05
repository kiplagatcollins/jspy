command = ""
started = False

while True:
    command = input(">").lower()
    if command =="start":
        if started:
            print("The car is already started")
        else:
            started = True
            print("Car Started")
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print("The car is stopped")
    elif command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to quit        
        """)
    elif command =="quit":
        break
    else:
        print("Sorry, I dont understand that command")
