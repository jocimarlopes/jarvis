import speech_recognition as sr
from playsound import playsound


def ouvir_microfone():
    try:
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            print("Fale agora: ")
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio, language='pt-BR')
            return frase
    except sr.UnknownValueError:
        return "Desculpe, não entendi o que disse, senhor."
