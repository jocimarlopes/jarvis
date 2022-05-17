import requests
import json
import polly_aws


url = "https://api.hgbrasil.com/weather?key=e7cf1324&city_name=Osorio,RS"

frases = [
    'como está o tempo',
    'qual a temperatura',
    'quantos graus',
    'como tá o tempo',
    'e o tempo'
]

def get_weather():
    response = json.loads((requests.get(url)).text)

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
        retorno = "Eu estou congelando! Hoje faz {} graus em {}, não saia nesse frio hein, senhor.".format(temp, city)
    return polly_aws.text_to_audio(retorno)


def weather(text):
    for item in frases:
        if item in text:
            get_weather()
            return True