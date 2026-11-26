from vitality_database.sql_querys import(
    consultar_alunos,
    consultar_professores,
    consultar_matriculas
)
from alterar_dados.menu_alterar import (
    alterar_cadastro,
    alterar_plano
)

def criar_senha():
    senhas = []
    print('CRIE UMA SENHA!\n ')
    while True:
        senha_admin = input('DIGITE SUA SENHA: ')
        if len(senha_admin) >= 8:
            senhas.append(senha_admin)
            print('SENHA CRIADA COM SUCESSO!')
            break
        else:
            print('A SENHA DEVE CONTER NO MINIMO 8 CARACTERES')
    return senhas, senha_admin

def senha_menu(senhas):
    while True:
        senha_digitada = input('CONFIRME A SENHA: ')
        if senha_digitada in senhas:
            print('ACESSANDO MENU...')
            break
        else:
            print('SENHA INVALIDA!')

def menu_admin():
    while True:
        print('''
====================================================
          ÁREA RESTRITA - ADMIN/PROFESSORES
====================================================

   CONSULTAS DO SISTEMA
    [1] Consultar Alunos
    [2] Consultar Professores
    [3] Consultar Matrículas

    ALTERAR DADOS DOS ALUNOS
    [4] ALTERAR DADOS
    [5] ALTERAR PLANO
   GERENCIAMENTO E EXCLUSÃO
    [6] Cancelar Matrículas
    [7] Exclusão de Profissionais

   NAVEGAÇÃO
    [0] Sair / Voltar
==================================================
''')

        opcao_menu = input('\nOPCÃO:')
        match opcao_menu:
            case '1':
                consultar_alunos()
            case '2':
                consultar_professores()
            case '3':
                consultar_matriculas()
            case '4':
                id_aluno = alterar_cadastro()
            case '5':
                alterar_plano()
            case '0':
                break
