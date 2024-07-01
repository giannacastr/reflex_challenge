import random
import datetime
import time
import keyboard

def topTenFile():
    topTenFilePath = "reaction_scores.txt"

def randomCountdown():
    timers = [2, 3, 4, 5]
    t = random.choice(timers)
    while t > 0:
        print(f"{t // 60:02}:{t % 60:02}", end="\r")  # display minutes and seconds
        time.sleep(1)  # wait for 1 second
        t -= 1

def on_key_event(event):
    global matchTarget, startTime
    if event.event_type == keyboard.KEY_DOWN:
        if event.name.upper() == matchTarget.upper():
            keyboard.unhook_all()  # Unhook all keyboard events
            print(f"Target key '{matchTarget}' pressed!")
            endTime = time.time()  # stop timer
            elapsedTime = endTime - startTime
            print(f"Reaction time: {elapsedTime:.2f} seconds")


def reflexChallenge():
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    targetKey = random.choice(keys)
    print(targetKey)
    randomCountdown()
    startTime = time.time() # start timer
    matchTarget = input("Enter the target: ")
    while True:
        if matchTarget is None:
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN:
                matchTarget = event.name.upper()
                keyboard.on.press(on_key_event)
                
        if matchTarget.upper() == targetKey:
            endTime = time.time() # stop timer
            elapsedTime = endTime - startTime
            print(f"Reaction time: {elapsedTime:.2f} seconds")
            break
        else:
            matchTarget = input("Wrong input. Please enter the target key: ")

reflexChallenge()