import tkinter as tk
from time import strftime
import random as rand
root=tk.Tk()
root.title("CLOCK")
bool=tk.BooleanVar(value=True)
def toggle(event):
    bool.set(not bool.get())
def update():
    colors=["red","orange","yellow","green","cyan","magenta",]
    newc=rand.choice(colors)
    newcol=rand.choice([c for c in colors if c!=newc])
    label.pack(anchor="center")
    if bool.get():
        root.config(background=newcol)
        label.config(background=newcol,text=strftime("%H:%M:%S %p"),foreground=newc)
    else:
        label.config(background=newcol,text=strftime("%d/%m/%Y"),foreground=newc)
    label.after(1000, update)
label=tk.Label(root,font=("Courier New",18,"bold"),background='black',foreground='white')
label.pack(anchor="center")
update()
root.bind("<space>",toggle)
root.bind("<Home>",toggle)
root.bind("<Return>", toggle)
root.mainloop()
