

#Verificar se uma palavra é um palíndromo: Implemente um programa que verifique se uma palavra é um palíndromo, ou seja, se pode ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda.


# pfv pip install unidecode 

from unidecode import unidecode


# Solicita ao usuário para inserir uma palavra
palavra = input("Fala uma palavra ou uma frase ai meu nobre: ")

# Remove espaços e converte para minúsculas para facilitar a comparação, tive dificuldade em usar em frase
palavra = unidecode(palavra.replace(" ", "").replace("-", "").replace(",", "")).lower()#vc sabe pq para subir os acentos  --- descobri que uma bibloteca chamada UNICODE que tira os acentos

# Verifica se a palavra ou frase é um palíndromo
if palavra == palavra[::-1]: #Esta é uma forma de slicing em Python, onde [::-1] indica que queremos pegar todos os elementos da sequência (palavra) com um passo de -1, ou seja, invertendo a ordem dos elementos.
    print("Cacetada a oração/palavra é braba")
else:
    print("que pena")

