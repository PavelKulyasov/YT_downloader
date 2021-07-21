from tkinter import *

window = Tk()
window.title("Загрузчик видео с YouTube")
window.geometry('600x200')
lbl = Label(window, text="Введите URL-адрес страницы:")
lbl.grid(column=0, row=0)
txt = Entry(window, width='50')
txt.grid(column=1, row=0)
window.mainloop()