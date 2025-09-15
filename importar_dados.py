# PROJETO LEDS - ELIABE DE JESUS LOUREIRO

import sqlite3
import csv

DB_NAME = "projeto_leds.db"

def normalizar_cpf(cpf: str) -> str:
    # Normaliza um CPF removendo caracteres especiais.
    return cpf.replace(".", "").replace("-", "").replace(" ", "")

def importar_candidatos() -> None:
    # Importa candidatos do arquivo candidatos.txt para o banco.
    with sqlite3.connect(DB_NAME) as conexao, open("candidatos.txt", "r", encoding="utf-8") as f:
        cursor = conexao.cursor()
        leitor = csv.reader(f)
        next(leitor)  # Pula cabeçalho
        for nome, nascimento, cpf, profissoes in leitor:
            cursor.execute(
                """
                INSERT OR IGNORE INTO candidatos (nome, nascimento, cpf, profissoes)
                VALUES (?, ?, ?, ?)
                """,
                (nome.strip(), nascimento.strip(), normalizar_cpf(cpf), profissoes.strip("[]"))
            )
        conexao.commit()
    print("✅ Candidatos importados com sucesso!")


def importar_concursos() -> None:
    # Importa concursos do arquivo concursos.txt para o banco.
    with sqlite3.connect(DB_NAME) as conexao, open("concursos.txt", "r", encoding="utf-8") as f:
        cursor = conexao.cursor()
        leitor = csv.reader(f)
        next(leitor)
        for orgao, edital, codigo, vagas in leitor:
            cursor.execute(
                """
                INSERT OR IGNORE INTO concursos (orgao, edital, codigo, vagas)
                VALUES (?, ?, ?, ?)
                """,
                (orgao.strip(), edital.strip(), codigo.strip(), vagas.strip("[]"))
            )
        conexao.commit()
    print("✅ Concursos importados com sucesso!")


if __name__ == "__main__":
    importar_candidatos()
    importar_concursos()
