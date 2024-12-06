import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import requests

url = "http://127.0.0.1:8080/general-visual-aid"

def playAudio():
    mixer.init()
    mixer.music.load("speech.mp3")
    mixer.music.play()


def uploadImage():
    filename = filedialog.askopenfilename()
    with open(filename, 'rb') as img:
        files = {'image': img}
        response = requests.post(url, files=files)
        print(response.content)



instructions_text = """Device Connected\n\n\n
Use the buttons on the device to switch between modes
1 Click: General Visual Aid
2 Clicks: Document Reading
3 Clicks: Obstacle and Crosswalk Detection"""

window = tk.Tk("Sight Guide App")
window.geometry("640x640")

top_label = tk.Label(window, text="Sight Guide", font=("Arial", 24, "bold"))
top_label.pack(side=tk.TOP, pady=10)

middle_text = tk.Label(window, text=instructions_text, font=("Arial", 18), justify="center", wraplength=320)
middle_text.pack(pady=40)

button_frame = tk.Frame(window)
button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

audio_button = tk.Button(button_frame, text="Upload Audio File", width=10, command=filedialog.askopenfilename)
audio_button.pack(side=tk.LEFT, expand=True, padx=5)

image_button = tk.Button(button_frame, text="Upload Image File", width=10, command=uploadImage)
image_button.pack(side=tk.RIGHT, expand=True, padx=5)



window.mainloop()
