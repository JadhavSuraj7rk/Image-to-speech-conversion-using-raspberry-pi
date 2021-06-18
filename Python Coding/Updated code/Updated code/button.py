import tkinter as tk


def onclick():
    print("Button clicked")


root = tk.Tk()
root.title("GUI Button")

btn1 = tk.Button(root, text="Button 1", command=onclick)

btn1.pack()
# btn1.config(command=)

root.mainloop()
