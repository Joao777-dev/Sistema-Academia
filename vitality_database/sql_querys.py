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
tabela_alunos()

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


#--------QUERYS PARA CRIAÇÃO E INSERÇÃO DE EXERCICIOS-------
def tabela_exercicios():
    conexao = sqlite3.connect("vitality.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exercicios (
        id_exercicio INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_exercicio TEXT NOT NULL,
        grupo_muscular TEXT NOT NULL
    )'''
    )

def inserir_exercicios():
  conexao = sqlite3.connect("vitality.db")
  cursor = conexao.cursor()

  lista_exercicios = [
    ("Supino Reto com Barra", "Peito"),
    ("Supino Inclinado com Halteres", "Peito"),
    ("Tríceps na Polia com Barra", "Tríceps"),
    ("Desenvolvimento com Halteres", "Ombros"),
    
    ("Puxada Alta na Polia", "Costas"),
    ("Remada Baixa", "Costas"),
    ("Rosca Direta com Barra", "Bíceps"),
    ("Rosca Alternada", "Bíceps"),
    
    ("Agachamento Livre", "Pernas"),
    ("Leg Press 45", "Pernas"),
    ("Cadeira Extensora", "Pernas"),
    ("Panturrilha Smith", "Pernas"),
    
    ("Elevação Lateral com Halteres", "Ombros"),
    ("Desenvolvimento Militar", "Ombros"),
    ("Encolhimento com Halteres", "Trapézio"),
    ("Abdominal Supra no Solo", "Abdominais"),
    ("Abdominal Infra na Paralela", "Abdominais"),
    
    ("Mesa Flexora", "Pernas"),
    ("Stiff com Barra", "Pernas"),
    ("Elevação Pélvica com Barra", "Glúteos"),
    ("Panturrilha Sentada na Máquina", "Pernas"),
]

  cursor.executemany('''INSERT  INTO exercicios (nome_exercicio, grupo_muscular) 
    VALUES (?, ?)''',
    lista_exercicios,
  )
  conexao.commit()
  conexao.close()

def tabela_ficha_treino():
    conexao = sqlite3.connect("vitality.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ficha_treino (
        id_ficha INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        exercicio_id INTEGER NOT NULL,
        dia_treino TEXT NOT NULL,
        num_series INTEGER NOT NULL,
        num_repeticoes TEXT NOT NULL,
        CONSTRAINT fk_aluno_ficha 
            FOREIGN KEY (aluno_id) 
            REFERENCES dados_alunos(id_aluno),
        CONSTRAINT fk_exercicio_ficha 
            FOREIGN KEY (exercicio_id) 
            REFERENCES exercicios(id_exercicio)
    )''')
    conexao.commit()
    conexao.close()

def inserir_ficha_treino(aluno_id, exercicio_id, dia_treino, num_series, num_repeticoes):
    conexao = sqlite3.connect("vitality.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    
    sql_query = '''
        INSERT INTO ficha_treino (aluno_id, exercicio_id, dia_treino, num_series, num_repeticoes) 
        VALUES (?, ?, ?, ?, ?)
    '''
    cursor.execute(sql_query, (aluno_id, exercicio_id, dia_treino, num_series, num_repeticoes))
    conexao.commit()
    conexao.close()

#---------QUERYS PARA CONSULTAS---------

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

def consultar_aulas():
    cursor.execute('SELECT * FROM exercicios')
    ficha_treino = cursor.fetchall()
    print('   FICHA DE TREINO PARA INICIANTES    ')
    print(f'{'ID':<10} {'EXERCICIO':<35} {'GRUPO MUSCULAR':35} {'DIA'} ')
    print('-' * 100)
    for exercicio in ficha_treino:
        print(f"{exercicio[0]:<10} {exercicio[1]:<35} {exercicio[2]:<30} {exercicio[3]:<20}")

def consultar_ficha_aluno(aluno_id):
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    
    sql_query = '''
        SELECT 
            da.nome_aluno,
            ft.dia_treino,
            e.nome_exercicio,
            e.grupo_muscular,
            ft.num_series,
            ft.num_repeticoes
        FROM ficha_treino ft
        JOIN dados_alunos da ON ft.aluno_id = da.id_aluno
        JOIN exercicios e ON ft.exercicio_id = e.id_exercicio
        WHERE ft.aluno_id = ?
    '''
    
    cursor.execute(sql_query, (aluno_id,))
    ficha_consultada = cursor.fetchall()
    print(f'{'NOME':<20} {'DIA':<25} {'EXERCICIO':<30} {'GRUPO':<32} {'SERIES':<30} {'REPETIÇÕES':<35}')
    print('-' * 200)
    
    for ficha in ficha_consultada:
        print(f'{ficha[0]:<20} {ficha[1]:<25} {ficha[2]:<30} {ficha[3]:<32} {ficha[4]:<30} {ficha[5]:35}')
    conexao.close()


#---------QUERYS DE CANCELAMENTO/EXCLUSÃO---------   

def cancelamento_matricula(id_usuario):
    conexao = sqlite3.connect("vitality.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM  matriculas_alunos WHERE aluno_id >= ?", (id_usuario,))
    cursor.execute("DELETE FROM dados_alunos WHERE id_aluno >= ?", (id_usuario,))
    conexao.commit()
    conexao.close()
    print('MATRICULA CANCELADA COM SUCESSO! ')

def cancelamento_professores(id_usuario):
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM dados_professores WHERE id_professor >= ?", (id_usuario,))   
    conexao.commit()
    conexao.close()
    print('PROFESSOR EXCLUIDO COM SUCESSO! ')

def deletar_tabela():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS ficha_treino")
    print('TABELA DELETADA COM SUCESSO!')
    conexao.commit()
    conexao.close()

def atualizar_dados():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    cursor.execute('UPDATE dados_alunos SET nome_aluno = "Lewandosky" WHERE id_aluno = 10')
    conexao.commit()
    cursor.close()
