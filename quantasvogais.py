# Contar a quantidade de vogais em uma palavra: Desenvolva uma função que receba uma palavra como entrada e retorne a quantidade de vogais presentes na palavra.

palavra = input("Fala uma palavra ou uma frase ai meu nobre: ")

def contar_vogais(palavra):
    # Converte a palavra para minúsculas para simplificar a contagem
    palavra = palavra.lower()

    # Definindo as vogais
    vogais = "aeiou"

    # Chama o cotnador de vogal
    quantidade_vogais = 0

    # Itera sobre cada caractere na palavra
    for caractere in palavra:
        # Verifica se o caractere é uma vogal
        if caractere in vogais:
            quantidade_vogais += 1

    # Retorna a quantidade total de vogais encontradas
    return quantidade_vogais

resultado = contar_vogais(palavra)
print(f"A palavra que tu me deu {palavra} tem {resultado} vogais")