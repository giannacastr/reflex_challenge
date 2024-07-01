import random
import time
import keyboard
import os

def topTen():
    # Step 1: Create a file if it doesn't exist
    filePath = "reaction_scores.txt"
    if not os.path.exists(filePath):
        with open(filePath, 'w') as f:
            f.write("Top 10 Reaction Times:\n")

    # Step 2: Read and display the top 10 reaction times
    with open(filePath, 'r') as f:
        print(f.read())

def randomCountdown():
    timers = [2, 3, 4, 5]
    t = random.choice(timers)
    while t > 0:
        print(f"Countdown: {t // 60:02}:{t % 60:02}", end="\r")  # display minutes and seconds
        time.sleep(1)  # wait for 1 second
        t -= 1
    print("Countdown complete!")

def on_key_event(event, targetKey, startTime):
    global matchTarget
    if event.event_type == keyboard.KEY_DOWN:
        if event.name.upper() == targetKey.upper():
            keyboard.unhook_all()  # Unhook all keyboard events
            print(f"Target key '{targetKey}' pressed!")
            endTime = time.time()  # stop timer
            elapsedTime = endTime - startTime
            print(f"Reaction time: {elapsedTime:.2f} seconds")
            return elapsedTime
    return None

def reflexChallenge():
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    # Perform countdown before selecting target key
    randomCountdown()
    
    targetKey = random.choice(keys)
    print(f"Target key: {targetKey}")
    
    startTime = time.time()  # start timer
    matchTarget = None
    
    while True:
        if matchTarget is None:
            # Listen for the first key press only
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN:
                matchTarget = event.name.upper()
                elapsedTime = on_key_event(event, targetKey, startTime)  # Capture elapsedTime
                if elapsedTime is not None:
                    return elapsedTime  # Return elapsedTime if matched
        else:
            if matchTarget.upper() == targetKey:
                endTime = time.time()  # stop timer
                elapsedTime = endTime - startTime
                print(f"Reaction time: {elapsedTime:.2f} seconds")
                return elapsedTime  # Return elapsedTime when target key is matched
            else:
                matchTarget = None  # Reset matchTarget to listen for the next key press

def updateScores(userInfo, elapsedTime):
    filePath = "reaction_scores.txt"
    scores = []

    # Read existing scores
    with open(filePath, 'r') as f:
        lines = f.readlines()
        scores = [(line.strip(), float(line.split()[-2])) for line in lines[1:]]

    # Append new score
    scores.append((f"{userInfo[0]} - Class of {userInfo[1]} - Reaction time: {elapsedTime:.2f} seconds", elapsedTime))

    # Sort scores by reaction time (ascending)
    scores.sort(key=lambda x: x[1])

    # Rewrite file with sorted scores
    with open(filePath, 'w') as f:
        f.write("Top 10 Reaction Times:\n")
        for score, time in scores[:10]:  # Limit to top 10
            f.write(f"{score}\n")

def main():
    print("""Welcome to the Reflex Challenge!
Once you are ready to start, a random timer from 2-5 seconds will go off.
When it ends, you are shown a target key and your reaction timer starts.
Match the target key in the fastest time you can!""")
    
    userInfo = []
    
    name = input("Enter username: ")
    try:
        grad_year = input("What year did you graduate? ")

    except ValueError:
        print("Please input a valid number.")

    userInfo.append(name)
    userInfo.append(grad_year)

    while True:
        input("Hit enter to start.")

        # Play the reflex challenge and get the reaction time
        elapsedTime = reflexChallenge()
        userInfo.append(elapsedTime)

        # Update scores in the file
        updateScores(userInfo, elapsedTime)

        # Display top 10 reaction times
        topTen()
        playAgain = input("To exit enter 0. To keep playing enter anything else: ")
        playAgain = playAgain.replace(" ","")
        if playAgain == "0":
            print("Have a great day!")
            topTen()
            break

main()
