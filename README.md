# Sistema de Cadastro de Medicamentos em Python

 ## 1\. Descrição do sistema

 O sistema de cadastro de medicamentos é uma aplicação simples desenvolvida em Python com o objetivo de permitir o cadastro e a consulta de medicamentos.

 O programa permite que o usuário:

 - Cadastre novos medicamentos;
- Visualize todos os medicamentos cadastrados;
- Pesquise um medicamento pelo nome;
- Armazene os dados em um arquivo de texto;
- Recupere os medicamentos cadastrados quando o programa for executado novamente.

 Cada medicamento possui três informações principais: **nome, categoria e quantidade**.

 Os dados são armazenados no arquivo `medicamentos.txt`. Dessa forma, as informações não são perdidas quando o programa é fechado.

 O sistema também possui um menu de opções, que facilita a interação com o usuário.

---

 ## 2\. Objetivo do sistema

 O objetivo principal do programa é criar uma forma simples de controlar medicamentos utilizando conceitos básicos da linguagem Python.

 Além de realizar o cadastro, o sistema permite colocar em prática diversos conceitos de programação, como:

 - Variáveis;
- Funções;
- Listas;
- Dicionários;
- Estruturas de repetição;
- Estruturas condicionais;
- Entrada e saída de dados;
- Validação de informações;
- Manipulação de arquivos;
- Organização do código em funções.

 Dessa maneira, o projeto demonstra como diferentes recursos do Python podem ser utilizados em conjunto para desenvolver uma aplicação funcional.

---

 # 3\. Como utilizar o sistema

 Para utilizar o sistema, é necessário ter o Python instalado no computador.

 Depois, basta executar o arquivo `.py` que contém o programa.

 Ao iniciar, o sistema apresenta um menu com as opções disponíveis. O usuário deve informar o número correspondente à operação que deseja realizar.

 Um exemplo de menu pode ser:

```
===== CADASTRO DE MEDICAMENTOS =====
1 - Cadastrar medicamento
2 - Listar medicamentos
3 - Buscar medicamento
4 - Sair
```

 ### Cadastro

 Para cadastrar um medicamento, o usuário escolhe a opção correspondente e informa os dados solicitados.

 Por exemplo:

```
Nome: Dipirona
Categoria: Analgésico
Quantidade: 20
```

 O programa verifica se a quantidade informada é válida e, caso esteja correta, adiciona o medicamento à lista.

 ### Listagem

 Ao escolher a opção de listar medicamentos, o programa apresenta todos os medicamentos cadastrados.

 Exemplo:

```
1 - Dipirona | Analgésico | Quantidade: 20
2 - Paracetamol | Analgésico | Quantidade: 15
```

 ### Busca

 Na opção de busca, o usuário informa o nome do medicamento que deseja encontrar.

 Por exemplo:

```
Digite o nome do medicamento: dipirona
```

 O sistema procura o medicamento na lista e apresenta suas informações caso ele seja encontrado.

 A busca não diferencia letras maiúsculas e minúsculas. Portanto, pesquisar `dipirona`, `Dipirona` ou `DIPIRONA` pode encontrar o mesmo medicamento.

 ### Saída

 Quando o usuário escolhe a opção de sair, o programa salva os medicamentos no arquivo `medicamentos.txt` e encerra sua execução.

---

 # 4\. Armazenamento dos dados

 O sistema utiliza um arquivo de texto chamado:

```
medicamentos.txt
```

 Esse arquivo funciona como uma forma simples de armazenamento dos dados.

 As informações de cada medicamento são separadas por ponto e vírgula.

 Por exemplo:

```
Dipirona;Analgésico;20
Paracetamol;Analgésico;15
```

 Cada linha representa um medicamento.

 O uso do arquivo permite que os dados continuem disponíveis mesmo depois que o programa for fechado.

---

 # 5\. Explicação das funções

 ## 5.1. Variável `ARQUIVO`

 Antes das funções, é definida a variável:

```
ARQUIVO = "medicamentos.txt"
```

 Essa variável indica qual arquivo será utilizado para armazenar os medicamentos.

 Em vez de escrever o nome do arquivo várias vezes no código, o programa utiliza a variável `ARQUIVO`.

 Isso facilita uma possível alteração futura. Por exemplo, se fosse necessário mudar o nome do arquivo para `estoque.txt`, bastaria alterar essa variável.

---

 ## 5.2. Função `carregar_medicamentos()`

 A função `carregar_medicamentos()` é responsável por carregar os medicamentos que foram salvos anteriormente.

 Quando o programa começa, essa função verifica se o arquivo `medicamentos.txt` existe.

 Se o arquivo existir, o programa:

 1. Abre o arquivo;
2. Lê cada linha;
3. Separa os dados pelo ponto e vírgula;
4. Identifica o nome, a categoria e a quantidade;
5. Cria um dicionário para cada medicamento;
6. Adiciona os dicionários a uma lista.

 Por exemplo, uma linha como:

```
Dipirona;Analgésico;20
```

 pode ser transformada em:

```
{
    "nome": "Dipirona",
    "categoria": "Analgésico",
    "quantidade": 20
}
```

 Ao final, a função retorna uma lista contendo todos os medicamentos encontrados.

 Caso o arquivo ainda não exista, a função começa com uma lista vazia.

 ### Resumindo

 A função `carregar_medicamentos()` serve para **recuperar os dados salvos no arquivo e colocá-los novamente na memória do programa**.

---

 # 5.3. Função `salvar_medicamentos()`

 A função `salvar_medicamentos()` realiza o processo contrário da função anterior.

 Ela recebe a lista de medicamentos e grava seus dados no arquivo `medicamentos.txt`.

 Para cada medicamento, são gravados:

 - Nome;
- Categoria;
- Quantidade.

 Os dados são separados pelo caractere `;`.

 Por exemplo:

```
Dipirona;Analgésico;20
Paracetamol;Analgésico;15
```

 Essa função é importante porque permite manter os dados armazenados mesmo depois que o programa for encerrado.

 ### Resumindo

 A função `salvar_medicamentos()` serve para **gravar no arquivo os medicamentos que estão armazenados na memória do programa**.

---

 # 5.4. Função `cadastrar_medicamento()`

 A função `cadastrar_medicamento()` é responsável por realizar o cadastro de um novo medicamento.

 Primeiro, o programa solicita ao usuário o nome do medicamento.

 Depois, solicita a categoria.

 Por último, solicita a quantidade.

 Exemplo:

```
Nome: Dipirona
Categoria: Analgésico
Quantidade: 20
```

 A quantidade passa por uma validação para garantir que o usuário informe um valor numérico válido.

 Também é verificado se a quantidade não é negativa.

 Depois que todas as informações são consideradas válidas, o programa cria um dicionário com os dados:

```
{
    "nome": "Dipirona",
    "categoria": "Analgésico",
    "quantidade": 20
}
```

 Esse dicionário é então adicionado à lista de medicamentos.

 ### Resumindo

 A função `cadastrar_medicamento()` serve para **receber os dados do usuário, validar as informações e adicionar um novo medicamento à lista**.

---

 # 5.5. Função `listar_medicamentos()`

 A função `listar_medicamentos()` tem como objetivo mostrar na tela todos os medicamentos cadastrados.

 Para isso, utiliza uma estrutura de repetição `for`.

 O `for` percorre cada medicamento presente na lista e exibe suas informações.

 Por exemplo:

```
1 - Dipirona
Categoria: Analgésico
Quantidade: 20

2 - Paracetamol
Categoria: Analgésico
Quantidade: 15
```

 Essa função permite que o usuário visualize facilmente os medicamentos existentes no sistema.

 ### Resumindo

 A função `listar_medicamentos()` serve para **percorrer a lista e apresentar os medicamentos cadastrados ao usuário**.

---

 # 5.6. Função `buscar_medicamento()`

 A função `buscar_medicamento()` é responsável por procurar um medicamento específico.

 Ela recebe a lista de medicamentos e o nome que o usuário deseja pesquisar.

 Depois, percorre a lista utilizando uma estrutura de repetição.

 A comparação dos nomes ignora diferenças entre letras maiúsculas e minúsculas.

 Por exemplo, as pesquisas:

```
dipirona
Dipirona
DIPIRONA
```

 podem encontrar o mesmo medicamento.

 Se o medicamento for encontrado, a função retorna seus dados.

 Caso contrário, retorna:

```
None
```

 O `None` indica que nenhum medicamento correspondente foi encontrado.

 ### Resumindo

 A função `buscar_medicamento()` serve para **localizar um medicamento pelo nome e retornar suas informações caso ele exista**.

---

 # 5.7. Função `executar_programa()`

 A função `executar_programa()` é responsável por controlar o funcionamento geral do sistema.

 Ela funciona como a principal função do programa.

 Primeiro, ela chama:

```
carregar_medicamentos()
```

 Assim, os medicamentos que já estavam salvos são carregados.

 Depois, é iniciado um `while`, que mantém o menu funcionando.

 Enquanto o usuário não escolher a opção de sair, o menu continuará aparecendo.

 A função utiliza `if`, `elif` e `else` para verificar a opção escolhida pelo usuário.

 Por exemplo:

```
Se escolher 1 → cadastrar medicamento
Se escolher 2 → listar medicamentos
Se escolher 3 → buscar medicamento
Se escolher 4 → sair
```

 ### Resumindo

 A função `executar_programa()` serve para **coordenar todas as outras funções e controlar o funcionamento do sistema**.

---

 # 6\. Estrutura `while`

 O `while` é utilizado para manter o menu funcionando continuamente.

 Depois que o usuário realiza uma operação, o programa volta a apresentar o menu.

 Por exemplo:

```
Menu
 ↓
Usuário escolhe cadastrar
 ↓
Medicamento é cadastrado
 ↓
Menu aparece novamente
 ↓
Usuário escolhe listar
 ↓
Medicamentos são exibidos
 ↓
Menu aparece novamente
```

 Esse processo continua até o usuário escolher a opção de sair.

---

 # 7\. Estruturas `if`, `elif` e `else`

 Essas estruturas são utilizadas para tomar decisões dentro do programa.

 O `if` verifica uma primeira condição.

 O `elif` verifica outras possibilidades.

 O `else` é utilizado quando nenhuma das condições anteriores foi atendida.

 No sistema, essas estruturas são utilizadas para identificar a opção escolhida pelo usuário no menu.

 Assim, cada número digitado pode levar a uma função diferente.

---

 # 8\. Uso do `break`

 Quando o usuário escolhe sair do sistema, o programa precisa interromper o `while`.

 Para isso, é utilizado o comando:

```
break
```

 Antes do `break`, os dados são salvos utilizando:

```
salvar_medicamentos()
```

 Dessa maneira, o programa primeiro garante que os dados sejam armazenados e depois encerra o menu.

---

 # 9\. Estrutura `if __name__ == "__main__"`

 No final do código existe:

```
if __name__ == "__main__":
    executar_programa()
```

 Essa estrutura verifica se o arquivo Python está sendo executado diretamente.

 Quando o arquivo é executado diretamente, `__name__` recebe o valor `"__main__"`.

 Nesse caso, o programa chama:

```
executar_programa()
```

 e inicia o sistema.

 Essa estrutura também é útil porque permite que o arquivo seja importado em outro programa sem executar automaticamente o sistema principal.

---

 # 10\. Fluxo completo do sistema

 O funcionamento geral pode ser resumido da seguinte maneira:

```
INÍCIO
   ↓
Carregar medicamentos salvos
   ↓
Exibir menu
   ↓
Usuário escolhe uma opção
   ↓
┌─────────────────────────────┐
│ 1 → Cadastrar medicamento   │
│ 2 → Listar medicamentos     │
│ 3 → Buscar medicamento      │
│ 4 → Salvar e sair           │
└─────────────────────────────┘
   ↓
Voltar para o menu
   ↓
Usuário escolhe sair
   ↓
Salvar medicamentos
   ↓
break
   ↓
FIM
```

---

 # 11\. Resumo das funções

 | Função/estrutura | Finalidade |
| --- | --- |
| `ARQUIVO` | Define o nome do arquivo utilizado para armazenar os dados. |
| `carregar_medicamentos()` | Recupera os medicamentos salvos no arquivo. |
| `salvar_medicamentos()` | Salva os medicamentos no arquivo. |
| `cadastrar_medicamento()` | Recebe e cadastra um novo medicamento. |
| `listar_medicamentos()` | Exibe todos os medicamentos cadastrados. |
| `buscar_medicamento()` | Procura um medicamento pelo nome. |
| `executar_programa()` | Controla o funcionamento geral do sistema. |
| `for` | Percorre os medicamentos da lista. |
| `while` | Mantém o menu funcionando. |
| `if`, `elif`, `else` | Tomam decisões de acordo com a opção escolhida. |
| `break` | Encerra o `while`. |
| `if __name__ == "__main__"` | Inicia o programa quando o arquivo é executado diretamente. |

---

 # 12\. Conclusão

 O sistema de cadastro de medicamentos é uma aplicação simples, mas permite demonstrar vários conceitos importantes da programação em Python.

 O programa utiliza funções para dividir as responsabilidades do sistema, listas e dicionários para organizar os medicamentos, estruturas condicionais para controlar as opções do menu e estruturas de repetição para realizar tarefas como percorrer a lista e manter o sistema funcionando.

 Além disso, a utilização do arquivo `medicamentos.txt` permite que os dados sejam armazenados de forma persistente. Assim, os medicamentos cadastrados continuam disponíveis mesmo depois que o programa é encerrado.

 Dessa forma, o projeto apresenta uma aplicação prática dos principais conceitos básicos de Python, utilizando uma estrutura organizada e de fácil compreensão.