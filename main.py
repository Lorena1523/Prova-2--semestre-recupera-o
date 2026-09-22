ARQUIVO = "medicamentos.txt"
def carregar_medicamentos():
    """Carrega os medicamentos salvos no arquivo."""
    medicamentos = []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha:
                    dados = linha.split(";")

                    medicamento = {
                        "nome": dados[0],
                        "categoria": dados[1],
                        "quantidade": int(dados[2])
                    }

                    medicamentos.append(medicamento)

    except FileNotFoundError:
        # Se o arquivo ainda não existe, começa com uma lista vazia.
        medicamentos = []

    return medicamentos


def salvar_medicamentos(medicamentos):
    """Salva todos os medicamentos no arquivo."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for medicamento in medicamentos:
            arquivo.write(
                f"{medicamento['nome']};"
                f"{medicamento['categoria']};"
                f"{medicamento['quantidade']}\n"
            )


def cadastrar_medicamento(medicamentos):
    """Cadastra um novo medicamento na lista."""
    nome = input("Nome do medicamento: ").strip()
    categoria = input("Categoria: ").strip()

    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))

            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
            else:
                break

        except ValueError:
            print("Digite uma quantidade válida.")

    medicamento = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade
    }

    medicamentos.append(medicamento)

    print("Medicamento cadastrado com sucesso!")


def listar_medicamentos(medicamentos):
    """Mostra todos os medicamentos cadastrados."""
    if len(medicamentos) == 0:
        print("\nNenhum medicamento cadastrado.")
        return

    print("\n--- MEDICAMENTOS CADASTRADOS ---")

    for indice, medicamento in enumerate(medicamentos, start=1):
        print(f"\n{indice}. Nome: {medicamento['nome']}")
        print(f"   Categoria: {medicamento['categoria']}")
        print(f"   Quantidade: {medicamento['quantidade']}")


def buscar_medicamento(medicamentos, nome_busca):
    """Busca um medicamento pelo nome e retorna o medicamento encontrado."""
    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome_busca.lower():
            return medicamento

    return None


def executar_programa():
    """Executa o menu principal do sistema."""
    medicamentos = carregar_medicamentos()

    while True:
        print("\n===== SISTEMA DE MEDICAMENTOS =====")
        print("1 - Cadastrar medicamento")
        print("2 - Listar medicamentos")
        print("3 - Buscar medicamento")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_medicamento(medicamentos)

        elif opcao == "2":
            listar_medicamentos(medicamentos)

        elif opcao == "3":
            nome = input("Digite o nome do medicamento: ").strip()
            medicamento = buscar_medicamento(medicamentos, nome)

            if medicamento is not None:
                print("\nMedicamento encontrado:")
                print(f"Nome: {medicamento['nome']}")
                print(f"Categoria: {medicamento['categoria']}")
                print(f"Quantidade: {medicamento['quantidade']}")
            else:
                print("Medicamento não encontrado.")

        elif opcao == "4":
            salvar_medicamentos(medicamentos)
            print("Dados salvos. Programa encerrado.")
            break

        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")


# Inicia o programa.
if __name__ == "__main__":
    executar_programa()
