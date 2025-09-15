# PROJETO LEDS - ELIABE DE JESUS LOUREIRO

from fastapi import FastAPI
import modulo

app = FastAPI(title="Projeto LEDS API - Eliabe de Jesus")

@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à API do Projeto LEDS"}

@app.get("/candidatos")
def listar_candidatos():
    return modulo.carregar_candidatos()

@app.get("/concursos")
def listar_concursos():
    return modulo.carregar_concursos()

@app.get("/candidatos/{cpf}")
def buscar_concursos_por_cpf(cpf: str):
    candidatos = modulo.carregar_candidatos()
    concursos = modulo.carregar_concursos()
    cpf = modulo.normalizar_cpf(cpf)

    candidato = next((c for c in candidatos if c["cpf"] == cpf), None)
    if not candidato:
        return {"erro": "CPF não encontrado."}

    concursos_compativeis = []
    for concurso in concursos:
        if any(prof in concurso["vagas"] for prof in candidato["profissoes"]):
            concursos_compativeis.append(concurso)

    return {"candidato": candidato, "concursos_compativeis": concursos_compativeis}

@app.get("/concursos/{codigo}")
def buscar_candidatos_por_codigo(codigo: str):
    candidatos = modulo.carregar_candidatos()
    concursos = modulo.carregar_concursos()

    concurso = next((c for c in concursos if c["codigo"] == codigo), None)
    if not concurso:
        return {"erro": "Concurso não encontrado."}

    candidatos_compativeis = [
        c for c in candidatos if any(prof in concurso["vagas"] for prof in c["profissoes"])
    ]

    return {"concurso": concurso, "candidatos_compativeis": candidatos_compativeis}
