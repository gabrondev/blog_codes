import time
import threading

def mostrar_tempo_decorrido(inicio, fim):
    tempo_decorrido = round(fim - inicio)
    print(f'Tempo decorrido: {tempo_decorrido} segundos.\n')

def andar(tempo):
    inicio = time.time()

    print('\nComeçou a andar...')
    time.sleep(tempo)
    print('\nTerminou de andar!')

    fim = time.time()
    mostrar_tempo_decorrido(inicio, fim)

def tocar_musica(tempo):
    inicio = time.time()

    print('Música começou a tocar')
    time.sleep(tempo)
    print('Música parou de tocar!')

    fim = time.time()
    mostrar_tempo_decorrido(inicio, fim)

print('Este é um exemplo de threads em Python! Digite dois números inteiros maiores que zero.\n')

while True:
    try:
        tempo_andar = int(input('Quanto tempo levará para andar? '))
        if tempo_andar <= 0:
            raise ValueError
        elif tempo_andar > 10:
            escolha = input(f"Deseja esperar {tempo_andar} segundos? 'S' para sim, 'N' para não: ").lower()
            match escolha:
                case 's':
                    break
                case _:
                    raise ValueError
        break
    except ValueError:
        print('Por favor, digite um número inteiro maior que zero.')

print('\n')

while True:
    try:
        tempo_musica = int(input('Quanto tempo a música tem? '))
        if tempo_musica <= 0:
            raise ValueError
        
        elif tempo_musica > 10:
            escolha = input(f"Deseja esperar {tempo_musica} segundos? 'S' para sim, 'N' para não: ").lower()
            match escolha:
                case 's':
                    break
                case _:
                    raise ValueError
        break
    except ValueError:
        print('Por favor, digite um número inteiro maior que zero.')

inicio = time.time()

thread_andar = threading.Thread(target=andar, args=(tempo_andar,))
thread_tocar_musica = threading.Thread(target=tocar_musica, args=(tempo_musica,))

thread_andar.start()
thread_tocar_musica.start()

thread_andar.join()
thread_tocar_musica.join()

fim = time.time()

print('As funções foram executadas!')
mostrar_tempo_decorrido(inicio, fim)