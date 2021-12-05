import os
import random
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Скажите вашу команду:  ")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='ru-Ru')
        print(f'Вы сказали: {query.lower()}')
        return query
    except sr.UnknownValueError:
        return 'error'
    except sr.RequestError:
        return 'error'

    # return input("Скажите вашу команду:  ")


def say(text):
    voice = gTTS(text, lang="ru")
    file_name = "audio_" + str(time.time()) + str(random.randint(0, 100000)) + ".mp3"
    voice.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
    print("Ассистент: " + text)


def handle_message(message):
    message = message.lower()
    if "привет" in message:
        say("Приветствую вас сэр!")
        say("Что я могу для вас сделать?")
    elif "как дела" in message:
        say("Хорошо")
        say("Что я могу для вас сделать?")
    elif "закажи мне еду" in message:
        say("Пиццу или роллы?")
    elif "закажи мне пиццу" in message:
        say("Заказ выполнен, сэр!")
        say("Хотите что-то еще, сэр?")
    elif "закажи мне роллы" in message:
        say("Заказ выполнен, сэр!")
    elif "спасибо" in message:
        say("Рада была помочь, сэр!")
    elif "пока" in message:
        finish()
    else:
        say("Простите сэр, я вас не понимаю!")


def finish():
    say("Всего доброго сэр!")
    exit()


if __name__ == '__main__':

    while True:
        command = listen_command()
        handle_message(command)
