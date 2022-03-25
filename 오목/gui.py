import sys
from tkinter import *
import tkinter

root = Tk()
root.title("오목 GUI")
root.geometry("400x640")


back_btn = Button(root, font = 20, text='무르기')
back_btn.pack(anchor = W)

root.mainloop()

