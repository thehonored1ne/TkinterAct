import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Student Information Form")
root.geometry("300x400")

p1 = tk.PhotoImage(file='student.png')
root.iconphoto(False, p1)

v = tk.IntVar()

# Labels
tk.Label(root, text="First Name").place(x=10, y=10)
tk.Label(root, text="Middle Name").place(x=10, y=40)
tk.Label(root, text="Last Name").place(x=10, y=70)
tk.Label(root, text="Address").place(x=10, y=100)
tk.Label(root, text="Course").place(x=10, y=130)
tk.Label(root, text="Year").place(x=10, y=160)

# Entry fields
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e4 = tk.Entry(root)

e1.place(x=100, y=10, width=180)
e2.place(x=100, y=40, width=180)
e3.place(x=100, y=70, width=180)
e4.place(x=100, y=100, width=180)

# Combobox
options = ["BSBA", "BSIT", "BSSE"]
combo = ttk.Combobox(root, values=options, state='readonly') # state set to readonly in init
combo.place(x=100, y=130, width=180)
combo.set("Select your course.")

# Radio Buttons
r1 = tk.Radiobutton(root, text="1st Year", variable=v, value=1)
r2 = tk.Radiobutton(root, text="2nd Year", variable=v, value=2)
r3 = tk.Radiobutton(root, text="3rd Year", variable=v, value=3)
r4 = tk.Radiobutton(root, text="4th Year", variable=v, value=4)

r1.place(x=100, y=160)
r2.place(x=100, y=180)
r3.place(x=100, y=200)
r4.place(x=100, y=220)

# Buttons
button1 = tk.Button(root, text="Add")
button2 = tk.Button(root, text="Update")
button3 = tk.Button(root, text="Delete")
button4 = tk.Button(root, text="Search")

button1.place(x=10, y=270, width=65)
button2.place(x=80, y=270, width=65)
button3.place(x=150, y=270, width=65)
button4.place(x=220, y=270, width=65)

root.mainloop()