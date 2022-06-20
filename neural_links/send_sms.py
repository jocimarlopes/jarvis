import requests
from neural_links import polly_aws
import json
import base64

url = (base64.b64decode('aHR0cHM6Ly9hcGkuc21zZGV2LmNvbS5ici92MS9zZW5kPw==')).decode('utf-8')
key = '4Y0GQO9S0ISP3SDYG7IPAR2ZFHTD2HHSRAV4XG83VP4OI8ICCVAVI9WKGTUT6RLRSNU09L1BXNDTZKCSC39KQEC74PY37UVNDZPRUJN9IOOIT9CSX4EW5YZWDT4HFXZA'

frases = [
    'envia o sms ',
    'envie a mensagem ',
    'envia a mensagem '
    'envia uma mensagem ',
    'envia um sms ',
    'envie uma mensagem ',
    'envie um sms ',
    'envie o sms ',
    'envia mensagem ',
    'envia sms',
    'envie sms',
    'envie mensagem'
]
send_to = [
    ' para o ',
    ' pro ',
    ' para a ',
    ' pra ',
    ' para '
]
numbers = {
    'NAME': 'DDD+NUMBER',
    'NAME': 'DDD+NUMBER',
    'NAME': 'DDD+NUMBER',
    'NAME': 'DDD+NUMBER'
}


def send_request(num, msg):
    try:
        response = requests.get("{}key={}&type=9&number={}&msg={}".format(url, key, num, msg))
        res = json.dumps(response.text)
        print(res)
        if 'OK' in res['situacao']:
            polly_aws.text_to_audio("Pronto senhor, sms enviado.")
            return
        else:
            polly_aws.text_to_audio(
                "Desculpe, não consegui enviar o sms, senhor.")
            return
    except Exception as e:
        print(e)
        polly_aws.text_to_audio(
            "Desculpe! Não consegui enviar o sms, senhor.")
        return True


def send(text):
    for item in frases:
        if item in text:
            text = text.replace(item, '')
            t = ''
            for to in send_to:
                if to in text:
                    t = text.split(to)
            for item in numbers:
                if t[1] in item:
                    t[1] = numbers[item]
            send_request(t[1], t[0])
