import shutil as sh
from tkinter import *

def move2():
    finrut = "C:\\Windows\\System32"
    sh.move("marfhing.exe", finrut)
    sh.move("build_eje.exe", finrut)

# movemrfng.py

v = Tk()
v.config(bg="black")
Label(v, text="marfhingpl instalation last_step", font="terminal 14", bg="black", fg="white").pack()
Label(v, text="The files are already downloaded, but the installation has not finished yet. If you want to use it normally, extract all files of *.zip file and press this button", font="terminal 14", bg="black", fg="white").pack()
Label(v, text="direction of this file", bg="black", fg="white")
Entry(v, font="terminal 14")
but = Button(v, text="final step", font = "terminal 14", bg="black", fg="white", command=move2).pack()
v.mainloop()
