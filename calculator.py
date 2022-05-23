import requests
import polly_aws

frases = [
    'quanto é ',
    'quanto são ',
    'quantos são ',
    'quantos é ',
    'quanto fica '
]
numerics = [
    {'c': ' + ', 'a': '%2B'},
    {'c': ' - ', 'a': '%2D'},
    {'c': ' x ', 'a': '*'},
    {'c': ' / ', 'a': '%2F'},
]


def get_response(n1, a, n2):
    try:
        response = requests.get(
            "https://api.mathjs.org/v4/?expr={}{}{}".format(n1, a, n2))
        polly_aws.text_to_audio("A resposta é {}".format(response.text))
        return True
    except Exception as e:
        polly_aws.text_to_audio(
            "Desculpe! Não consegui calcular, não entendi, senhor.")
        return True


def calculate_now(text):
    a = ''
    for item in frases:
        if item in text:
            text = text.replace(item, "")
    for item in numerics:
        if item['c'] in text:
            a = item['a']
            text = text.split(item['c'])
    if isNumber(text[0]) and isNumber(text[1]):
        get_response(text[0], a, text[1])


def isNumber(value):
    try:
        float(value)
    except ValueError:
        return False
    return True
