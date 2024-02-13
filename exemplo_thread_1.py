import time

def mostrar_tempo_decorrido(inicio, fim):
    tempo_decorrido = round(fim - inicio)
    print(f'Tempo decorrido: {tempo_decorrido} segundos.\n')

def andar():
    inicio = time.time()

    print('Começou a andar...')
    time.sleep(2)
    print('Terminou de andar!')

    fim = time.time()
    mostrar_tempo_decorrido(inicio, fim)

def tocar_musica():
    inicio = time.time()

    print('Música começou a tocar')
    time.sleep(2)
    print('Música parou de tocar!')

    fim = time.time()
    mostrar_tempo_decorrido(inicio, fim)

inicio = time.time()
andar()
tocar_musica()
fim = time.time()

print('As funções foram executadas!')
mostrar_tempo_decorrido(inicio, fim)