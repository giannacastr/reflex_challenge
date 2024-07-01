import random
import time
import keyboard

def topTenFile():
    topTenFilePath = "reaction_scores.txt"

def randomCountdown():
    timers = [2, 3, 4, 5]
    t = random.choice(timers)
    while t > 0:
        print(f"Countdown: {t // 60:02}:{t % 60:02}", end="\r")  # display minutes and seconds
        time.sleep(1)  # wait for 1 second
        t -= 1
    print("Countdown done")

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
    
    # Perform countdown before selecting target key
    randomCountdown()
    
    targetKey = random.choice(keys)
    print(f"Target key: {targetKey}")
    
    global startTime, matchTarget
    startTime = time.time()  # start timer
    matchTarget = None
    while True:
        if matchTarget is None:
            # Listen for the first key press only
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN:
                matchTarget = event.name.upper()
                keyboard.on_press(on_key_event)
        else:
            if matchTarget.upper() == targetKey:
                endTime = time.time()  # stop timer
                elapsedTime = endTime - startTime
                print(f"Reaction time: {elapsedTime:.2f} seconds")
                break
            else:
                matchTarget = None  # Reset matchTarget to listen for the next key press

# Start the reflex challenge
reflexChallenge()
