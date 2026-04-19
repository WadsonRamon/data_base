import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                titular TEXT NOT NULL,
                saldo FLOAT NOT NULL,
                cpf TEXT NOT NULL UNIQUE
                )""")
                
cursor.execute("""INSERT INTO contas_bancarias
                (titular, saldo, cpf) VALUES
                ('Raimundo', 80000, '60232193424')""")

cursor.execute("""SELECT * FROM contas_bancarias""")

for row in cursor.fetchall():
    print(row)
    

conexao.commit()