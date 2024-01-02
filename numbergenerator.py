# Calcular a média de uma lista de números em mémoria: Crie um programa que receba uma lista de números e retorne a média dos valores presentes na lista.

import random

random.seed() # Visite a bibloteca RANDOM

def olhaonumeroai():
    # Cria uma lista para armezenar os numeros que vão ser gerados ainda no FOR I IN
    numeros = []
    
    for i in range(5):
        numero = random.randint(0, 100)
        print(numero)
        numeros.append(numero)  # o método append está sendo usado para adicionar cada número gerado à lista chamada numeros;

        #####################################################################################################################
        #fruits = ["apple", "banana", "cherry"]

        #fruits.append("orange")

        #print(fruits)
        #ESSE COMENTARIO VAI RETORNAR:
        #['apple', 'banana', 'cherry', 'orange']
        
    return numeros  # O RETURN vai devolver com os valores gerados

numeros_gerados = olhaonumeroai()

# - OLHA Q BONITO ELE "TRANSFORMOU" Olhaonumeroai para interagir para fazer a média com o calculo abaixo

soma = sum(numeros_gerados)
media = soma / len(numeros_gerados)

# CHAMA O RESULTADO PARA TELA
print(media)
