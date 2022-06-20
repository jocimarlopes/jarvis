import requests
import json
from neural_links import polly_aws
import base64

cidade = 'Osorio,RS'
url = (base64.b64decode('aHR0cHM6Ly9hcGkuaGdicmFzaWwuY29tL3dlYXRoZXI/a2V5PWU3Y2YxMzI0JmNpdHlfbmFtZT0=')).decode('utf-8')

frases = {
    0: 'como está o tempo',
    1: 'como tá o tempo',
    2: 'qual a temperatura',
    3: 'quantos graus',
    4: 'e o tempo',
    5: 'tá frio',
    6: 'ta frio',
    7: 'tá calor',
    8: 'ta calor'
}

def get_weather():
    response = json.loads((requests.get('{}{}'.format(url, cidade))).text)

    temp = response['results']['temp']
    city = response['results']['city_name']
    retorno = ""
    respostas = {
        31: "Tá bem quente hoje estão fazendo {} graus em {}, tô sentindo o calor daqui senhor".format(temp, city),
        26: "Hoje fazem {} graus em {}, acho que está começando a esquentar, senhor.".format(temp, city),
        21: "Clima agradável, Hoje fazem {} graus em {}, aproveite, senhor.".format(temp, city),
        16: "Tá ficando frio, hoje fazem {} graus em {}".format(temp, city),
        11: "Tá frio hein hoje fazem {} graus em {}, prepare os casacos senhor.".format(temp, city),
        6: "Eu estou congelando! Hoje fazem {} graus em {}, não saia nesse frio hein, senhor.".format(temp, city)
    }

    for item in respostas:
        if temp <= item and temp >= (item - 5):
            retorno = respostas[item]
    return polly_aws.text_to_audio(retorno)


def weather(text):
    for item in frases:
        if frases.get(item) in text:
            get_weather()
            return True