import tkinter as tk
import winsound
import time
from PIL import Image,ImageTk
import threading

window=tk.Tk()
window.title("Exercise 5")
window.geometry("800x800")

island = tk.Canvas(window, width=100, height=500, bg="green")
island.grid(row=1, column=1, rowspan=5)
island.create_text(50, 250, text="island", fill="white", font=("Arial", 12, "bold"))

continent = tk.Canvas(window, width=100, height=500, bg="blue")
continent.grid(row=1, column=5, rowspan=5)
continent.create_text(50, 250, text="continent", fill="white", font=("Arial", 12, "bold"))

monkey = tk.Canvas(window, width=100, height=100, bg="red")
monkey.create_text(50, 50, text="monkey", fill="white", font=("Arial", 12, "bold"))

word_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
word_label.grid(row=9, column=5)

emergencyMessage="We are stuck on the island please send help"
word_to_teach = ""

def move_erne_monkey():
    global word_to_teach
    x_start = island.winfo_x() + island.winfo_width() // 2
    y_start = island.winfo_y()
    x_target = continent.winfo_x() + continent.winfo_width() // 2
    y_target = continent.winfo_y() + continent.winfo_height()  // 2

    distance_x = x_target - x_start
    step_size = distance_x / 100  # Adjust the step size as needed

    # Move the monkey horizontally
    for step in range(100):
        x = x_start + step * step_size
        monkey.place(x=x, y=y_start)
        winsound.Beep(440,100)
        window.update()  # Update the window to show the new position
        window.after(50)  # Delay for smoother animation (adjust as needed)

        #Prints monkey movement
        print(f"Step {step + 1}/{100} - X: {x}, Y: {y_start}")

    # Ensure the monkey reaches the target
    monkey.place(x=x_target, y=y_start)
    winsound.Beep(840,500)

    # Display the word at the target position
    word_label.config(text=word_to_teach)
    
# button=tk.Button(window,text="erne send monkey ",command=move_erne_monkey)
# button.grid(row=6,column=1)

def send_monkey_with_word():
    global word_to_teach
    word_to_teach = "Help"
    threading.Thread (target=move_erne_monkey).start()

def move_kerne_monkey():
    x_start = island.winfo_x() + island.winfo_width() // 2
    y_start = island.winfo_y() + island.winfo_height() - 105
    x_target = continent.winfo_x() + continent.winfo_width() // 2
    y_target = continent.winfo_y() + continent.winfo_height()  // 2

    distance_x = x_target - x_start
    step_size = distance_x / 100  # Adjust the step size as needed

    # Move the monkey horizontally
    for step in range(100):
        x = x_start + step * step_size
        monkey.place(x=x, y=y_start)
        window.update()  # Update the window to show the new position
        window.after(50)  # Delay for smoother animation (adjust as needed)

        #Prints monkey movement
        print(f"Step {step + 1}/{100} - X: {x}, Y: {y_start}")

    # Ensure the monkey reaches the target
    monkey.place(x=x_target, y=y_start)
 
button=tk.Button(window,text="kerne send monkey ",command=move_kerne_monkey)
button.grid(row=7,column=1)   

#function that defines monkey that have been taught a word
def teach_monkey_word(emergencyMessage, wordNumber):
    # Split the emergency message into words
    words = emergencyMessage.split()
    # Check if the wordNumber is within the range of words in the message
    if 0<= wordNumber < len(words):
        # Get the word at the specified wordNumber
        word_to_teach = words[wordNumber]

        # Update the text on the monkey's canvas to show the word
        monkey.create_text(50, 250, text=word_to_teach, fill="white", font=("Arial", 12, "bold"))
    else:
        print("Invalid word number")

teach_monkey_word(emergencyMessage, 2)


send_monkey_button = tk.Button(window, text="Ernesti send monkey with word", command=send_monkey_with_word)
send_monkey_button.grid(row=8, column=1)

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

# example ...
i_suppose_i_have_earned_so_much_points(1)
window.mainloop()

#-luo toiminto säikeistystä (threading) käyttäen, 
#jolla Ernesti voi lähettää yksittäisen apinan mukanaan yksi sana kohti manteretta.
#Threading toimii mutta kuva bugaa