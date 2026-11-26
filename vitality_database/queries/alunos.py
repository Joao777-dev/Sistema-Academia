import sqlite3
from cadastro_usuario.cadastro import (
    cadastro_usuario
)

#---------QUERIES DE CONSULTA----------

def consultar_alunos():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    cursor.execute('''
    SELECT * FROM dados_alunos
    JOIN matriculas_alunos
    ON dados_alunos.id_aluno = matriculas_alunos.aluno_id''')
    alunos_consultados = cursor.fetchall()
    print('\nALUNOS CONSULTADOS: \n')
    print(f"{'ID':<4} {'NOME':<20} {'DATA NASC':<21} {'CPF':<19} {'TELEFONE': <20} {'PLANO': <20} {'DATA MATRICULA'}")
    print("-" * 140)
    for aluno in alunos_consultados:
        print(f"{aluno[0]:<4} {aluno[1]:<20} {aluno[2]:<21} {aluno[3]:<19} {aluno[4]: <20} {aluno[6]: <20} {aluno[8]}")
    conexao.close()

def consultar_matriculas():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM matriculas_alunos")
    matriculas_consultadas = cursor.fetchall()
    print('\n    MATRICULAS CONSULTADAS: \n')
    print(f'{'RA':<4} {'PLANO':<15} {'ID_ALUNO':<16} {'DATA MATRICULA'} ')
    print('-' * 80)
    for matricula in matriculas_consultadas:
        print(f"{matricula[0]:<4} {matricula[1]:<15} {matricula[2]:<16} {matricula[3]:<20}")

    conexao.close()

#-------QUERY PARA CANCELAR MATRICULA----------

def cancelamento_matricula():
    conexao = sqlite3.connect("vitality.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    print(f'AREA DE CANCELAMENTO DE MATRICULA\n CONFIRA O {'RA'} CORRETAMENTE!\n')
    id_matricula = input('INFORME O RA DA MATRICULA: ')
    if not id_matricula.isdigit():
            print("Erro: O ID deve ser um número inteiro.")
            return
    cursor.execute('''
            SELECT * FROM dados_alunos
            JOIN matriculas_alunos
            ON dados_alunos.id_aluno = matriculas_alunos.aluno_id
            WHERE id_aluno = ?''',(id_matricula,))
    aluno_consultado = cursor.fetchall()
    print('\nMATRICULA CONSULTADA: \n')
    print(f"{'ID':<4} {'NOME':<20} {'DATA NASC':<21} {'CPF':<19} {'TELEFONE': <20} {'PLANO': <20} {'DATA MATRICULA'}")
    print("-" * 140)
    for aluno in aluno_consultado:
        print(f"{aluno[0]:<4} {aluno[1]:<20} {aluno[2]:<21} {aluno[3]:<19} {aluno[4]: <20} {aluno[6]: <20} {aluno[8]}")

    print('\nDESEJA MESMO EXCLUIR ESTE ALUNO?\n')

    confirmar_id = input('CONFIRME O RA: ')
    if confirmar_id == id_matricula:
        cursor.execute("DELETE FROM  matriculas_alunos WHERE aluno_id = ?", (id_matricula,))
        cursor.execute("DELETE FROM dados_alunos WHERE id_aluno = ?", (id_matricula,))
        print('CANCELANDO MATRICULA...')
        print('\nMATRICULA CANCELADA COM SUCESSO! ')
    else:
        print('\nNUMERO DE MATRICULA DIFERENTES!\nCONFIRA CORRETAMENTE ANTES DA OPERAÇÃO')
    conexao.commit()
    conexao.close()

#--------QUERYS PARA ALTERAR DADOS E PLANOS--------

def alterar_cadastro():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    print('ALTERAR CADASTRO')
    id_aluno = input('INFORME O ID: ')
    if not id_aluno.isdigit():
            print("Erro: O ID deve ser um número inteiro.")
            return
    nome_usuario, data_nasc, cpf_usuario, tel_usuario = cadastro_usuario()
    try:
            cursor.execute("""
                UPDATE dados_alunos
                SET nome_aluno = ?, data_nasc = ?, cpf_aluno = ?, telefone = ?
                WHERE id_aluno = ?
            """, (nome_usuario, data_nasc, cpf_usuario, tel_usuario, id_aluno))

            conexao.commit()

            if cursor.rowcount > 0:
                print(f"\nSucesso! Cliente {id_aluno} atualizado.")
            else:
                print(f"\nAtenção: Nenhum cliente foi encontrado com o ID {id_aluno}.")

    except sqlite3.Error as e:
            print(f"\nErro ao atualizar: {e}")
    finally:
        conexao.close()
def alterar_plano():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    print('CONSULTE O RA DE MATRICULA ANTES DE QUALQUER ALTERAÇÃO!\n ')
    id_aluno = input('INFORME O ID: \n')
    if not id_aluno.isdigit():
        print("Erro: O ID deve ser um número inteiro.")
        return
    lista_planos = ["BRONZE", "PRATA", "OURO\n"]
    print('PLANOS DISPONIVEIS:\n ')
    for plano in lista_planos:
        print(plano)
    opcao_plano = input("INFORME O PLANO: ").upper()
    if opcao_plano in lista_planos:
        try:
            cursor.execute("""
                        UPDATE matriculas_alunos
                        SET plano_aluno = ?
                        WHERE id_matricula = ?
                        """, (opcao_plano, id_aluno,))
            conexao.commit()
            if cursor.rowcount > 0:
                print(f"\nSucesso! Plano: {opcao_plano}, RA: {id_aluno} atualizado.")
            else:
                print(f"\nAtenção: Nenhuma matricula foi encontrada com o RA: {id_aluno}.")

        except sqlite3.Error as e:
            print(f"\nErro ao atualizar: {e}")
        finally:
                conexao.close()
