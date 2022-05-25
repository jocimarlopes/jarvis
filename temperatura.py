import requests
import json
import polly_aws
import base64

cidade = 'Osorio,RS'
url = (base64.b64decode('aHR0cHM6Ly9hcGkuaGdicmFzaWwuY29tL3dlYXRoZXI/a2V5PWU3Y2YxMzI0JmNpdHlfbmFtZT0=')).decode('utf-8')

frases = [
    'como está o tempo',
    'como tá o tempo',
    'qual a temperatura',
    'quantos graus',
    'e o tempo',
    'tá frio',
    'ta frio',
    'tá calor',
    'ta calor'
]

def get_weather():
    response = json.loads((requests.get('{}{}'.format(url, cidade))).text)

    temp = response['results']['temp']
    city = response['results']['city_name']
    retorno = ""
    print(temp)

    if temp > 29:
        retorno = "Tá bem quente hoje! Estão fazendo {} graus em {}, tô sentindo o calor daqui, saia um pouco, senhor..".format(temp, city)
    if temp > 26 and temp <= 29:
        retorno = "Hoje fazem {} graus em {}, acho que está começando a esquentar, senhor.".format(temp, city)
    if temp <= 26 and temp > 21:
        retorno = "Clima agradável! Hoje faz {} graus em {}, aproveite, senhor.".format(temp, city)
    if temp <= 21 and temp > 15:
        retorno = "Tá ficando frio, senhor! Hoje faz {} graus em {}".format(temp, city)
    if temp <= 15 and temp > 9:
        retorno = "Tá frio hein, hoje faz {} graus em {}, prepare os casacos, senhor.".format(temp, city)
    if temp <= 9:
        retorno = "Eu estou congelando! Hoje fazem {} graus em {}, não saia nesse frio hein, senhor.".format(temp, city)
    return polly_aws.text_to_audio(retorno)


def weather(text):
    for item in frases:
        if item in text:
            get_weather()
            return True