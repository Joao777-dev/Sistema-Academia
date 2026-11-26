import sqlite3
conexao = sqlite3.connect("vitality.db")
cursor = conexao.cursor()

def consultar_professores():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM dados_professores')

    professores_consultados = cursor.fetchall()
    print('\nPROFESSORES CONSULTADOS: \n')
    print(f'{'ID':<4} {'NOME':<20} {'DATA NASC':<21} {'CPF':<19} {'TELEFONE'}')
    print('-' * 80)
    for professor in professores_consultados:
        print(f"{professor[0]:<4} {professor[1]:<20} {professor[2]:<21} {professor[3]:<19} {professor[4]}")
    conexao.close()
