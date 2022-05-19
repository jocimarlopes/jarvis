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


def init():
    while True:
        #battery.battery()
        text = (speech.ouvir_microfone()).lower()
        if "jarvis " in text:
            text = text.replace("jarvis ", "")
            try:
                neural(text)
                text = ""
            except:
                text = ''
                polly_aws.text_to_audio("Desculpe, não entendi, senhor.")


def neural(text):
    waiting = False
    if text:
        waiting = True
        send_sms.send(text)
        learning.learn_now(text)
        learning.search_in_memory(text)
        calculator.calculate_now(text)
        battery.get_battery(text)
        date_now.dates(text)
        temperatura.weather(text)
        movies.download_movie(text)
        musics.pause_music(text)
        musics.play_music(text)
        wikipedia_search.wiki_search(text)
    else:
        if waiting:
            polly_aws.text_to_audio(
                "Por favor senhor, quando me chamar já diga o que precisa.")
            waiting = False


init()
