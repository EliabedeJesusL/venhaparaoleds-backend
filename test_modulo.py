# PROJETO LEDS - ELIABE DE JESUS LOUREIRO

import modulo

def test_normalizar_cpf():
    # Testa a normalização de CPFs.
    assert modulo.normalizar_cpf("123.456.789-00") == "12345678900"
    assert modulo.normalizar_cpf(" 111.222.333-44 ") == "11122233344"
    assert modulo.normalizar_cpf("98765432100") == "98765432100"


def test_carregar_candidatos():
    # Testa se os candidatos são carregados corretamente do banco.
    candidatos = modulo.carregar_candidatos()
    assert isinstance(candidatos, list)
    assert all(isinstance(c, dict) for c in candidatos)
    assert all("cpf" in c for c in candidatos)


def test_carregar_concursos():
    # Testa se os concursos são carregados corretamente do banco.
    concursos = modulo.carregar_concursos()
    assert isinstance(concursos, list)
    assert all(isinstance(c, dict) for c in concursos)
    assert all("codigo" in c for c in concursos)


def test_buscar_concurso_encontra(capsys):
    # Testa se a busca de concurso por CPF retorna algo válido.
    candidatos = modulo.carregar_candidatos()
    concursos = modulo.carregar_concursos()

    if candidatos:
        cpf = candidatos[0]["cpf"]
        modulo.buscar_concurso(cpf, candidatos, concursos)
        captured = capsys.readouterr()
        assert "Concursos compatíveis" in captured.out or "Nenhum concurso compatível" in captured.out


def test_buscar_concurso_invalido(capsys):
    # Testa se um CPF inexistente é tratado corretamente.
    candidatos = modulo.carregar_candidatos()
    concursos = modulo.carregar_concursos()

    modulo.buscar_concurso("00000000000", candidatos, concursos)
    captured = capsys.readouterr()
    assert "CPF não encontrado" in captured.out


def test_buscar_candidato_encontra(capsys):
    # Testa se a busca de candidatos por concurso retorna algo válido.
    candidatos = modulo.carregar_candidatos()
    concursos = modulo.carregar_concursos()

    if concursos:
        codigo = concursos[0]["codigo"]
        modulo.buscar_candidato(codigo, candidatos, concursos)
        captured = capsys.readouterr()
        assert "Concurso encontrado" in captured.out


def test_buscar_candidato_invalido(capsys):
    # Testa se um código de concurso inexistente é tratado corretamente.
    candidatos = modulo.carregar_candidatos()
    concursos = modulo.carregar_concursos()

    modulo.buscar_candidato("999999", candidatos, concursos)
    captured = capsys.readouterr()
    assert "Concurso não encontrado" in captured.out
