# PROJETO LEDS - ELIABE DE JESUS LOUREIRO

import modulo

def exibir_menu():
    # Exibe o menu principal do sistema.
    print("\n=== Projeto LEDS - ELIABE DE JESUS ===")
    print("Escolha conforme o seu interesse:")
    print("1 - Buscar concurso por CPF")
    print("2 - Buscar candidatos por código de concurso")
    print("0 - Sair")


def main():
    # Executa o loop principal da aplicação.
    concursos = modulo.carregar_concursos()
    candidatos = modulo.carregar_candidatos()

    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ").strip()

        if opcao == "1":
            cpf = input("Digite o CPF: ").strip()
            modulo.buscar_concurso(cpf, candidatos, concursos)

        elif opcao == "2":
            codigo = input("Digite o código do concurso: ").strip()
            modulo.buscar_candidato(codigo, candidatos, concursos)

        elif opcao == "0":
            print("✅ Encerrando o sistema. Até mais!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
