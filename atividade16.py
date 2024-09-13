# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Receber o peso e a altura da pessoa
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Calcular o IMC
imc = calcular_imc(peso, altura)

# Exibir o resultado e a classificação
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificar_imc(imc)}")