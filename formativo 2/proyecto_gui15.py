from tkinter import *
from tkinter import Menu
window = Tk()
window.title("Welcome to LikeGeeks app")
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
new_item.add_command(label='Edit')
new_item.add_command(label='unas rank o que')
window.config(menu=menu)
window.mainloop()