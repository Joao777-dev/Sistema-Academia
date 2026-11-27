from relatorios.plano_campeao import(
    plano_mais_utilizado
)
from relatorios.idade_media import(
    data_formatada
)
def menu_relatorio():
    while True:
        print('''
        [1] PLANO MAIS UTILIZADO
        [2] IDADE MÉDIA DOS ALUNOS
        [3] VOLTAR
    ''')
        opcao_menu = input('OPÇÃO: ')
        match opcao_menu:
            case '1':
                plano_mais_utilizado()
            case '2':
                data_formatada()
            case '3':
                break
