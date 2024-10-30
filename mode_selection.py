import tkinter 

button_held = False
status = 0
Mode = ["Environment Check", "Document Read", "Obstacle Detection"]

def onRelease(self):
    global button_held
    button_held = False
    if (status == 1):
        #end memo, save
        print("Finished taking voice")
    #print("Released")
    statusLabel.config(text=Mode[status-1])

def single_click(self):
    global button_held
    global status
    status = 1
    button_held = True
    print("Taking voice...")
    #initiate voice memo 
    #print("single")
    statusLabel.config(text=Mode[status-1])

def double_click(self):
    print("Document Read Mode")
    global status
    status = 2
    statusLabel.config(text=Mode[status-1])

def triple_click(self):
    print("Obstacle Detection Mode")
    global status
    status = 3
    statusLabel.config(text=Mode[status-1])

def status_check():
    print(f"Status: {status}")

window = tkinter.Tk("Sight Guide App")
button = tkinter.Button(
    text="Mode switch input",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

statusLabel = tkinter.Label(
    text=f"Status: {status}",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

button.pack()
statusLabel.pack()
button.bind("<ButtonRelease-1>", onRelease)  # Left mouse button release
button.bind("<Button-1>", single_click)
button.bind("<Double-Button-1>", double_click)
button.bind("<Triple-Button-1>", triple_click)


window.mainloop()