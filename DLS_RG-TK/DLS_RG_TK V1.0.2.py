import tkinter as tk
from screeninfo import get_monitors
global draw_points
draw_points = []

# Initialize debug info for button clicks
def debug_buttons(num):
    text_display(f"Button {num} clicked!", 50, 50)
    print(f"Button {num} clicked!")

"""
Set up button actions
Note: Change function names to what the buttton does
"""
def button1click():
    debug_buttons(1)
    
def button2click():
    debug_buttons(2)

def button3click():
    debug_buttons(3)

#Initialize screen aspects
primary_monitor = get_monitors()[0]
screen_height = primary_monitor.height
screen_width = primary_monitor.width
half_width = screen_width / 2
half_height = screen_height / 2

# Create the window  
window = tk.Tk()
window.title("Digital Logic Sim V 1.0.2")
window.geometry(f"{screen_width}x{screen_height}")
window.resizable(False, False)

# Set up click actions
def left_click(event):
    x, y = event.x, event.y
    draw_points.append([x, x + 5, y, y + 5])
   
def left_click_update(event):
    x, y = event.x, event.y
    original_points = draw_points
    if original_points[-1][1] <= x:
        draw_points[-1][1] = x + 5
    else:
        draw_points[-1][0] = x
        
    if original_points[-1][3] <= y:
        draw_points[-1][3] = y + 5
    elif original_points[-1][3] > y:
        draw_points[-1][2] = y
    

# Set up basic functions
def text_display(txt, x_pos, y_pos):
    text = tk.Label(window, text=txt)
    text.place(x=x_pos, y=y_pos)
    
def button_create(txt, offsetx, offsety, function):
    button = tk.Button(window, text=txt, command=function)
    button.place(x=(half_width + offsetx), y=(half_height + offsety))
    
def fill(color, x1, x2, y1, y2):
    cover = tk.Frame(window, width=x2 - x1, height=y2 - y1, bg=color)
    cover.place(x=x1, y=y1)

# Set up per-tick functions
def create_buttons():
    button_create("Click Me!", 0, 0, button1click)
    button_create("Also Me!", 200, 0, button2click)
    
def draw(points):
    counter = 1
    for point in points:
        fill("black", point[0], point[1], point[2], point[3])
        print(f"{counter}. {point}")
        counter += 1

# Set the window loop
def window_update():
    global counter
    fill("light gray", 0, screen_width, 0, screen_height)
    create_buttons()
    text_display("Hi", half_width, 500)
    draw(draw_points)
    window.after(1000, window_update)

# Set up click detection
window.bind('<Button-1>', left_click)    
window.bind('<B1-Motion>', left_click_update)
# window.bind('<Button-3>', right_click)

# Run the sript
counter = 1
window.after(0, window_update)
window.mainloop()

# Debug info
if __name__ == "__main__":
    print("Counter is:", counter)
    print("Draw points are:", draw_points)