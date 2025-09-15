# Projeto LEDS - Eliabe de Jesus Loureiro

## 📌 Contextualização
O desafio consiste em desenvolver um sistema que permita realizar buscas em concursos públicos e candidatos cadastrados.

### Funcionalidades principais:
1. **Buscar concurso por CPF**  
   - O sistema lista os órgãos, editais e códigos de concursos compatíveis com o perfil do candidato, usando as profissões cadastradas.

2. **Buscar candidatos por código de concurso**  
   - O sistema lista todos os candidatos que possuem profissões compatíveis com as vagas do concurso informado.

---

## 🚀 Tecnologias Utilizadas
- **Python 3.10+**
- **SQLite3** (banco de dados relacional nativo do Python)
- **FastAPI** (para expor a API REST)
- **Uvicorn** (servidor ASGI para rodar a API)
- **CSV** (para importação inicial de dados)
- **Pytest** (para testes unitários)

---

## 🛠️ Estrutura do Projeto

```
📂 Projeto-LEDS
│── main.py              # Interface CLI do sistema
│── api.py               # API REST com FastAPI
│── modulo.py            # Funções de negócio (carregar e buscar dados)
│── database_setup.py    # Criação do banco e tabelas
│── importar_dados.py    # Importação dos dados CSV para o banco
│── test_modulo.py       # Testes unitários com Pytest
│── projeto_leds.db      # Banco de dados SQLite (gerado após setup/importação)
│── requirements.txt     # Dependências do projeto
│── README.md            # Documentação
```

---

## ⚙️ Como Configurar o Projeto

### 1. Clone o repositório
```bash
git clone <seu-repositorio>
cd Projeto-LEDS
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Crie o banco de dados
```bash
python database_setup.py
```

### 5. Importe os dados dos arquivos CSV
```bash
python importar_dados.py
```

Agora o arquivo `projeto_leds.db` está pronto para uso.

---

## ▶️ Como Rodar o Sistema

### Opção 1: Interface de Linha de Comando (CLI)
```bash
python main.py
```
Menu disponível:
- `1` → Buscar concurso por CPF
- `2` → Buscar candidatos por código de concurso
- `0` → Sair

### Opção 2: API REST com FastAPI
```bash
uvicorn api:app --reload --port 8001
```
Acesse no navegador:
- Swagger UI: [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)
- Redoc UI: [http://127.0.0.1:8001/redoc](http://127.0.0.1:8001/redoc)

Endpoints principais:
- `GET /buscar-concursos/{cpf}` → Retorna concursos compatíveis com o CPF informado
- `GET /buscar-candidatos/{codigo}` → Retorna candidatos compatíveis com o concurso informado

---

## 🧪 Testes Unitários

O projeto possui **testes unitários** implementados com `pytest`.

### Rodando os testes:
```bash
python -m pytest -v
```

Exemplo de saída esperada:
```
collected 7 items

test_modulo.py::test_normalizar_cpf PASSED
test_modulo.py::test_carregar_candidatos PASSED
test_modulo.py::test_carregar_concursos PASSED
test_modulo.py::test_buscar_concurso_encontra PASSED
test_modulo.py::test_buscar_concurso_invalido PASSED
test_modulo.py::test_buscar_candidato_encontra PASSED
test_modulo.py::test_buscar_candidato_invalido PASSED
```

✅ Todos os testes passando confirmam que o sistema funciona corretamente.

---

## 📖 Documentação do Código

### `main.py`
- Função `exibir_menu()` → Exibe as opções ao usuário.
- Função `main()` → Executa o loop principal e chama o `modulo`.

### `modulo.py`
- `normalizar_cpf(cpf)` → Normaliza um CPF removendo caracteres especiais.
- `carregar_candidatos()` → Carrega os candidatos do banco SQLite.
- `carregar_concursos()` → Carrega os concursos do banco SQLite.
- `buscar_concurso(cpf, candidatos, concursos)` → Busca concursos compatíveis com o candidato.
- `buscar_candidato(codigo, candidatos, concursos)` → Busca candidatos compatíveis com o concurso.

### `database_setup.py`
- `criar_banco()` → Cria as tabelas `candidatos` e `concursos` no SQLite.

### `importar_dados.py`
- `importar_candidatos()` → Insere candidatos do `candidatos.txt` no banco.
- `importar_concursos()` → Insere concursos do `concursos.txt` no banco.

### `api.py`
- Cria endpoints com FastAPI para buscar concursos e candidatos.

---

## ✅ Critérios Atendidos

- [x] **Legibilidade do Código** → Segue PEP8, nomes claros, funções bem definidas.
- [x] **Documentação do Código** → Docstrings em todas as funções.
- [x] **Documentação da Solução** → README completo (setup, uso e arquitetura).
- [x] **Tratamento de Erros** → CPF inexistente, concurso não encontrado, dados ausentes.
- [x] **Testes Unitários** → Implementados com Pytest.

---

## 🌟 Diferenciais Implementados

- [x] Criar um serviço com o problema (API REST com FastAPI) → **+30 pontos**
- [x] Utilizar banco de dados (SQLite) → **+30 pontos**
- [x] Implementar Clean Code (nomes claros, remoção de redundâncias) → **+20 pontos**
- [x] Implementar o padrão de programação da tecnologia escolhida (PEP8, docstrings) → **+20 pontos**
- [x] Implementar testes unitários (Pytest) → **+15 pontos**

---

## 👤 Autor
Projeto desenvolvido por **Eliabe De Jesus Loureiro**.
