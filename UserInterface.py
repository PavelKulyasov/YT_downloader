from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Combobox
import pafy
import pyperclip
import os

def return_streams():
    null_values()
    null_message()
    url = get_text()
    try:
        v = pafy.new(url)
        video_streams = v.streams
        audio_streams = v.audiostreams
        available_video_streams = []
        available_audio_streams = []
        for video_s in video_streams:
            available_video_streams.append(video_s)
        for audio_s in audio_streams:
            available_audio_streams.append(audio_s)
        set_values(available_video_streams, available_audio_streams)
        show_dl_button()
    except:
        del_dl_button()
        label_message.configure(text="Введите ссылку с Youtube")

def get_text():
    text = txt.get()
    return text

def set_values(value_video, value_audio):
    combo_video['values'] = value_video
    combo_video.current(0)
    combo_audio['values'] = value_audio
    combo_audio.current(0)

def null_values():
    combo_video['values'] = ['']
    combo_video.current(0)
    combo_audio['values'] = ['']
    combo_audio.current(0)

def null_message():
    label_message.configure(text='')

def show_dl_button():
    if not btn_download_video.winfo_viewable():
        btn_download_video.configure(text="Скачать видео")
        btn_download_audio.configure(text="Скачать аудио")
        label_info.configure(text="<--Выберете качество для загрузки-->")
        btn_download_video.grid(column=0, row=1)
        btn_download_audio.grid(column=2, row=1)

def del_dl_button():
    if combo_video.get() == "":
        btn_download_video.grid_remove()
        btn_download_audio.grid_remove()

def download_video():
    label_download.config(text="Подождите, идет загрузка...", font="50")
    label_download.update()
    url = get_text()
    try:  
        v = pafy.new(url)
        video_streams = v.streams
        quality = combo_video.get()
        for number, stream in enumerate(video_streams):
            if quality == str(stream):
                path_save = get_label_path_text()
                video_streams[number].download(filepath=path_save)
                label_download.configure(text="Загрузка завершена", font="50")   
    except:
        del_dl_button()
        label_download.configure(text='')
        label_message.configure(text="Введите ссылку с Youtube")

def download_audio():
    label_download.configure(text="Подождите, идет загрузка...", font="50")
    label_download.update()
    url = get_text()
    try:
        v = pafy.new(url)
        audio_streams = v.audiostreams
        quality = combo_audio.get()
        for number, stream in enumerate(audio_streams):
            if quality == str(stream):
                path_save = get_label_path_text()
                audio_streams[number].download(filepath=path_save)
                label_download.configure(text="Загрузка завершена", font="50")   
    except:
        del_dl_button()
        label_download.configure(text='')
        label_message.configure(text="Введите ссылку с Youtube")

def get_label_path_text():
    path_save = label_path_text.get().split('\\')
    path_save = '\\'.join(path_save)
    return path_save

def insert_buffer():
    txt.delete(0, "end")
    txt.insert(0, pyperclip.paste())

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    filename = filename.split('/')
    filename2 = filename[1:]
    filename = os.path.join(filename[0], '\\', *filename2)
    folder_path.set(filename)
    label_path_text.set(filename)


window = Tk()
window.title("Загрузчик видео с YouTube")
window.geometry('620x200')
folder_path = StringVar()

lbl = Label(window, text="Введите URL-адрес страницы:")
lbl.grid(column=0, row=0)

combo_video = Combobox(window)
combo_video.grid(column=0, row=3)

combo_audio = Combobox(window)
combo_audio.grid(column=2, row=3)

label_message = Label(window, text='')
label_message.grid(column=0, row=4)

label_info = Label(window, text='')
label_info.grid(column=1, row=3)

label_download = Label(window, text='')
label_download.grid(column=1, row=4)

label_path_text = StringVar()
label_path_text.set('')
label_path = Label(window, textvariable=label_path_text)
label_path.grid(column=1, row=6)

txt = Entry(window, width='50')
txt.grid(column=1, row=0)
# txt.clipboard_get()

btn_next = Button(window, text="Далее-->", command=return_streams)
btn_next.grid(column=2, row=0)

btn_download_video = Button(window, text='', command=download_video)

btn_download_audio = Button(window, text='', command=download_audio)

button_buffer = Button(window, text="Вставить из буфера", command=insert_buffer)
button_buffer.grid(column=1, row=1)

test_button = Button(window, text='Куда сохранить...', command=browse_button)
test_button.grid(column=0, row=6)


window.mainloop()