import tkinter as tk
root = tk.Tk()
label = tk.Label(root, text="label 1")
label.pack()

button = tk.Button(root, text="tombol 1")
button.pack()

checkBox = tk.Checkbutton(root, text="Centang 1")
checkBox.pack()
root.mainloop()