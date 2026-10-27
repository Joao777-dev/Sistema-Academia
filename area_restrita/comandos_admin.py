from vitality_database.sql_querys import(
    consultar_alunos,
    consultar_professores,
    consultar_matriculas,
    consultar_aulas,
    inserir_ficha_treino,
    consultar_ficha_aluno
)


def menu_admin():
    while True:
        print('''
====================================================
          ÁREA RESTRITA - ADMIN/PROFESSORES
====================================================

   GESTÃO DE AULAS
    [1] Montar Ficha
    [2] Consultar Exercicios
    [3] Visualizar Fichas

   CONSULTAS DO SISTEMA
    [4] Consultar Alunos
    [5] Consultar Professores
    [6] Consultar Matrículas

   GERENCIAMENTO E EXCLUSÃO
    [7] Cancelar Matrículas
    [8] Exclusão de Profissionais

   NAVEGAÇÃO
    [0] Sair / Voltar
==================================================
''')

        opcao_menu = input('\nOPCÃO:')
        match opcao_menu:
            case '1':
                inserir_ficha_treino(
                    aluno_id=10,
                    exercicio_id=1,
                    dia_treino="Terça-feira",
                    num_series=4,
                    num_repeticoes="10-12"
                )
            case '2':
                 consultar_aulas()
            case '3':
                consultar_ficha_aluno(10)
            case '4':
                consultar_alunos()
            case '5':
                consultar_professores()
            case '6':
                consultar_matriculas()
            case '7':
                print('SOMENTE PESSOAS AUTORIZADAS!')
            case '8':
                print('SOMENTE PESSOAS AUTORIZADAS!')
            case '0':
                break
