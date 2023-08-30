import numpy as np
import keyboard
import matplotlib.pyplot as plt
from matplotlib import colors

# Create the Jungle matrix
Jungle = np.zeros((100, 100))

# Create the dictionaries for Ernesti and Kernesti
Ernesti = {
    "name": "Ernesti",
    "location": [25, 50]  # Row 25, Column 50 in the Jungle matrix
}

Kernesti = {
    "name": "Kernesti",
    "location": [75, 30]  # Row 75, Column 30 in the Jungle matrix
}

# Function to update location and Jungle matrix
def update_location(character, direction):
    new_location = character["location"].copy()
    
    if direction == "up":
        new_location[0] = max(new_location[0] - 1, 0)
    elif direction == "down":
        new_location[0] = min(new_location[0] + 1, Jungle.shape[0] - 1)
    elif direction == "left":
        new_location[1] = max(new_location[1] - 1, 0)
    elif direction == "right":
        new_location[1] = min(new_location[1] + 1, Jungle.shape[1] - 1)
    
    # Clear the old position
    Jungle[character["location"][0], character["location"][1]] = 0
    
    character["location"] = new_location
    Jungle[character["location"][0], character["location"][1]] = 1

# Set up the plot
cmap = colors.ListedColormap(['white', 'green'])
plt.figure(figsize=(8, 8))
plt.imshow(Jungle, cmap=cmap, origin='upper')
plt.title("Jungle Adventure")
plt.show(block=False)

# Main loop
current_character = Ernesti  # Start with Ernesti
print("Current Character:", current_character["name"])

while True:
    if keyboard.is_pressed("q"):  # Press 'q' to quit the program
        break
    
    if keyboard.is_pressed("up") or keyboard.is_pressed("down") or keyboard.is_pressed("left") or keyboard.is_pressed("right"):
        if keyboard.is_pressed("up"):
            update_location(current_character, "up")
        elif keyboard.is_pressed("down"):
            update_location(current_character, "down")
        elif keyboard.is_pressed("left"):
            update_location(current_character, "left")
        elif keyboard.is_pressed("right"):
            update_location(current_character, "right")
        
        # Update the plot
        plt.clf()
        plt.imshow(Jungle, cmap=cmap, origin='upper')
        plt.title("Jungle Adventure")
        plt.pause(0.001)
        
        current_character = Kernesti if current_character == Ernesti else Ernesti
        print("Current Character:", current_character["name"])

print("Program ended.")
