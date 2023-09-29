import tkinter as tk
import winsound
import time
from PIL import Image, ImageTk
import threading
import random

window = tk.Tk()
window.title("Exercise 5")
window.geometry("800x800")

island = tk.Canvas(window, width=100, height=500, bg="yellow")
island.grid(row=1, column=1, rowspan=5)
island.create_text(50, 250, text="island", fill="white", font=("Arial", 12, "bold"))

continent = tk.Canvas(window, width=100, height=500, bg="purple")
continent.grid(row=1, column=5, rowspan=5)
continent.create_text(50, 250, text="continent", fill="white", font=("Arial", 12, "bold"))

# erne_monkey = tk.Canvas(window, width=100, height=100, bg="brown")
# erne_monkey.create_text(50, 50, text="monkey", fill="white", font=("Arial", 12, "bold"))

# kerne_monkey = tk.Canvas(window, width=100, height=100, bg="red")
# kerne_monkey.create_text(50, 50, text="monkey", fill="white", font=("Arial", 12, "bold"))

word_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
word_label.grid(row=9, column=5)

word_label2 = tk.Label(window, text="", font=("Arial", 12, "bold"))
word_label2.grid(row=11, column=5)

emergencyMessage = "We are stuck on the island please send help"
word_to_teach = ""
eat_probability = 0.01
monkeys_reached_continent = 0
total_monkeys = 0
erne_monkeys = []
kerne_monkeys = []

def create_erne_monkey():
    monkey = tk.Canvas(window, width=100, height=100, bg="brown")
    monkey.create_text(50, 50, text="monkey", fill="white", font=("Arial", 12, "bold"))
    return monkey

def create_kerne_monkey():
    monkey = tk.Canvas(window, width=100, height=100, bg="red")
    monkey.create_text(50, 50, text="monkey", fill="white", font=("Arial", 12, "bold"))
    return monkey

def move_monkey(monkey_canvas, y_start):
    global word_to_teach, monkeys_reached_continent, total_monkeys
    x_start = island.winfo_x() + island.winfo_width() // 2
    x_target = continent.winfo_x() + continent.winfo_width() // 2
    y_target = continent.winfo_y() + continent.winfo_height()  // 2

    distance_x = x_target - x_start
    step_size = distance_x / 100  # Adjust the step size as needed

    eaten_by_shark = False

    for step in range(100):
        x = x_start + step * step_size

        if not eaten_by_shark and random.random() < eat_probability:
            word_label2.config(text="Monkey eaten by shark")
            print("eaten by shark")
            eaten_by_shark = True            
            winsound.Beep(200,100)
            monkey_canvas.destroy()

        if not eaten_by_shark:
            monkey_canvas.place(x=x, y=y_start)
            winsound.Beep(440, 100)
            window.update()  # Update the window to show the new position
            window.after(50)  # Delay for smoother animation (adjust as needed)
            
        print(f"Step {step + 1}/{100}")
        
        if monkey_canvas.winfo_exists() == 0:
            return
        
    if not eaten_by_shark and monkey_canvas.winfo_exists():
        monkey_canvas.place(x=x_target, y=y_start)
        winsound.Beep(840, 500)
        word_label.config(text=word_to_teach)
        monkeys_reached_continent += 1

        
def send_erne_monkey_with_word(word_number):
    global word_to_teach
    words = emergencyMessage.split()
    if words:
        random_word_index = random.randint(0, len(words) - 1)
        word_to_teach = words[random_word_index]
        monkey_canvas = create_erne_monkey()
        erne_monkeys.append(monkey_canvas)
        y_start = island.winfo_y()
        threading.Thread(target=move_monkey, args=(monkey_canvas,y_start)).start()
        # Adjust the eat_probability
        # adjust_eat_probability()
    else:
        print("Invalid word number")

def send_kerne_monkey_with_word(word_number):
    global word_to_teach
    words = emergencyMessage.split()
    if words:
        random_word_index = random.randint(0, len(words) - 1)
        word_to_teach = words[random_word_index]
        monkey_canvas = create_kerne_monkey()
        kerne_monkeys.append(monkey_canvas)
        y_start = island.winfo_y() + island.winfo_height() - 105
        threading.Thread(target=move_monkey, args=(monkey_canvas,y_start)).start()
        # adjust_eat_probability()
    else:
        print("Invalid word number")
        
# # Adjust the eat_probability dynamically to achieve a 50% success rate
# def adjust_eat_probability():
#     global eat_probability, total_monkeys,monkeys_reached_continent
#     total_monkeys += 1  # Double the probability to increase success rate

#     if monkeys_reached_continent == 0:
#         eat_probability = 0.01  # Double the probability to increase success rate
#     else:
#         success_rate = monkeys_reached_continent / total_monkeys
#         # Adjust the eat_probability based on the success rate
#         max_probability = 0.1  # Set a maximum threshold for eat_probability
#         eat_probability = min(max_probability, eat_probability * (1 + 0.1 * (0.5 - success_rate)))   

#     print(f"Adjusted eat_probability: {eat_probability}")

def teach_monkey_word(emergency_message, word_number):
    words = emergency_message.split()
    if 0 <= word_number < len(words):
        return words[word_number]
    else:
        print("Invalid word number")
        return ""

def send_ten_monkeys():
    for i in range(10):
        send_erne_monkey_with_word(4)

word_to_send = teach_monkey_word(emergencyMessage, 4)

kerne_monkey_button = tk.Button(window, text="Kerne send monkey", command=lambda: send_kerne_monkey_with_word(4))
kerne_monkey_button.grid(row=7, column=1)

erne_monkey_button = tk.Button(window, text=f"Ernesti send monkey", command=lambda: send_erne_monkey_with_word(4))
erne_monkey_button.grid(row=8, column=1)

erne_monkeys_button = tk.Button(window, text=f"Ernesti send 10 monkeys", command=lambda: send_ten_monkeys())
erne_monkeys_button.grid(row=9, column=1)

koristetta = tk.Label(window, text="").grid(row=0, column=0)
point_button = []
for i in range(5):
    button_temp = tk.Button(window, text="Points: " + str(i + 1), padx=40)
    button_temp.grid(row=0, column=i + 1)
    point_button.append(button_temp)

def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440 + i * 100, 500)

i_suppose_i_have_earned_so_much_points(2)
window.mainloop()
