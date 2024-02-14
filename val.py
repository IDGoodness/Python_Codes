import tkinter as tk
import random



def impress_crush():
    pickup_lines = [
        "Do you have a map? I keep getting lost in your eyes.",
        "Is your name Google? Because you have everything I've been searching for.",
        "Are you a magician? Because whenever I look at you, everyone else dissappears!",
        "Excuse me, but I think you dropped something: my jaw.",
        "Is your Dad a baker? Because you are a cutie pie.",
        "Do you believe in love at first sight, or should I walk by again?",
        "If you were a vegetable, you'd be a cute-cumber.",
        "Do you have Band-Aid? I just scrapped my knee falling for you.",
        "Are you a camera? Because every time I look at you, I samile.",
        "Is your name Wi-Fi? Because I'm really feeling a connection to you.",
        "I must be a snowflake, because I've fallen for you.",
        "You make the world a brighter place just by being in it.",
        "My heart is a paperweight and yours is the glue that holds it together.",
    ]
    
    pickup_line =  random.choice(pickup_lines)
    label.config(text=pickup_line)
    
# Create the main window
window = tk.Tk()
window.title("Impress Your Crush")
window.geometry("400x300")

# Create a label to display the pickup lines
label = tk.Label(window, text="Click the button for a romantic pickup line!")
label.pack(pady=20)

# Create a button
button = tk.Button(window, text="Click Me", command=impress_crush)
button.pack()

# Start the main event loop
window.mainloop()


 