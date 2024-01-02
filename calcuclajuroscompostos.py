#Calcular o valor do juros compostos: Desenvolva uma função que calcule o valor final de um investimento com base em uma taxa de juros e um período de tempo.



def calcular_juros_compostos(principal, taxa_juros, periodo, vezes_compostos_por_ano=1):
    taxa_decimal = taxa_juros / 100
    valor_final = principal * (1 + taxa_decimal / vezes_compostos_por_ano) ** (vezes_compostos_por_ano * periodo)
    return valor_final

# Solicita ao usuário inserir as informações
principal = float(input("Informe o valor principal do investimento: "))
taxa_juros = float(input("Informe a taxa de juros anual (%): "))
periodo = float(input("Informe o período de investimento em anos: "))
vezes_compostos_por_ano = int(input("Informe o número de vezes que os juros são compostos por ano: "))

# Calcula e imprime o valor final do investimento
resultado = calcular_juros_compostos(principal, taxa_juros, periodo, vezes_compostos_por_ano)
print(f"O valor final do investimento é: {resultado:.2f}")
