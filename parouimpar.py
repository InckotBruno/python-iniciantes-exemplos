# Verificar se um número é par ou ímpar: Desenvolva um programa que receba um número como entrada e determine se ele é par ou ímpar.

#a proposta do exercicio pede para que o usuário me fale um número para ver se é par ou impar, então por isso eu começo com INPUT

numero = float(input ("fala um numero ai meu bom: ")) #AQUI USEI O FLOAT PQ SEI Q ISSO O USUÁRIO PODE COLOCAR 2.3 
resto = numero % 2 # Sebendo que qualquer número dividido por 2 com resto zero é par // O operador de módulo(%) é utilizado para obter o resto da divisão.

if resto == 0: # Inicia um bloco condicional que verifica se o resto é igual a zero. - Se verdadeiro (indicando que o número é par), executa o próximo bloco de código.
    print('Esse número é par')

else: # Se o bloco condicional anterior for falso (indicando que o número é ímpar), executa o próximo bloco de código.
    print("Este número que tu digitou é ímpar meu mano")