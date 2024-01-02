#Calcular o fatorial de um número: Crie uma função que calcule o fatorial de um número dado como entrada.

# Solicita ao usuário para inserir um número, não vou explicar mais pq usar FLOAT E INPUT
numero = float(input("Fala um número para fatorar: "))

# usei um metodo recursivo, mas usar LOOP ITERATIVO
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Chama a função fatorial e imprime o resultado
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")