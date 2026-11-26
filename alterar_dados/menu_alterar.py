from cadastro_usuario.cadastro import (
    cadastro_usuario
)
import sqlite3

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
