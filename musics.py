import os
import polly_aws

frases_play = [
    'play',
    'volte a tocar',
    'volta a tocar',
    'toca a música ',
    'toque a música ',
    'toque música ',
    'toca música ',
    'tocar música ',
    'tocar a música '
]
frases_pause = [
    'pause',
    'pausar música',
    'pause a música',
    'parar música',
    'parar música',
    'pare a música'
]

def play_music(frase):
    frase = frase.replace("'", "")
    for item in frases_play:
        if item in frase:
            os.popen("spotify play " + frase.replace(item, ""))
            polly_aws.text_to_audio("Pronto senhor, está tocando...")
            return True
    return False

def pause_music(frase):
    for item in frases_pause:
        if item in frase:
            try:
                os.popen("spotify pause")
                polly_aws.text_to_audio("Pronto senhor, pausei a música.")
                return True
            except:
                polly_aws.text_to_audio(
                    "Desculpe senhor, acho que não tem música tocando.")
    return False

def do_music(frase):
    play_music(frase)
    pause_music(frase)