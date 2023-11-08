from datetime import datetime
import calendar
import locale

# Defina o idioma como português
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

# Função para verificar se a data de nascimento está no mês atual
def aniversariantes_do_mes(data_nascimento):
    hoje = datetime.now()
    return data_nascimento.month == hoje.month

# Ler o arquivo de dados dos consultores em formato de texto
with open('02_funcionários.txt', 'r') as arquivo_txt:
    linhas = arquivo_txt.readlines()

# Obter o nome do mês em português a partir do mês atual
mes_atual = datetime.now().month
nome_mes = calendar.month_name[mes_atual]

# Verificar se há aniversariantes no mês
aniversariantes = [linha for linha in linhas[1:] if aniversariantes_do_mes(datetime.strptime(linha.strip().split('|')[2], '%Y-%m-%d'))]

if aniversariantes:
    # Nome do arquivo de saída para os aniversariantes
    arquivo_saida = f'02_aniversariantes_{nome_mes}.txt'

    with open(arquivo_saida, 'w') as arquivo_saida_txt:
        for linha in aniversariantes:
            arquivo_saida_txt.write(linha)

    print(f'Arquivo de aniversariantes do mês de {nome_mes} gerado em {arquivo_saida}')
else:
    print(f'Nenhum aniversariante encontrado para o mês de {nome_mes}. Nenhum arquivo foi criado.')
