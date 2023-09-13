import numpy as np
import time
import random
import winsound

#-create a 100x100 space, and place Ernest's and Kernest's space rockets at the bottom 
# (on the surface of the earth) in random places
Space = np.zeros((10,10))

ErnestiRocket = {
    "location" : (9,np.random.randint(10))
}

KernestiRocket = {
    "location" :(9,np.random.randint(10))
}

# Moon = {
#     "location" :(3,8)
# }

Space[ErnestiRocket["location"][0], ErnestiRocket["location"][1]] = 1
Space[KernestiRocket["location"][0], KernestiRocket["location"][1]] = 2
# Space[Moon["location"][0], Moon["location"][1]] = 3

#Add the functionality that with a one percent probability the rocket launch goes wrong, 
#so the program execution ends here
if random.random() < 0.01:
    print("Rocket exploded due to technical issues")
else:
#next, go to the rocket launch center and somehow show in your program the launch countdown 
# "10, 9, … , 2, 1, 0", after which the launch of the space rocket will appear
    for i in range(10, 0, -1):
        print(f"Countdown: {i} seconds")
        time.sleep(1)  # Pause for 1 second

    print("Blastoff!")
        
        # Simulation parameters
    num_frames = 10  # Number of frames to simulate
    frame_delay = 1  # Delay between frames in seconds

        # Rocket movement simulation
    for frame in range(num_frames + 1):
        if frame == 0:
            print(Space)
        elif frame > 0:
        # Update rocket positions (moving straight up)
            ErnestiRocket["location"] = (ErnestiRocket["location"][0] - 1, ErnestiRocket["location"][1])
            winsound.Beep(240,500)
            KernestiRocket["location"] = (KernestiRocket["location"][0] - 1, KernestiRocket["location"][1])
            winsound.Beep(600,500)

            # Ensure rocket remains within bounds
            ErnestiRocket["location"] = (
                max(0, ErnestiRocket["location"][0]),
                min(99, ErnestiRocket["location"][1])
            )
            KernestiRocket["location"] = (
                max(0, KernestiRocket["location"][0]),
                min(99, KernestiRocket["location"][1])
            )

            # Clear the Space array and mark the new rocket positions
            Space.fill(0)
            Space[ErnestiRocket["location"][0], ErnestiRocket["location"][1]] = 1
            Space[KernestiRocket["location"][0], KernestiRocket["location"][1]] = 2
    
            print(Space)
            print(f"Frame {frame}")

            # Check if either rocket has reached the top row
            if ErnestiRocket["location"][0] == 0 or KernestiRocket["location"][0] == 0:
                print("Rockets have reached the top. Program ends.")
                break

        time.sleep(frame_delay)