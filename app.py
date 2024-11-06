import tkinter as tk
from tkinter import filedialog

instructions_text = """Device Connected\n\n\n
Use the buttons on the device to switch between modes
1 Click: General Visual Aid
2 Clicks: Document Reading
3 Clicks: Obstacle and Crosswalk Detection"""

window = tk.Tk("Sight Guide App")
window.geometry("360x640")

top_label = tk.Label(window, text="Sight Guide", font=("Arial", 24, "bold"))
top_label.pack(side=tk.TOP, pady=10)

middle_text = tk.Label(window, text=instructions_text, font=("Arial", 18), justify="center",  wraplength=320)
middle_text.pack(pady=40)


button_frame =tk.Frame(window)
button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

# Add two buttons in the frame
audio_button = tk.Button(button_frame, text="Upload Audio File", width=10, command=filedialog.askopenfilename)
audio_button.pack(side=tk.LEFT, expand=True, padx=5)
    
image_button = tk.Button(button_frame, text="Upload Image File", width=10, command=filedialog.askopenfilename)
image_button.pack(side=tk.RIGHT, expand=True, padx=5)

# Run the main event loop
window.mainloop()
