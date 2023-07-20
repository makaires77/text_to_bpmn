# Criar o repositório no GitHub pela máquina local

Inicie o repositório Git e crie o repositório GitHub: 
    Dentro do diretório principal /text_to_bpmn, inicie um novo repositório Git com git init. 

Crie um novo repositório GitHub através do site do GitHub. 
    Vincule seu repositório local ao repositório GitHub com git remote add origin [URL do repositório GitHub].

Fazer push para o GitHub: 
    Adicione todos os arquivos ao repositório Git com git add ., faça um commit com git commit -m "Initial commit" e então faça push para o GitHub com git push -u origin master.


# Guias de estilo

No contexto da programação há basicamente dois níveis de visibilidade dos artefatos de software com relação a onde estão na estrutura dos arquivos de pacotes e módulos, há artefatos "exportados" e "não exportados" no que se refere à visibilidade dos membros de um pacote, como funções, tipos e variáveis. 

No caso da linguagem Go, por exemplo, um membro de um pacote é exportado se seu nome começa com uma letra maiúscula. Membros exportados são acessíveis fora do pacote em que são definidos. Por exemplo, se você define uma função `Print()` em um pacote, você pode chamá-la de outro pacote.

Por outro lado, os membros não exportados começam com uma letra minúscula e só podem ser acessados dentro do mesmo pacote onde são definidos. Se você tem uma função `print()` em um pacote, você não pode chamá-la de outro pacote.

A razão para essa distinção é proporcionar o encapsulamento de dados, que é um princípio fundamental da programação orientada a objetos. Ele permite que você oculte os detalhes de implementação de um pacote e exponha apenas uma interface pública, o que pode tornar o código mais fácil de usar e manter.

| Linguagem/Convenção | Estilo de Case                                                | Nomeação de Artefatos          |
|---------------------|--------------------------------------------------------------|--------------------------------|
| Go (Effective Go)   | MixedCase para exportados, camelCase para não exportados     | Conciso, mnemônico             |
| Python (PEP 8)      | snake_case para funções e variáveis, PascalCase para classes | Use nomes significativos       |
| JavaScript (Airbnb) | camelCase para variáveis e funções, PascalCase para classes  | Evite abreviações              |
| PowerShell          | PascalCase para funções e cmdlets, camelCase para variáveis  | Use Verb-Noun para cmdlets     |
| Bash (Google's Guide)| snake_case para funções e variáveis                          | Evite caracteres especiais e espaços |

# Links para as guias de estilo

GO: Guia de Estilo do Go (Effective Go), disponível em: 
    'https://golang.org/doc/effective_go.html'

PYTHON: PEP 8 - Guia de Estilo para Código Python, disponível em: 
    'https://www.python.org/dev/peps/pep-0008/'

JAVSCRIPT: Airbnb JavaScript Style Guide, disponível em: 
    'https://github.com/airbnb/javascript'

POWERSHELL: Guia de Melhores Práticas para o PowerShell, disponível em: 
    'https://github.com/PoshCode/PowerShellPracticeAndStyle'

BASH: Google's Shell Style Guide, disponível em:
    'https://google.github.io/styleguide/shellguide.html'