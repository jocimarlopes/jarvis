import psutil
from neural_links import polly_aws

frases_battery = [
    'qual o nível da bateria',
    'nível da bateria',
    'como está a bateria',
    'como tá a bateria',
    'bateria',
    'você tem carga',
    'você tem bateria',
    'tem bateria',
    'quantos tem de bateria',
    'quanto tem de bateria',
    'como é que ta a bateria'
]

def nivel_battery():
    battery = psutil.sensors_battery()
    percent = str(battery.percent)
    retorno = "A bateria está em {} porcento senhor.".format(percent)
    return polly_aws.text_to_audio(retorno)

def get_battery(text):
    for item in frases_battery:
        if text in item:
            nivel_battery()

def battery():
    battery = psutil.sensors_battery()
    percent = str(battery.percent)
    if int(percent) < 15:
        return polly_aws.text_to_audio('Senhor.. Está na hora de carregar o notebook, estamos com {} porcento'.format(inteiro))
