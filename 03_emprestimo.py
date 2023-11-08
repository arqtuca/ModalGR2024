# Função para calcular as notas de maior valor
def calcular_notas_maior_valor(valor_emprestimo):
    notas_cem = valor_emprestimo // 100
    valor_emprestimo %= 100
    notas_cinquenta = valor_emprestimo // 50

    return notas_cem, notas_cinquenta

# Função para calcular as notas de menor valor
def calcular_notas_menor_valor(valor_emprestimo):
    notas_vinte = valor_emprestimo // 20
    valor_emprestimo %= 20
    notas_dez = valor_emprestimo // 10
    valor_emprestimo %= 10
    notas_cinco = valor_emprestimo // 5
    notas_dois = valor_emprestimo % 5

    return notas_vinte, notas_dez, notas_cinco, notas_dois

# Função para realizar a simulação de empréstimo
def simular_emprestimo(nome, data_admissao, salario_atual, valor_emprestimo, escolha):
    anos_de_servico = (2023 - int(data_admissao.split('-')[0]))
    if anos_de_servico > 5 and valor_emprestimo % 2 == 0:
        print(f"Valor empréstimo: {valor_emprestimo} reais")

        if escolha == 'maior':
            # Calcular notas de maior valor
            notas_cem, notas_cinquenta = calcular_notas_maior_valor(valor_emprestimo)
            print("Notas de maior valor:")
            if notas_cem > 0:
                print(f"{notas_cem} nota(s) de 100 reais")
            if notas_cinquenta > 0:
                print(f"{notas_cinquenta} nota(s) de 50 reais")
        else:
            # Calcular notas de menor valor
            notas_vinte, notas_dez, notas_cinco, notas_dois = calcular_notas_menor_valor(valor_emprestimo)
            print("Notas de menor valor:")
            if notas_vinte > 0:
                print(f"{notas_vinte} nota(s) de 20 reais")
            if notas_dez > 0:
                print(f"{notas_dez} nota(s) de 10 reais")
            if notas_cinco > 0:
                print(f"{notas_cinco} nota(s) de 5 reais")
            if notas_dois > 0:
                print(f"{notas_dois} nota(s) de 2 reais")
    else:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")

# Solicitar informações do colaborador
nome = input("Digite seu nome: ")
data_admissao = input("Digite o ano de sua admissão: ")
salario_atual = float(input("Digite seu salário atual: "))
valor_emprestimo = int(input("Digite o valor do empréstimo: "))
escolha = input("Escolha 'maior' para notas de maior valor ou 'menor' para notas de menor valor: ")

# Realizar a simulação de empréstimo
simular_emprestimo(nome, data_admissao, salario_atual, valor_emprestimo, escolha)
