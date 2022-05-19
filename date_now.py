import datetime
import polly_aws

months = [
    {"number": '01', "name": "Janeiro"},
    {"number": '02', "name": "Fevereiro"},
    {"number": '03', "name": "Março"},
    {"number": '04', "name": "Abril"},
    {"number": '05', "name": "Maio"},
    {"number": '06', "name": "Junho"},
    {"number": '07', "name": "Julho"},
    {"number": '08', "name": "Agosto"},
    {"number": '09', "name": "Setembro"},
    {"number": '10', "name": "Outubro"},
    {"number": '11', "name": "Novembro"},
    {"number": '12', "name": "Dezembro"},
]
frases = {
    'hour': [
        'que horas são',
        'que hora é',
        'horas por favor',
    ],
    'date': [
        'que dia é',
        'qual a data',
        'qual dia é'
    ]
}

def get_hour():
    x = str(datetime.datetime.now())
    y = x.split(' ')
    d = y[1].split('.')
    hora = d[0].split(':')

    if '00' in hora[0]:
        print(hora)
        return polly_aws.text_to_audio(
            "Agora são meia noite e {} minutos, senhor.".format(int(hora[1])))
        
    if '01' in hora[0]:
        return polly_aws.text_to_audio(
            "Agora são {} hora e {} minutos, senhor.".format(int(hora[0]), int(hora[1])))
    else:
        return polly_aws.text_to_audio(
            "Agora são {} horas e {} minutos, senhor.".format(int(hora[0]), int(hora[1])))


def get_date():
    x = str(datetime.datetime.now())
    y = x.split(' ')
    d = y[0].split('-')

    for month in months:
        if d[1] == month['number']:
            d[1] = month['name']
    polly_aws.text_to_audio(
        "Hoje é dia {} de {} de {}".format(int(d[2]), d[1], int(d[0])))


def dates(text):
    for item in frases['hour']:
        if item in text:
            get_hour()
            return True
    for item in frases['date']:
        if item in text:
            get_date()
            return True
