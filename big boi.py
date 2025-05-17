import tkinter as tk


root = tk.Tk()
root.title("i am adopted")
root.geometry("800x800")


label = tk.Label(root, text="your a big fat furry", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()

