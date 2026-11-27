import sqlite3
def plano_mais_utilizado():
    conexao = sqlite3.connect("vitality.db")
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT plano_aluno
        FROM matriculas_alunos
        GROUP BY plano_aluno
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """)
    plano_mais_utilizado = cursor.fetchone()[0]
    print(f'O PLANO VENCEDOR É: {plano_mais_utilizado}')
