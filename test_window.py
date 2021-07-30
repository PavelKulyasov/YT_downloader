from tkinter import *
from tkinter.ttk import Combobox
import pafy

class GetVideo():
    # STREAMS = pafy.new()

    def __init__(self, text_url):
        self.STREAMS = pafy.new(text_url)

    def get_text(self):
        return self.text_url.get()

    def get_video_streams(self):
        video_streams = self.STREAMS.streams
        return video_streams    

    def download_video(self):
        self.STREAMS.download()

# url = "https://www.youtube.com/watch?v=dqUMxAT13kw"
# v = pafy.new("https://www.youtube.com/watch?v=dqUMxAT13kw")

def return_streams(url):
    v = GetVideo(url).STREAMS
    video_streams = v.streams
    available_streams = []
    for stream in video_streams:
        available_streams.append(stream)
        # print(f"{count}: {stream}")
    return available_streams, v

def get_text():
    text = txt.get()
    return text

def set_values(val):
    combo['values'] = val
    return combo['values']

# def get_url(text_field, label_field):
#     label_field.configure(text=set_values(return_streams(url)))
    # lbl1.configure(text=new_text)
    # if new_text != 0:
    #     return set_values(return_streams(new_text))
    # return lbl1.configure(text="Введите URL")
    
def clicked():
    # lbl1.configure(text=set_values(return_streams(url)))
    add_text.configure(text="<-- Выберите качество для загрузки")
    text=txt.get()
    return set_values(return_streams(text))

def get_entered_value(val1, val2):
    quality = combo.get()
    for stream in val1:
        if stream == quality:
            return val2.stream.download()

# def download_video():
#     stream = get_entered_value()
#     filename = v.download()
    
def get_combo():
    pass


window = Tk()
window.title("Загрузчик видео с YouTube")
window.geometry('600x200')
lbl = Label(window, text="Введите URL-адрес страницы:")
lbl.grid(column=0, row=0)

test_text = "https://www.youtube.com/watch?v=dqUMxAT13kw"

lbl1 = Label(window, text='test')
# lbl1.grid(column=0, row=2)

txt = Entry(window, width='50')
txt.grid(column=1, row=0)

combo = Combobox(window)
# combo.set(get_video_streams(get_text_url()))
# combo['values'] = ["поток1", "поток2"]
# potoki = ["поток1", "поток2"]
# combo.set(potoki)
combo.grid(column=0, row=3)

add_text = Label(window, text='')
add_text.grid(column=1, row=3)

btn_next = Button(window, text="Далее", command=set_values(return_streams(get_text())[0])) # command=set_values(return_streams(test_text))
# btn1 = Button(window, text="Показать качество", command=get_video_streams(url=lbl1.getvar))
btn_next.grid(column=2, row=0)

# btn_test = Button(window, text="download", command=get_entered_value(return_streams(test_text)))
# btn_test.grid(column=3, row=0)

lbl_get_quality = Label(window, text='...')
lbl_get_quality.grid(column=3, row=3)


# btn_quality = Button(window, text="download", command=download_video)
# btn_quality.grid(column=3, row=1)


window.mainloop()