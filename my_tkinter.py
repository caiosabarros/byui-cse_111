import tkinter as tk
from math import *

def evaluate(event):
    res.configure(text = "Area: " + str(eval(entry.get())))

w = tk.Tk()
tk.Label(w, text="Enter the width*height of the rectangle you want ot calculate the area of and press enter:").pack()
entry = tk.Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()
