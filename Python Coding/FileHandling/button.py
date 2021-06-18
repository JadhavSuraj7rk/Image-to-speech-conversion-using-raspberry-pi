import tkinter as tk
from imagetospeech import image_to_speech


def onclick():
    print("Button clicked")


root = tk.Tk()
root.title("GUI Button")

btn1 = tk.Button(root, text="Button", command=onclick)

btn1.pack()
btn1.config(command=image_to_speech)

root.mainloop()
