# Converter temperatura de Celsius para Fahrenheit: Escreva um programa que converta uma temperatura em graus Celsius para Fahrenheit. (X °C × 9/5) + 32 

# LEMBRA QUE O USUÁRIO TENQ COLOCAR O VALOR QUE ELE QUER PARA CALCULAR (INPUT), FLOAT PQ TEMPERATURA PODE 99,99 CELCIUS IGUAL INVERNO NO RJ
celsius = float(input("Fala a temperatura em graus Celsius: "))

# Fórmula de conversão de Celsius para Fahrenheit: (Celsius × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

#f na frente de uma string em Python indica que a string é uma "f-string" (format string) permitindo a incorporação de variáveis diretamente na string. - SIM, N SABIA DISSO.
print(f"A temperatura em Fahrenheit é: {fahrenheit}°F") 
#O valor da variável fahrenheit será substituído diretamente na string onde a expressão {fahrenheit} está localizada.