from neural_links import speech
from neural_links import wikipedia_search
from neural_links import polly_aws
from neural_links import movies
from neural_links import learning
from neural_links import date_now
from neural_links import temperatura
from neural_links import musics
from neural_links import calculator
from neural_links import send_sms
from neural_links import battery
from neural_links import bluetooth_connection


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

if __name__ == "__main__":
    init()
