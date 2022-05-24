import speech
import wikipedia_search
import polly_aws
import movies
import learning
import date_now
import temperatura
import musics
import calculator
import send_sms
import battery
import bluetooth_connection


def init():
    while True:
        #battery.battery()
        text = (speech.ouvir_microfone()).lower()
        if "jarvis " in text:
            text = text.replace("jarvis ", "")
            neural(text)
            text = ""
        if " jarvis" in text:
            text = text.replace(" jarvis", "")
            neural(text)
            text = ""


def neural(text):
    waiting = False
    if text:
        try:
            print(text)
            waiting = True
            send_sms.send(text)
            learning.learn_now(text)
            learning.search_in_memory(text)
            bluetooth_connection.run(text)
            calculator.calculate_now(text)
            battery.get_battery(text)
            date_now.dates(text)
            temperatura.weather(text)
            movies.download_movie(text)
            musics.do_music(text)
            wikipedia_search.wiki_search(text)
        except Exception as e:
            print(e)
            text = ''
            polly_aws.text_to_audio("Desculpe, não entendi, senhor.")


init()
