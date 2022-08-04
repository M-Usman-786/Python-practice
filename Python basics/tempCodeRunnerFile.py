command = ""
started = False
stopped = False
while command != "quit":
    command = input(">  ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started....")
    elif command == "stop":
        print("Car stopped,")
    elif command == "help":
        print("""
start -- To start the car
stop -- To stop the car
quit -- To quit
        """)
    elif command == "quit":
        print("Game quit")
    else:
        print("Sorry! i don't understand")
