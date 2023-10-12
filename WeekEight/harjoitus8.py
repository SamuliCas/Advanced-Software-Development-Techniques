import tkinter as tk
import winsound
import time
import random
import threading
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("laughter.wav")
pygame.mixer.music.load("eating.wav")

window=tk.Tk()
window.title("Exercise 5")
window.geometry("800x800")

# add five buttons to the top line of the window
koristetta=tk.Label(window,text="").grid(row=0,column=0)
point_button=[]
for i in range(5):
    button_temp=tk.Button(window,text="Points: "+str(i+1),padx=40)
    button_temp.grid(row=0,column=i+1)
    point_button.append(button_temp)
def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)    
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440+i*100,500)

# Create a list to store island locations
island_locations = []

# Create a list to store monkeys on the island
monkeys = []

# Define a lock to prevent concurrent access to monkeys
monkey_lock = threading.Lock()

# Function to generate a unique sound effect for each monkey
def generate_monkey_sound():
    return 200 + random.randint(0, 800)

# Function to simulate a monkey's life on the island
def monkey_life(monkey):
    laughter_sound = pygame.mixer.Sound("laughter.wav")

    while monkey['alive']:
        monkey['sound'] = generate_monkey_sound()
        winsound.Beep(monkey['sound'], 500)
        
        # Simulate a 1% chance of monkey's death
        if random.randint(1, 100) <= 1:
            monkey['alive'] = False
            # Play "laughter.wav" when a monkey dies
            laughter_sound.play()
            remove_monkey_oval(monkey['oval'])

        time.sleep(10)  # Wait for 10 seconds between sounds

# Function to remove the oval associated with a monkey from the canvas
def remove_monkey_oval(oval):
    sea_canvas.delete(oval)

# Function to generate a random location for a new island
def generate_random_location(existing_locations, max_attempts=100):
    for _ in range(max_attempts):
        x = random.randint(0, 7)  # Assuming an 8x8 grid for the sea
        y = random.randint(1, 7)  # Leave the top row for buttons
        new_location = (x, y)
        if (new_location not in existing_locations) and (not is_adjacent(new_location, existing_locations)):
            return new_location
    return None

# Function to check if a location is adjacent to any existing islands
def is_adjacent(new_location, existing_locations):
    x, y = new_location
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (x + dx, y + dy) in existing_locations:
                return True
    return False

## Function to create a new island
def create_new_island():
    if len(island_locations) >= 10:
        return  # Limit the number of islands to 10

    new_location = generate_random_location(island_locations)
    if new_location:
        island_locations.append(new_location)
        x, y = new_location
        sea_canvas.create_rectangle(x * 100, (y - 1) * 100, (x + 1) * 100, y * 100, fill="green")

        # Calculate coordinates for each monkey within the island
        monkey_size = 20  # Adjust the size as needed
        margin_x = (100 - monkey_size * 5) / 2
        margin_y = (100 - monkey_size * 2) / 2

         # Create 10 monkeys for the new island
        for i in range(10):
            new_monkey = {
                'sound': generate_monkey_sound(),
                'alive': True,
            }
            monkeys.append(new_monkey)

            monkey_x = x * 100 + margin_x + (i % 5) * monkey_size
            monkey_y = (y - 1) * 100 + margin_y + (i // 5) * monkey_size

            # Draw individual oval for each monkey
            monkey_oval = sea_canvas.create_oval(
                monkey_x, monkey_y,
                monkey_x + monkey_size, monkey_y + monkey_size,
                fill="brown"
            )

            new_monkey['oval'] = monkey_oval  # Store the oval reference in the monkey dictionary

            # Start a new thread for the monkey's life
            monkey_thread = threading.Thread(target=monkey_life, args=(new_monkey,))
            monkey_thread.start()

# Function to make some monkeys swim to the ocean
def make_monkeys_swim():
    num_monkeys_to_swim = min(len(monkeys), 5)  # Let a maximum of 5 monkeys swim
    monkeys_swimming = random.sample(monkeys, num_monkeys_to_swim)
    
    for monkey in monkeys_swimming:
        monkey['alive'] = False
        swim_monkey_to_ocean_threaded(monkey['oval'])

# Function to check if a monkey gets eaten while swimming
def monkey_gets_eaten():
    return random.randint(1, 100) <= 10

# Modify the swim_monkey_to_ocean function
def swim_monkey_to_ocean(monkey_oval):
    # Get the initial and final coordinates for the monkey's animation
    start_x, start_y, _, _ = sea_canvas.coords(monkey_oval)
    final_x = start_x
    final_y = sea_canvas.winfo_height()  # Move to the bottom of the canvas

    eaten_sound = pygame.mixer.Sound("eating.wav")

    # Calculate the number of steps for the animation
    num_steps = 200

    # Calculate the step size for each movement
    step_x = (final_x - start_x) / num_steps
    step_y = (final_y - start_y) / num_steps

    # Create a moving oval to represent the monkey during the animation
    moving_monkey = sea_canvas.create_oval(start_x, start_y, start_x, start_y, fill="brown")

    # Animate the monkey's movement to the ocean
    for step in range(num_steps):
        time.sleep(0.1)  # Delay between movements
        sea_canvas.move(monkey_oval, step_x, step_y)
        sea_canvas.update()  # Update the canvas to show the intermediate step

        if step == num_steps // 2 and monkey_gets_eaten():
            sea_canvas.delete(moving_monkey)  # Remove the moving oval
            sea_canvas.delete(monkey_oval)
            # Play "laughter.wav" when a monkey dies
            eaten_sound.play()
            return  # Monkey gets eaten

    # Remove the moving oval and update the original monkey's position
    sea_canvas.delete(moving_monkey)
    sea_canvas.coords(monkey_oval, final_x, final_y)

# Function to make a monkey swim to the ocean in a separate thread
def swim_monkey_to_ocean_threaded(monkey_oval):
    swim_thread = threading.Thread(target=swim_monkey_to_ocean, args=(monkey_oval,))
    swim_thread.start()

# Function to clear all islands and monkeys
def clear_all_islands_and_monkeys():
    global island_locations, monkeys
    island_locations = []  # Clear island locations
    for monkey in monkeys:
        monkey['alive'] = False  # Stop monkey threads
    monkeys = []  # Clear monkeys list
    sea_canvas.delete("all")  # Clear the canvas

# Create the sea background
sea_canvas = tk.Canvas(window, width=800, height=700, bg="blue")
sea_canvas.grid(row=1, columnspan=6)

# Create the "NEW ISLAND" button
new_island_button = tk.Button(window, text="NEW ISLAND", command=create_new_island)
new_island_button.grid(row=0, column=6)
 
# Create the "CLEAR ALL" button
clear_all_button = tk.Button(window, text="CLEAR ALL", command=clear_all_islands_and_monkeys)
clear_all_button.grid(row=0, column=8)

# Create the "MAKE MONKEYS SWIM" button
make_monkeys_swim_button = tk.Button(window, text="MAKE MONKEYS SWIM", command=make_monkeys_swim)
make_monkeys_swim_button.grid(row=0, column=7)

i_suppose_i_have_earned_so_much_points(2)
window.mainloop()
