#!/usr/bin/env python

import tkinter as tk

# --- functions ---

def open_subwindow():
    subwindow = tk.Toplevel()

    btn = tk.Button(subwindow, text="Close subwindow", command=subwindow.destroy)
    btn.pack()
    
# --- main ---    

root = tk.Tk()
root.geometry("300x300")

btn = tk.Button(root, text="Open subwindow", command=open_subwindow)
btn.pack()

root.mainloop()
