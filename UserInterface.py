from tkinter import *
from tkinter.ttk import Combobox
import pafy

def return_streams():
    null_values()
    null_message()
    url = get_text()
    try:
        v = pafy.new(url)
        video_streams = v.streams
        available_streams = []
        for stream in video_streams:
            available_streams.append(stream)
        set_values(available_streams)
        show_dl_button()
    except:
        del_dl_button()
        label_message.configure(text="Введите ссылку с Youtube")

def get_text():
    text = txt.get()
    return text

def set_values(val):
    combo['values'] = val
    combo.current(0)

def null_values():
    combo['values'] = ['']
    combo.current(0)

def null_message():
    label_message.configure(text='')

def show_dl_button():
    if not button_download.winfo_viewable():
        button_download.configure(text="Скачать")
        button_download.grid(column=2, row=1)

def del_dl_button():
    if combo.get() == "":
        button_download.grid_remove()

def download_video():
    url = get_text()
    try:
        v = pafy.new(url)
        video_streams = v.streams
        quality = combo.get()
        for number, stream in enumerate(video_streams):
            if quality == str(stream):
                video_streams[number].download()
    except:
        del_dl_button()
        label_message.configure(text="Введите ссылку с Youtube")


window = Tk()
window.title("Загрузчик видео с YouTube")
window.geometry('600x200')
lbl = Label(window, text="Введите URL-адрес страницы:")
lbl.grid(column=0, row=0)

txt = Entry(window, width='50')
txt.grid(column=1, row=0)
txt.clipboard_get()

btn_next = Button(window, text="Далее", command=return_streams)
btn_next.grid(column=2, row=0)

button_download = Button(window, text='', command=download_video)

combo = Combobox(window)
combo.grid(column=0, row=3)

label_message = Label(window, text='')
label_message.grid(column=0, row=4)


window.mainloop()