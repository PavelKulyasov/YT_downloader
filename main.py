import pafy

# url = "https://www.youtube.com/watch?v=i_wJbCTCItE&t=2s"

# v = pafy.new(url)

# print(v)
# streams = v.streams
# for item in streams:
#     print(item)

# audio_streams = v.audiostreams
# for item in audio_streams:
#     print(item)

# all_streams = v.allstreams
# for item in all_streams:
#     print(item.quality)

url = input("Введите URL видео: ")

try:
    v = pafy.new(url)
    print(v.title)

    print("Выберите желаемое качество видеоролика передав цифру. Пример: 1")

    available_streams = {}
    count = 1

    video_streams = v.streams
    for stream in video_streams:
        available_streams[count] = stream
        print(f"{count}: {stream}")
        count += 1

    stream_count = int(input("Введите номер: "))
    d =video_streams[stream_count - 1].download()
    print("Скачивание завершено успешно!")
except:
    print("Не верный URL. Попробуйте снова.")