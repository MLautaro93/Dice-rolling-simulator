import tkinter as tk
from PIL import Image, ImageTk
import random

# Creating the window
root = tk.Tk()
root.geometry('512x384')
root.title('Dice Rolling Simulator')
root.config(bg = 'light blue')

# Adding a header
header = tk.Label(text = 'Roll the dice!', font = 'arial 15 bold', bg = 'light blue')
header.place(relx = 0.5, y = 50, anchor = tk.CENTER)

# Images
dice = ['die_1.png', 'die_2.png', 'die_3.png', 'die_4.png', 'die_5.png', 'die_6.png']

# Function activated by the play button
def roll_dice():    
    image = Image.open(random.choice(dice)).resize((128, 128))
    img = ImageTk.PhotoImage(image)
    label = tk.Label(image = img)
    label.place(relx = .5, y = 175, anchor = tk.CENTER)
    label.image = img

# Function to exit the game
def exit():
    root.destroy()

# The Buttons
button = tk.Button(text = 'PLAY', font = 'arial 10 bold', command = roll_dice)
button.place(relx = .5, y = 300, anchor = tk.CENTER)

button = tk.Button(text = 'EXIT', font = 'arial 10 bold', command = exit)
button.place(relx = .5, y = 350, anchor = tk.CENTER)

root.mainloop()
