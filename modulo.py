# PROJETO LEDS - ELIABE DE JESUS LOUREIRO

import sqlite3
from typing import List, Dict

DB_NAME = "projeto_leds.db"


def normalizar_cpf(cpf: str) -> str:
    # Remove pontos, traços e espaços de um CPF.
    return cpf.replace(".", "").replace("-", "").replace(" ", "")


def carregar_candidatos() -> List[Dict]:
    # Carrega todos os candidatos do banco de dados.
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, nascimento, cpf, profissoes FROM candidatos")
        registros = cursor.fetchall()

    return [
        {
            "nome": nome,
            "nascimento": nascimento,
            "cpf": cpf,
            "profissoes": [p.strip() for p in profissoes.split(",")]
        }
        for nome, nascimento, cpf, profissoes in registros
    ]


def carregar_concursos() -> List[Dict]:
    # Carrega todos os concursos do banco de dados.
    with sqlite3.connect(DB_NAME) as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT orgao, edital, codigo, vagas FROM concursos")
        registros = cursor.fetchall()

    return [
        {
            "orgao": orgao,
            "edital": edital,
            "codigo": codigo,
            "vagas": [v.strip() for v in vagas.split(",")]
        }
        for orgao, edital, codigo, vagas in registros
    ]


def buscar_concurso(cpf: str, candidatos: List[Dict], concursos: List[Dict]) -> None:
    # Exibe concursos compatíveis com o CPF informado.
    cpf = normalizar_cpf(cpf)
    candidato = next((c for c in candidatos if c["cpf"] == cpf), None)

    if not candidato:
        print("❌ CPF não encontrado.")
        return

    print(f"\n📌 Concursos compatíveis para {candidato['nome']} ({cpf}):")
    print(f"💼 Profissões: {', '.join(candidato['profissoes'])}\n")

    encontrados = False
    for concurso in concursos:
        if any(prof in concurso["vagas"] for prof in candidato["profissoes"]):
            print(
                f"🏛️ Órgão: {concurso['orgao']}\n"
                f"📑 Edital: {concurso['edital']}\n"
                f"🔢 Código: {concurso['codigo']}\n"
                f"📋 Vagas: {', '.join(concurso['vagas'])}\n"
            )
            encontrados = True

    if not encontrados:
        print("⚠️ Nenhum concurso compatível encontrado.")


def buscar_candidato(codigo: str, candidatos: List[Dict], concursos: List[Dict]) -> None:
    # Exibe candidatos compatíveis com o código de concurso informado.
    concursos_encontrados = [c for c in concursos if c["codigo"] == codigo]

    if not concursos_encontrados:
        print("❌ Concurso não encontrado.")
        return

    for concurso in concursos_encontrados:
        print(
            f"\n📌 Concurso encontrado:\n"
            f"🏛️ Órgão: {concurso['orgao']}\n"
            f"📑 Edital: {concurso['edital']}\n"
            f"🔢 Código: {concurso['codigo']}\n"
            f"📋 Vagas: {', '.join(concurso['vagas'])}\n"
        )

        encontrados = False
        for candidato in candidatos:
            if any(prof in concurso["vagas"] for prof in candidato["profissoes"]):
                print(
                    f"👤 {candidato['nome']} | 📅 {candidato['nascimento']} | 🆔 {candidato['cpf']}\n"
                    f"   💼 Profissões: {', '.join(candidato['profissoes'])}\n"
                )
                encontrados = True

        if not encontrados:
            print("⚠️ Nenhum candidato compatível encontrado.\n")
