# input: Lê uma linha com dados de entrada do usuario
# print: imprime um texto de saida (output), pulando linha

def caucular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05

    return salario * aliquota

valor_salario = float(input("Informe o valor do salário: "))
valor_beneficios = float(input("Informe o valor dos benefícios: "))
valor_imposto = caucular_imposto(valor_salario) 
saida = valor_salario - valor_imposto + valor_beneficios
print(f"Valor do salário: {valor_salario:.2f}")