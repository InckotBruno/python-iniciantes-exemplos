#Ordenar uma lista em ordem crescente: Crie uma função que receba uma lista de números como entrada e retorne a mesma lista ordenada em ordem crescente.

# Solicita ao usuário inserir números separados por espaços
entrada = input("Fala uns números separados por espaços ai meu nobre: ")

# Converte a entrada em uma lista de floats
numeros = [float(num) for num in entrada.split()]

def ordenar_lista(lista):
    # faz a função
    lista_ordenada = sorted(lista)
    return lista_ordenada

# fala a lista original
print("Lista original:", numeros)

# Chama a função para ordenar a lista e imprime o resultado
lista_ordenada = ordenar_lista(numeros)
print("Lista ordenada:", lista_ordenada)
