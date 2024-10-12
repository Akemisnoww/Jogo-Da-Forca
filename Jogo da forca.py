import random
import unicodedata

def escolher_palavra():
    palavras = ['arroz', 'doce', 'jogos', 'cartas', 'desafio']
    return random.choice(palavras).lower()

def exibir_palavra(palavra, letras_corretas):
    return ''.join([letra if letra in letras_corretas else '_' for letra in palavra])

def normalizar(texto):
    
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower()

def jogar():
    palavra = escolher_palavra()
    palavra_normalizada = normalizar(palavra)
    letras_corretas = []
    letras_erradas = []
    tentativas_restantes = 6
    venceu = False

    while tentativas_restantes > 0 and not venceu:
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Palavra: {exibir_palavra(palavra, letras_corretas)}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        palpite = input('Digite uma letra: ').lower()

        
        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        palpite = normalizar(palpite)

        if palpite in letras_corretas or palpite in letras_erradas:
            print('Você já tentou essa letra.')
            continue

        if palpite in palavra_normalizada:
            letras_corretas.append(palpite)
            if all(letra in letras_corretas for letra in palavra_normalizada):
                venceu = True
        else:
            letras_erradas.append(palpite)
            tentativas_restantes -= 1

    if venceu:
        print(f'Parabéns! Você venceu! A palavra era {palavra}.')
    else:
        print(f'Você perdeu! A palavra era {palavra}.')

jogar()