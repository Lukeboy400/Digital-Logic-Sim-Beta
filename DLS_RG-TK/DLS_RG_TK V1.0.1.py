import tkinter as tk
from screeninfo import get_monitors

def button1click():
    text_display("Button 1 clicked!", 50, 50)
    
def button2click():
    text_display("Button 2 clicked!", 100, 100)

#Initialize screen aspects
primary_monitor = get_monitors()[0]
screen_height = primary_monitor.height
screen_width = primary_monitor.width
half_width = screen_width / 2
half_height = screen_height / 2

# Create the window  
window = tk.Tk()
window.title("Digital Logic Sim V 1.0.1")
window.geometry(f"{screen_width}x{screen_height}")
window.resizable(False, False)

def text_display(txt, x_pos, y_pos):
    text = tk.Label(window, text=txt)
    text.place(x=x_pos, y=y_pos)
    
def button_create(txt, offsetx, offsety, function):
    button = tk.Button(window, text=txt, command=function)
    button.place(x=(half_width + offsetx), y=(half_height + offsety))
    
def fill(color, x1, x2, y1, y2):
    cover = tk.Frame(window, width=x2 - x1, height=y2 - y1, bg=color)
    cover.place(x=x1, y=y1)

def create_buttons():
    button_create("Click Me!", 0, 0, button1click)
    button_create("Also Me!", 200, 0, button2click)

def window_update():
    fill("light gray", 0, screen_width, 0, screen_height)
    create_buttons()
    text_display("Hi", half_width, 500)
    window.after(1000, window_update)

# Run the sript
window.after(0, window_update)
window.mainloop()
