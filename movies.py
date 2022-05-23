import requests
from bs4 import BeautifulSoup
import ssl
import polly_aws
import subprocess

ssl._create_default_https_context = ssl._create_unverified_context

PRINCIPAL = 'https://ondebaixa.com/index.php?s='

frases_movies = [
    "baixe o filme ",
    "baixe o filme do ",
    "baixe o filme da ",
    "baixa o filme do ",
    "baixa o filme da ",
    "baixar o filme ",
    "baixar filme ",
    "baixa filme ",
    "baixa o filme ",
    "baixe o último filme ",
    "baixar o último filme ",
    "baixar último filme ",
    "baixa o último filme ",
    "baixa último filme ",
    "baixe último filme ",
    "baixe o último filme do ",
    "baixa o ultimo filme do ",
    "baixe o último filme do ",
    "baixa o ultimo filme do ",
    "baixe último filme do ",
    "baixa último filme do "
]
frases_series = [
    "baixa a série ",
    "baixar a série ",
    "baixe a série ",
]


def run(args):
    print(args)
    i = 1
    go = PRINCIPAL + args

    page = requests.get(go)
    soup = BeautifulSoup(page.text, 'html.parser')

    list_movies = soup.find(id='capas_pequenas')

    filtered_list_movies = list_movies.find_all('a')
    new_list_links = []
    new_list = []

    try:
        for link in filtered_list_movies:
            if link.get('href') not in new_list_links:
                new_list_links.append(link.get('href'))
                new_list.append(link)
        for item in new_list:
            if i < 3:
                i = i + 1
                torrent_page = requests.get(item.get('href'))
                soup_torrent = BeautifulSoup(torrent_page.text, 'html.parser')

                list_movies_torrent = soup_torrent.find(id='lista_download')
                filtered_list_movies_torrent = list_movies_torrent.find_all(
                    'a')

                for obj in filtered_list_movies_torrent:
                    if 'magnet:' in obj.get('href'):
                        mgn = obj.get('href')
                        polly_aws.text_to_audio(
                            "Achei o filme senhor, vou pôr a baixar agora mesmo.")
                        subprocess.call(
                            'gnome-terminal -x bash -c "cd ~/Downloads/ && webtorrent download {}; exec bash"'.format(mgn), shell=True)
                        return True
    except Exception as e:
        print(e)
        polly_aws.text_to_audio(
            "Desculpe senhor, não consegui encontrar o filme que você pediu.")
        return True


def download_movie(text):
    for item in frases_movies:
        if item in text:
            print(item)
            polly_aws.text_to_audio(
                "Ok senhor, estou pesquisando na internet.")
            text = text.replace(item, "")
            run(text)
            return True
    for item in frases_series:
        if item in text:
            polly_aws.text_to_audio(
                "Desculpe senhor, eu baixo apenas filmes por enquanto.")
            return True
