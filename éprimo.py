#Verificar se um número é primo: Implemente um programa que verifique se um número é primo, ou seja, se é divisível apenas por 1 e por ele mesmo.

def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

def primo_mais_proximo(numero):
    numero_menor = numero - 1
    numero_maior = numero + 1

    while True:
        if eh_primo(numero_menor):
            return numero_menor
        elif eh_primo(numero_maior):
            return numero_maior

        numero_menor -= 1
        numero_maior += 1


numero = int(input("Digite um número para encontrar o número primo mais próximo: "))

primo_proximo = primo_mais_proximo(numero)
print(f"O número primo mais próximo de {numero} é: {primo_proximo}")