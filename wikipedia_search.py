import wikipedia
import polly_aws

wikipedia.set_lang('pt')

frases = [
    'quem é ',
    'quem foi ',
    'quem foram ',
    'o que é ',
    'o que são ',
    'o que foram ',
    'quais são ',
    'quais foram ',
    'qual é ',
    'qual foi ',
    'sobre '
]

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
            if item in frase:
                get_wiki(frase.split(item))
                return True