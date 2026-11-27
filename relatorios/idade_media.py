import sqlite3
from datetime import(
    datetime,
    date
)
def data_formatada():
    data_atual = date.today()
    data_atual = data_atual.strftime("%d%m%Y")
    print(data_atual)

data_formatada()
