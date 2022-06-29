import datetime
import time

option = input("Do you want to use the clock (C), the timer (T) or the stopwatch (S)?\n> ")

def stopwatch():
    start_time = time.time()
    last_time = start_time
    lap_number = 1
    user_input = ""

    print("Press ENTER for new lap.\nType Q and press ENTER to quit.")

    while user_input.lower() != "q":

        # User input
        user_input = input("> ")

        # Current lap-time
        # round() is rounding the number
        lap_time = round((time.time() - last_time), 2)

        # Total time
        total_time = round((time.time() - start_time), 2)

        # Printing the information
        print("-" * 20)
        print("Lap No. " + str(lap_number))
        print("Total Time: " + str(total_time))
        print("Lap Time: " + str(lap_time))
        print("-" * 20)

        # Updating the information
        last_time = time.time()
        lap_number += 1

    print("Finished!")

def timer():

    # Inputs for stopwatch
    input_hours = input("Enter number of hours:\n> ")
    input_minutes = input("Enter number of minutes:\n> ")
    input_seconds = input("Enter number of seconds:\n> ")

    # Converting blank input to 0 and checking for numbers
    try:
        convert = lambda x: "0" if x == "" else x
        h = int(convert(input_hours))
        m = int(convert(input_minutes))
        s = int(convert(input_seconds))

    except:
        print("Values need to be numbers.")

    # Total number of seconds
    total_seconds = h * 3600 + m * 60 + s

    """  # Checks if total_seconds are more than zero
    while total_seconds > 0:

        # Time left
        time_left = datetime.timedelta(seconds = total_seconds)

        # Prints the time left
        print("Time left:", time_left, end = '\r')

        # 1 second delay
        time.sleep(1)

        # Reduces total_time by 1 second
        total_seconds -= 1 """

    # updated to fit in for loop
    for second in reversed(range(total_seconds+1)):
        print("Time left:", second, end="   \r")
        time.sleep(1)

    print("BZZZZT!!! Finished!")

def clock():
    show_date = input("Do you want to see the date? (Y/N)\n> ")

    if show_date.lower() == "y":

        actual = datetime.datetime.now()
        date_formatted = actual.strftime("Date: %d %B %Y")
        print(date_formatted)

    # Infinite loop
    while True:

        # Getting actual time from computer
        actual = datetime.datetime.now()

        # Printing actual time and date

        time_formatted = actual.strftime("Time: %H:%M:%S")
        print(time_formatted, end = '\r')

        time.sleep(1)

if option.lower() == "t":
    timer()
elif option.lower() == "s":
    stopwatch()
elif option.lower() == 'c' or option.lower() == "":
    clock()
