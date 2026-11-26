import sqlite3
conexao = sqlite3.connect("vitality.db")
cursor = conexao.cursor()

#---------QUERYS PARA CRIAÇÃO E INSERÇÃO DE ALUNOS---------

def tabela_alunos():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS dados_alunos(
    id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_aluno VARCHAR(30) NOT NULL,
    data_nasc VARCHAR(8),
    cpf_aluno VARCHAR(11),
    telefone VARCHAR(11)
    )''')
    conexao.commit()
    conexao.close()


def inserir_alunos(nome_usuario, data_nasc, cpf_usuario, tel_usuario):
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    sql_query = (''' INSERT INTO dados_alunos (nome_aluno, data_nasc, cpf_aluno, telefone )VALUES (?, ?, ?, ?)''')
    cursor.execute(sql_query, (nome_usuario, data_nasc, cpf_usuario, tel_usuario))
    id_usuario = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return id_usuario

#---------QUERYS PARA CRIAÇÃO E INSERÇÃO DE PROFESSORES---------

def tabela_professores():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS dados_professores(
    id_professor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_professor VARCHAR(255) NOT NULL,
    data_nasc VARCHAR(8) NOT NULL,
    cpf_professor VARCHAR(11) NOT NULL,
    telefone VARCHAR(11) NOT NULL
    )''')
    conexao.commit()
    conexao.close()

def inserir_professores(nome_usuario, data_nasc, cpf_usuario, tel_usuario):
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    sql_query = (''' INSERT INTO dados_professores (nome_professor, data_nasc, cpf_professor, telefone )VALUES (?, ?, ?, ?)''')
    cursor.execute(sql_query, (nome_usuario, data_nasc, cpf_usuario, tel_usuario))
    id_usuario = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return id_usuario


#---------QUERYS PARA CRIAÇÃO E INSERÇÃO DE MATRICULAS ---------

def tabela_matriculas():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('''CREATE TABLE IF NOT EXISTS matriculas_alunos(
    id_matricula INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    plano_aluno VARCHAR(10) NOT NULL,
    aluno_id INT NOT NULL,
    data_matricula TEXT NOT NULL,
    CONSTRAINT fk_matricula_aluno
    FOREIGN KEY (aluno_id)
    REFERENCES dados_alunos(id_aluno)
    )''')
    conexao.commit()
    conexao.close()

def inserir_matriculas(plano_aluno, aluno_id, data_matricula):
    conexao = sqlite3.connect("vitality.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()

    sql_query = (''' INSERT INTO  matriculas_alunos (plano_aluno, aluno_id, data_matricula) VALUES (?, ?, ?)''')
    cursor.execute(sql_query, (plano_aluno, aluno_id, data_matricula))
    conexao.commit()
    conexao.close()
