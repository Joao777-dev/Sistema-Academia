from cadastro_usuario.cadastro import (
    cadastro_usuario
)
import sqlite3

def alterar_cadastro():
    conexao = sqlite3.connect("vitality.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    print('ALTERAR CADASTRO!')
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
