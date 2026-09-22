ARQUIVO = "medicamentos.txt"
def carregar_medicamentos():
    """
    Carrega os medicamentos que já estão salvos no arquivo.
    Retorna uma lista de dicionários.
    """
    medicamentos = []

    try:
     #Abre o arquivo para leitura.
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            # Percorre cada linha do arquivo.
            for linha in arquivo:
                linha = linha.strip()

                 # Ignora linhas vazias.
                if linha:
                  # Separa nome, categoria e quantidade pelo ponto e vírgula.
                    dados = linha.split(";")

                    # Cria um dicionário para representar o medicamento.
                    medicamento = {
                        "nome": dados[0],
                        "categoria": dados[1],
                        "quantidade": int(dados[2])
                    } 
                   
                     # Adiciona o medicamento à lista.
                    medicamentos.append(medicamento)

    except FileNotFoundError:
        # Se o arquivo ainda não existe, começa com uma lista vazia.
        medicamentos = []

     # Retorna a lista de medicamentos carregada.
    return medicamentos


def salvar_medicamentos(medicamentos):
    """
    Salva todos os medicamentos da lista no arquivo.
    """
    # Abre o arquivo para escrita.
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

        # Percorre todos os medicamentos cadastrados.
        for medicamento in medicamentos:

            # Salva os dados separados por ponto e vírgula
            arquivo.write(
                f"{medicamento['nome']};"
                f"{medicamento['categoria']};"
                f"{medicamento['quantidade']}\n"
            )


def cadastrar_medicamento(medicamentos):
    """
    Solicita os dados do medicamento e adiciona à lista.
    """
    nome = input("Nome do medicamento: ").strip()
    categoria = input("Categoria: ").strip()

    # Repete a pergunta até o usuário informar uma quantidade válida.
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))

              # Impede que seja cadastrada uma quantidade negativa.
            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
            else:
                break

        # Trata o erro caso o usuário digite algo que não seja número.
        except ValueError:
            print("Digite uma quantidade válida.")

    # Cria um dicionário com os dados do medicamento.
    medicamento = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade
    }

    # Adiciona o novo medicamento à lista.
    medicamentos.append(medicamento)

    print("Medicamento cadastrado com sucesso!")


def listar_medicamentos(medicamentos):
    """
    Exibe todos os medicamentos cadastrados.
    """

    # Verifica se a lista está vazia.
    if len(medicamentos) == 0:
        print("\nNenhum medicamento cadastrado.")
        return

    print("\n--- MEDICAMENTOS CADASTRADOS ---")
     
     # Percorre a lista e mostra cada medicamento.
    for indice, medicamento in enumerate(medicamentos, start=1):
        print(f"\n{indice}. Nome: {medicamento['nome']}")
        print(f"   Categoria: {medicamento['categoria']}")
        print(f"   Quantidade: {medicamento['quantidade']}")


def buscar_medicamento(medicamentos, nome_busca):
    """
    Procura um medicamento pelo nome.
    Retorna o medicamento encontrado ou None.
    """
    # Percorre todos os medicamentos da lista.
    for medicamento in medicamentos:

        # Compara os nomes ignorando maiúsculas e minúsculas.
        if medicamento["nome"].lower() == nome_busca.lower():
            return medicamento

    # Retorna None quando nenhum medicamento é encontrado.
    return None


def executar_programa():
    """
    Controla o menu principal e o funcionamento do sistema.
    """ 

    # Carrega os medicamentos salvos antes de iniciar o menu.
    medicamentos = carregar_medicamentos()

     # Mantém o menu funcionando até o usuário escolher sair.
    while True:
        print("\n===== SISTEMA DE MEDICAMENTOS =====")
        print("1 - Cadastrar medicamento")
        print("2 - Listar medicamentos")
        print("3 - Buscar medicamento")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        # Opção 1: chama a função responsável pelo cadastro.
        if opcao == "1":
            cadastrar_medicamento(medicamentos)

        # Opção 2: chama a função responsável pela listagem
        elif opcao == "2":
            listar_medicamentos(medicamentos)

        # Opção 3: solicita um nome e realiza a busca.
        elif opcao == "3":
            nome = input("Digite o nome do medicamento: ").strip()
            medicamento = buscar_medicamento(medicamentos, nome)

            # Verifica se a busca encontrou um medicamento.
            if medicamento is not None:
                print("\nMedicamento encontrado:")
                print(f"Nome: {medicamento['nome']}")
                print(f"Categoria: {medicamento['categoria']}")
                print(f"Quantidade: {medicamento['quantidade']}")
            else:
                print("Medicamento não encontrado.")

         # Opção 4: salva os dados e encerra o programa.
        elif opcao == "4":
            salvar_medicamentos(medicamentos)
            print("Dados salvos. Programa encerrado.")

            # Encerra o while e, consequentemente, o programa.
            break

         # Caso o usuário digite uma opção diferente de 1 a 4.
        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")


# Executa o programa somente quando este arquivo for executado diretamente.
if __name__ == "__main__":
    executar_programa()
