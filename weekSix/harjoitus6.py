# Link to the video
# https://youtu.be/IMUJXfJChUw

import tkinter as tk 
import winsound 
import time 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading


window = tk.Tk() 
window.title("Exercise 5") 
window.geometry("700x700") 
# Configure row and column weights
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# add five buttons to the top line of the window 
koristetta = tk.Label(window, text="").grid(row=0, column=0) 
point_button = [] 
for i in range(5): 
    button_temp = tk.Button(window, text="Points: "+str(i+1), padx=40) 
    button_temp.grid(row=0, column=i+1) 
    point_button.append(button_temp) 

def i_suppose_i_have_earned_so_much_points(amount_of_points): 
    for i in range(5): 
        point_button[i].configure(bg='gray') 
        time.sleep(1)
    for i in range(amount_of_points): 
        point_button[i].configure(bg='green') 
        winsound.Beep(440+i*100, 500) 

# Create the main canvas for ocean and island
ocean = tk.Canvas(window, width=600, height=600, bg="blue")
ocean.grid(row=3, column=3, rowspan=2, columnspan=2)

island = tk.Canvas(window, width=400, height=300, bg="yellow")
island.grid(row=3, column=3, rowspan=2, columnspan=2)

# Create the pool and position it within the island
pool = tk.Canvas(island, width=60, height=20, bg="green")
pool.grid(row=1, column=1, padx=170, pady=70)

# Create the Ernesti_ditch starting from the border of the pool to the border of the island
ernesti_ditch = island.create_line(180, 70, 180, -30, fill="black")

# Create the Kernesti_ditch starting from the border of the pool to the border of the island
kernesti_ditch = island.create_line(225, 70, 225, -30, fill="black")

# Create a variable to track the monkey's position
monkey_position = (180, 70)

# Initialize matrices
pool_matrix = np.zeros((20, 60))
ernesti_ditch_matrix = np.ones((100, 1))
kernesti_ditch_matrix = np.ones((100, 1))

def guide_monkey_to_ditch():
    global monkey_position
    target_y = -30
    while monkey_position[1] > target_y:
        island.coords(ernesti_ditch, 180, monkey_position[1], 180, target_y)
        time.sleep(0.1)
        dig_ditch_pixel(monkey_position[1])
        monkey_position = (180, monkey_position[1] - 1)

# Function to dig a ditch and update the ditch matrix
def dig_ditch_pixel(y):
    x = 180
    ditch_row = int((70 - y) / 2) 
    if ditch_row >= 0:
        if ernesti_ditch_matrix[ditch_row] == 1:
            ernesti_ditch_matrix[ditch_row] = 0 
            winsound.Beep(440, 50)
            update_ditch_display()

# Function to update the ditch display
def update_ditch_display():
    pass

# Create a thread to run the guide_monkey_to_ditch function
def start_guiding_monkey():
    guide_thread = threading.Thread(target=guide_monkey_to_ditch)
    guide_thread.start()

# Add a button to trigger the monkey guiding process
start_button = tk.Button(window, text="Start Guiding Monkey", command=start_guiding_monkey)
start_button.grid(row=6, column=3)

i_suppose_i_have_earned_so_much_points(1) 
window.mainloop()
