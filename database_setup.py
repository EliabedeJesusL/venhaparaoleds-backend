# PROJETO LEDS - ELIABE DE JESUS LOUREIRO

import sqlite3

DB_NAME = "projeto_leds.db"

def criar_banco():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nascimento TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        profissoes TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS concursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        orgao TEXT NOT NULL,
        edital TEXT NOT NULL,
        codigo TEXT NOT NULL,
        vagas TEXT NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()
    print("✅ Banco e tabelas criados com sucesso!")

if __name__ == "__main__":
    criar_banco()
