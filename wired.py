#This file is used to run ELixir Training FMS with all arduino's wired to the laptop or raspberry pi running Elixir
#Imports
import serial
import time
from playsound import playsound

#Setup our serial connection (change the COM port to the COM port your arduino is running on)
hub_ser = serial.Serial("COM2", 9600, timeout=1)

running = True
while running == True:
    #Setup our game
    print("Press the A button to start the game.")
    waiting = True
    while waiting == True:
        start = hub_ser.readline()
        score = 0

        if start == "start_button_pushed":
            waiting = False

    print("Countdown starts in 5 seconds.")
    time.sleep(5)
    print("Game starts in:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    game_running = True
    start_time = time.time()
    print("Game started!")
    playsound("audio/start.wav")

    while game_running == True:
        end_time = time.time()
        if end_time - start_time >=120:
            game_running = False
        if end_time - start_time >= 90 and end_time - start_time <= 90.1:
            playsound("audio/horn.wav")
        
        hub_data = hub_ser.readline()

        if hub_data == "upper_hub":
            score = score + 2
        elif hub_data == "lower_hub":
            score = score + 1
        else:
            score = score + 0

    hang = input("Did the bot hang? (y/n): ")
    if hang == "y":
        hang_points = int(input("How many hang points did they get? "))
    else:
        hang_points = 0

    score = score + hang_points

    print("Your match score is:", score)