import sqlite3
import polly_aws

con = sqlite3.connect('database/database.db', check_same_thread=False)
cur = con.cursor()

frases = {
    'human': [
        'quando eu falar ',
        'se eu falar ',
        'se eu disser ',
        'quando eu disser ',
        'quando falar ',
        'se falarem ',
        'caso falem ',
        'quando eu perguntar ',
        'quando eu fazer a pergunta '
    ],
    'robot': [
        ' você diz ',
        ' você fala ',
        ' tu diz ',
        ' tu fala ',
        ' você responde ',
        ' tu responde '
    ]
}

def to_learn(me, jarvis):
    try:
        cur.execute("INSERT INTO learning VALUES ('{}', '{}')".format(
            me.lower(), jarvis.lower()
        ))
        con.commit()
        polly_aws.text_to_audio("Está salvo na memória senhor.")
    except Exception as e:
        polly_aws.text_to_audio("Desculpe senhor não consegui salvar na memória.")

def search_in_memory(frase):
    try:
        table = cur.execute("SELECT * FROM learning WHERE listen = '{}'".format(
            frase.lower()
        ))
        for row in table:
            polly_aws.text_to_audio(row[1])

    except Exception as e:
        print(e)

def learn_now(text):
    for item in frases['human']:
        if item in text:
            f = text.replace(item, "")
            for rob in frases['robot']:
                if rob in text:
                    s = f.split(rob)
            to_learn(s[0], s[1])
            return True
