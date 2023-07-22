# Descrição da solução de análise
Para desenvolver nossa plataforma de análise de dados, utilizamos arquitetura de microservices em monorepo e a utilização do padrão Ports and Adapters. Em uma arquitetura com a abordagem Ports and Adapters (também conhecida como Hexagonal Architecture), a camada de domínio é independente das tecnologias utilizadas para persistir os dados, como bancos de dados, APIs REST, entre outros. Essa independência é alcançada por meio de interfaces (também chamadas de portas) que definem como a camada de domínio se comunica com a camada de persistência.

### Proposta de Valor
Nossa plataforma promove geração de informação por meio da interação entre usuários, especialistas de domínio e analistas de negócio. Os usuários descrevem suas necessidades de informação e demandam as análises, para isso essas necessidades serão descritas na forma de requisições para conduzir os levantamentos e a prospecção de dados para gerar informação sobre temas específicos. Cada análise é composta por um processo específico de levantamento, processamento e análise de dados montado pelo equipe de analistas de negócio, permitindo assim que os usuários escolham dentre uma lista de processos modelados previamente para solicitar uma análise existente, ou para dar início a um novo pipeline de análise. Cada pipeline de análise é composto das várias fases de levantamento de dados, pré-processamento, escolha dos algoritmos de análise, ingestão de dados, processamento, análise e apresentação de resultados na forma de relatórios interativos capazes de atender às necessidades de informação requisitadas pelo usuário. 

### Estrutura do Repositório Monorepo

Ao trabalharmos com um monorepo, temos a flexibilidade de organizar o projeto de maneira que melhor atender uma gama de necessidades de informação, permitindo agregarmos módulos semelhantes para compor distintos relatórios e pipelines de geração de informação. A estrutura de pastas principais do monorepo segue a seguinte lógica:

**api**: A interface da API será desenvolvida em GoLang para lidar com alto volume de solicitações utilizando de multiprocessamento nativo para melhor performance.

**services**: Este diretório contém os serviços, cada um numa subpasta. Teríamos, por exemplo, duas subpastas: go-services para os serviços de GoLang que lidam com multiprocessamento e flask-services para os serviços Flask que lidam com análises mais simples. Os serviços também serão organizados por tipo de análise.

a. go-services: Aqui estarão os serviços escritos em GoLang que realizam tarefas de multiprocessamento. Cada serviço deve ter o seu próprio Dockerfile para que possa ser executado em um contêiner separado, garantindo assim a escalabilidade e a robustez. Dentro deste diretório temos os subdiretórios para cada tipo de análise, por exemplo: `go-services/prospect_specialist`, `go-services/maturity_analisys`, etc.

b. flask-services: Aqui estão os microserviços Flask que lidam com análises mais simples. Semelhante aos serviços GoLang, organizamos diferentes análises em subdiretórios separados. Cada um desses também deve ter o seu próprio Dockerfile para a execução em um contêiner separado.

**pipelines**: Este diretório contém os pipelines de análise que foram criados pelos analistas de negócio. Cada pipeline será armazenado em um subdiretório que contém um conjunto de scripts e configurações específicas para a análise em questão.

**data**: Este diretório é responsável pela coleta e manipulação de dados, possivelmente escrito em Python, como mencionado anteriormente.

**web**: Este diretório mantém o código para a visualização dos relatórios, utilizando D3.js para gráficos interativos.

**common**: Este diretório contém código comum a todos os serviços.

**test**: Este diretório contém todos os testes automatizados para cada serviço, bem como para a API e a camada de visualização.

- Os arquivos de configuração, como `.gitignore`, `requirements.txt`, `go.mod`, `package.json`, etc., estão na raiz do monorepo.

Para cada nova análise que é adicionada ao sistema, um novo subdiretório é criado em `go-services` ou `flask-services` (dependendo da complexidade e requisitos específicos da análise, como a fonte de dados). Para cada análise estruturada modelada um novo pipeline é adicionado ao diretório `pipelines`. Esta estrutura permite uma separação clara das diferentes análises, tornando o sistema fácil de navegar e manter. A adição de novas análises se torna uma questão de adicionar novos diretórios e pipelines, sem afetar as análises existentes. Além disso, esta estrutura apoia a implementação de práticas DevOps, como a Integração Contínua/Entrega Contínua (CI/CD). Por exemplo, você pode configurar a ferramenta de CI/CD para executar testes específicos e implantar serviços com base nas mudanças que ocorrem em determinados diretórios.

### Fluxo geral de Operação da Aplicação

O usuário envia um pedido de análise através da API, contendo o objetivo que deseja da análise e a especificação das palavras-chave para levantamento de dados.

A API recebe a solicitação, valida-a e encaminha-a para o serviço adequado na pasta services dependendo do tipo de análise solicitada.

O serviço executa o algoritmo de análise determinado no pipeline que irá produzir a informação com base nos resultados dos algoritmos mediante entrada dos dados coletados e retornados pelo módulo data. Como temos dois tipos distintos de serviços: os de GoLang e os Flask. A API irá encaminhar as solicitações para o serviço apropriado dependendo do tipo de análise requerida no pipeline em uso.

O resultado da análise é retornado para a API, que o formata adequadamente em um relatório antes de enviar a resposta para o usuário.

Para a visualização dos relatórios, os dados processados são enviados ao módulo web, que usa LaTeX quando o relatório for entregue na forma de documento, ou quando a entrega for por relatório interativo em página HTML, será utilizada biblioteca D3.js para gerar gráficos interativos e visuais que comporão o relatório.


### Orquestração de Serviços

Uma vez que estamos lidando com múltiplos serviços, cada um possivelmente em um contêiner separado, implementaremos uma solução de orquestração de contêineres com o Kubernetes para gerenciar os contêineres e facilitar a comunicação entre eles. Isso permitirá um balanceamento de carga eficiente e uma rápida escalabilidade, garantindo um tempo de resposta rápido mesmo durante picos de demanda.


### Entrevistas com Usuários Especialistas

Para garantir que a aplicação atenda às necessidades dos usuários, faremos entrevistas com os usuários especialistas. Essas entrevistas nos ajudarão a entender os requisitos e as expectativas dos usuários, bem como a definir os dados necessários para a análise. As informações coletadas serão usadas para orientar o desenvolvimento dos algoritmos de análise e a estruturação dos relatórios.

### Considerações de Testes

Testes automatizados devem ser implementados para garantir a qualidade e a robustez da aplicação. Testes unitários devem ser escritos para cada serviço, bem como testes de integração para garantir que todos os serviços e a API trabalhem juntos como esperado. Além disso, devido à coexistência de serviços GoLang e Flask, os testes de integração serão ainda mais importantes para garantir que todos os componentes da aplicação estejam funcionando harmoniosamente juntos.

Lembrando que cada serviço deverá ser implementado pensando na independência, ou seja, cada serviço deve ser autocontido e responsável por sua própria lógica e persistência, se necessário. Esse design de solução mantém os princípios do SOLID, a separação de responsabilidades, o encapsulamento, e também atende aos requisitos funcionais e não funcionais da aplicação. Isso permitirá um ambiente de desenvolvimento coeso e escalável que pode crescer e evoluir com as necessidades dos usuários e da empresa.


# Adaptadores
Nossa estrutura de monorepo pode facilmente acomodar as necessidades de diferentes bancos de dados e cache. Vamos adicionar novos diretórios em src/adapters para os respectivos bancos de dados e serviços de cache que planejamos usar. Isso também está alinhado com o princípio Ports and Adapters, já que os bancos de dados e o cache são partes externas ao nosso domínio de aplicação.

MongoDB: No diretório mongodb, você pode armazenar todos os códigos relacionados ao gerenciamento de conexões do MongoDB, consultas e outras operações relacionadas ao MongoDB.

Neo4j: Semelhante ao MongoDB, o diretório neo4j pode conter todos os códigos para gerenciar conexões Neo4j, consultas Cypher, operações com a biblioteca GDS do Neo4j e outras operações relacionadas ao Neo4j.

Redis: No diretório redis, você pode colocar todos os códigos relacionados à gestão do Redis, incluindo a criação de cache, invalidação de cache, consulta e outras operações.

O código em cada um desses diretórios é usado pelos serviços na pasta services para interagir com o respectivo banco de dados ou serviço de cache. Por exemplo, o serviço prospect_specialist pode usa o código em mongodb para consultar e armazenar dados no MongoDB.

Todos os segredos e credenciais relacionados aos bancos de dados e cache devem ser gerenciados de maneira segura e injetados como variáveis de ambiente, em vez de serem armazenados diretamente no repositório.

# Iniciando a desenvolvimento
### Criar o repositório no GitHub pela máquina local

Inicie o repositório Git e crie o repositório GitHub: 
    Dentro do diretório principal /text_to_bpmn, inicie um novo repositório Git com git init. 

Crie um novo repositório GitHub através do site do GitHub. 
    Vincule seu repositório local ao repositório GitHub com git remote add origin [URL do repositório GitHub].

Fazer push para o GitHub: 
    Adicione todos os arquivos ao repositório Git com git add ., faça um commit com git commit -m "Initial commit" e então faça push para o GitHub com git push -u origin master.


### Guias de estilo para nomear arquivos e artefatos de código

Ser bem compreensível e fácil de ler é requisito para boa comunicação em qualquer linguagem humana, em software não é diferente. Saber como nomear os artefatos de software e em qual estilo escrever este nome escolhido é essencial para escrever bons códigos. Quanto ao estilo o uso das maiúsculas e minúsculas e do caractere separador entre palavras é que define a legibilidade e fácil entendimento, popularmente temos o snake_case (todas as letras minúsculas com palavras separadas por underscores), camelCase, PascalCase e o MixedCase, cada alternativa tem sua popularidade dentre de alguma das cominidades de desenvolvimento.

Já no que diz repeito à execução do código pelos computadores, basicamente, há dois níveis de visibilidade dos artefatos de software com relação a onde estão armazenados na estrutura dos arquivos de pacotes e módulos, há artefatos "exportados" e "não exportados" no que se refere à visibilidade dos membros de um pacote, como funções, tipos e variáveis. 

No caso da linguagem Go, por exemplo, um membro de um pacote é exportado se seu nome começa com uma letra maiúscula. Membros exportados são acessíveis fora do pacote em que são definidos. Por exemplo, se você define uma função `Print()` em um pacote, você pode chamá-la de outro pacote. Por outro lado, os membros não exportados começam com uma letra minúscula e só podem ser acessados dentro do mesmo pacote onde são definidos. Se você tem uma função `print()` em um pacote, você não pode chamá-la de outro pacote.

A razão para essa distinção é proporcionar o encapsulamento de dados, que é um princípio fundamental da programação orientada a objetos. Ele permite que você oculte os detalhes de implementação de um pacote e exponha apenas uma interface pública, o que pode tornar o código mais fácil de usar e manter.

| Linguagem/Convenção     | Estilo de Case                                                     | Nomeação de Artefatos |
|-------------------------|-------------------------------------------------------------------|-----------------------|
| Go (Effective Go)       | MixedCase para exportados, camelCase para não exportados            | Conciso, mnemônico    |
| Python (PEP 8)          | snake_case para funções e variáveis, PascalCase para classes        | Use nomes significativos |
| JavaScript (Airbnb)     | camelCase para variáveis e funções, PascalCase para classes         | Evite abreviações     |
| Clojure (Community conventions) | kebab-case para funções e variáveis                            | Use nomes descritivos |
| Julia (Julia Style Guide)       | lower_case para variáveis e funções                           | Use nomes significativos |
| PowerShell (Best Practice Guide) | PascalCase para funções e cmdlets, camelCase para variáveis | Use Verb-Noun para cmdlets |
| Bash (Google's Guide)   | snake_case para funções e variáveis                                 | Evite caracteres especiais e espaços |


### Links para guias de estilo populares em suas comunidades

GO: Guia de Estilo do Go (Effective Go), disponível em: 
    'https://golang.org/doc/effective_go.html'

PYTHON: PEP 8 - Guia de Estilo para Código Python, disponível em: 
    'https://www.python.org/dev/peps/pep-0008/'

JULIA: Guia de estilo da documentação, disponível em:
    'https://docs.julialang.org/en/v1/manual/style-guide/'

JAVASCRIPT: Airbnb JavaScript Style Guide, disponível em: 
    'https://github.com/airbnb/javascript'

CLOJURE: Clojure Style Guide, disponível em: 
    'https://clojuredocs.org/examples-styleguide'

POWERSHELL: Guia de Melhores Práticas para o PowerShell, disponível em: 
    'https://github.com/PoshCode/PowerShellPracticeAndStyle'

BASH: Google's Shell Style Guide, disponível em:
    'https://google.github.io/styleguide/shellguide.html'