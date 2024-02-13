import time
import threading

def mostrar_tempo_decorrido(inicio, fim):
    tempo_decorrido = round(fim - inicio)
    print(f'Tempo decorrido: {tempo_decorrido} segundos.\n')

def andar():
    inicio = time.time()

    print('Começou a andar...')
    time.sleep(2)
    print('\nTerminou de andar!')

    fim = time.time()
    mostrar_tempo_decorrido(inicio, fim)

def tocar_musica():
    inicio = time.time()

    print('Música começou a tocar')
    time.sleep(3)
    print('Música parou de tocar!')

    fim = time.time()
    mostrar_tempo_decorrido(inicio, fim)

inicio = time.time()

thread_andar = threading.Thread(target=andar)
thread_tocar_musica = threading.Thread(target=tocar_musica)

thread_andar.start()
thread_tocar_musica.start()

thread_andar.join()
thread_tocar_musica.join()

fim = time.time()

print('As funções foram executadas!')
mostrar_tempo_decorrido(inicio, fim)