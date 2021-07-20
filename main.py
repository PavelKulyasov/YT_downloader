import pafy
import sys
import os

# url = "https://www.youtube.com/watch?v=i_wJbCTCItE&t=2s"

# v = pafy.new(url)

# print(v)
# streams = v.streams
# for item in streams:
#     print(item)

# audio_streams = v.audiostreams
# for item in audio_streams:
#     print(item)
# внес изменения 21.07.21

def download(choice):
    try:
        v = pafy.new(url)
        # print(v.title)
        if choice == "1":
            streams = v.streams
        elif choice == "2":
            streams = v.audiostreams
        else:
            sys.exit()

        print("Выберите желаемое качество видеоролика передав цифру. Пример: 1") if choice == "1" else print("Выберите желаемое качество аудио передав цифру. Пример: 1")

        available_streams = {}
        count = 1
        for stream in streams:
            available_streams[count] = stream
            print(f"{count}: {stream}")
            count += 1

        stream_count = int(input("Введите номер: "))
        d = streams[stream_count - 1].download()
        print("Скачивание завершено успешно!")

        audio_extension = str(available_streams[stream_count])
        audio_extension = audio_extension.split("@")[0].split(":")[1]
        print(audio_extension)

        file_name = v.title
        music_file = f"{file_name}.{audio_extension}"
        base = os.path.splitext(music_file)[0]
        print(base)
        os.rename(music_file, base + ".mp3")
        print("Преобразование в mp3 успешно!")
    except:
        print("Не верный URL. Попробуйте снова.")

url = input("Введите URL видео: ")

print("Чтобы скачать видео введите: 1 | Чтобы скчать аудио введите: 2")
choice = input("Введите цифру: ")

download(choice)

# if choice == "1":
#     try:
#         v = pafy.new(url)
#         print(v.title)

#         print("Выберите желаемое качество видеоролика передав цифру. Пример: 1")

#         available_streams = {}
#         count = 1

#         video_streams = v.streams
#         for stream in video_streams:
#             available_streams[count] = stream
#             print(f"{count}: {stream}")
#             count += 1

#         stream_count = int(input("Введите номер: "))
#         d = video_streams[stream_count - 1].download()
#         print("Скачивание завершено успешно!")
#     except:
#         print("Не верный URL. Попробуйте снова.")
# elif choice == "2":
#     try:
#         v = pafy.new(url)
#         print(v.title)

#         print("Выберите желаемое качество аудио передав цифру. Пример: 1")

#         available_streams = {}
#         count = 1

#         video_streams = v.audiostreams
#         for stream in video_streams:
#             available_streams[count] = stream
#             print(f"{count}: {stream}")
#             count += 1

#         stream_count = int(input("Введите номер: "))
#         d = video_streams[stream_count - 1].download()
#         print("Скачивание завершено успешно!")
#     except:
#         print("Не верный URL. Попробуйте снова.")
# else:
#     print("What?")