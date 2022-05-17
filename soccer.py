from pyfutebol import crawler
 
def jogos_de_hoje():
    resultados = crawler.jogos_de_hoje()
    for resultado in resultados:
        print(resultado)

def jogos_ao_vivo():
    resultados = crawler.jogos_ao_vivo(format='json')
    print(resultados)

def jogo_por_time(time):
    resultado = crawler.buscar_jogo_por_time(time)
    print(resultado)

jogos_de_hoje()