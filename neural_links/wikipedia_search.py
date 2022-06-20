import wikipedia
from neural_links import polly_aws

wikipedia.set_lang('pt')

frases = {
    0:'quem é ',
    1:'quem foi ',
    2:'quem foram ',
    3:'o que é ',
    4:'o que são ',
    5:'o que foram ',
    6:'quais são ',
    7:'quais foram ',
    8:'qual é ',
    9:'qual foi ',
    10:'sobre '
}

def get_wiki(data):
    try:
        response = wikipedia.summary(data, sentences=2)
        print(response)
        return polly_aws.text_to_audio(response)
    except Exception as e:
        print(e)

def wiki_search(frase):
    if "pesquise " in frase:
        frase = frase.replace("pesquise ", "")
        for item in frases:
            if frases.get(item) in frase:
                get_wiki(frase.split(item))
                return True