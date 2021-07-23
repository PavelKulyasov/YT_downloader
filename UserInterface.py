from tkinter import *
from tkinter.ttk import Combobox
import pafy
import sys


def get_text_url():
    # lbl1.configure(text=txt.get())
    return lbl1.configure(text=txt.get())

def get_video_streams(url):
    v = pafy.new(url)
    video_streams = v.streams
    available_streams = []
    for stream in video_streams:
        available_streams.append(stream)
        # print(f"{count}: {stream}")

    return available_streams

window = Tk()
window.title("Загрузчик видео с YouTube")
window.geometry('600x200')
lbl = Label(window, text="Введите URL-адрес страницы:")
lbl.grid(column=0, row=0)

lbl1 = Label(window, text='')
lbl1.grid(column=0, row=1)

txt = Entry(window, width='50')
txt.grid(column=1, row=0)

btn = Button(window, text="Далее", command=get_text_url)
btn.grid(column=2, row=0)

combo = Combobox(window)
combo['values'] = get_video_streams(btn)

window.mainloop()