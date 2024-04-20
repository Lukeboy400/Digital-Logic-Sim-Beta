import tkinter as tk
from screeninfo import get_monitors

def button1click():
    print("Button 1 clicked!")
    
def button2click():
    print("Button 2 clicked!")

#Initialize the screen
primary_monitor = get_monitors()[0]
screen_height = primary_monitor.height
screen_width = primary_monitor.width
half_width = screen_width // 2
half_height = screen_height // 2

# Create a window  
window = tk.Tk()
window.title("Digital Logic Sim V 1.0.0")
window.geometry(f"{screen_width}x{screen_height}")
window.resizable(False, False)

def text_display(txt, x_pos, y_pos):
    text = tk.Label(window, text=txt)
    text.place(x=x_pos, y=y_pos)
    
def button_create(txt, offsetx, offsety, function):
    button = tk.Button(window, text=txt, command=function)
    button.place(x=(half_width + offsetx), y=(half_height + offsety))

# Add buttons
button_create("Click Me!", 0, 0, button1click)
button_create("Also Me!", 200, 0, button2click)

def window_update():
    text_display("Hi", half_width, 500)
    window.after(100, window_update)

window.after(0, window_update)

window.mainloop()
