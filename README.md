# 📋 TaskFlow

> ✅ **Status do Projeto:** Concluído

> **Sistema Web de Gerenciamento Ágil de Tarefas**

Projeto desenvolvido para a disciplina de **Engenharia de Software**, com o objetivo de aplicar na prática conceitos de desenvolvimento de software, versionamento de código, metodologias ágeis, testes automatizados, integração contínua e modelagem UML utilizando Python e Flask.

---

# 📖 Sobre o Projeto

A empresa fictícia **TechFlow Solutions** foi contratada pela empresa **FastRoute Logistics** para desenvolver um sistema web destinado ao gerenciamento de tarefas.

O sistema permite cadastrar, visualizar, editar, excluir e organizar tarefas de maneira simples e intuitiva, auxiliando no acompanhamento das atividades por meio de um Dashboard com indicadores e recursos de gerenciamento.

Durante o desenvolvimento foram aplicados diversos conceitos estudados na disciplina de Engenharia de Software, incluindo:

- Desenvolvimento incremental;
- Metodologia Ágil Kanban;
- Controle de versão utilizando Git;
- Hospedagem do projeto no GitHub;
- Testes automatizados utilizando Pytest;
- Integração Contínua utilizando GitHub Actions;
- Modelagem UML;
- Documentação técnica.

---

# 🎯 Objetivo

Desenvolver uma aplicação web para gerenciamento de tarefas aplicando os conceitos estudados durante a disciplina de Engenharia de Software, desde o planejamento até a entrega do software.

O projeto demonstra a utilização integrada de metodologias ágeis, versionamento, testes automatizados, documentação técnica e integração contínua.

---

# 🚀 Funcionalidades

O sistema possui as seguintes funcionalidades:

- 📋 Listagem de tarefas;
- ➕ Cadastro de tarefas;
- ✏️ Edição de tarefas;
- 🗑️ Exclusão de tarefas;
- 🚦 Controle de prioridade;
- 📌 Controle de status;
- 📊 Dashboard com estatísticas das tarefas;
- 🔍 Filtro de tarefas por prioridade *(implementado como mudança de escopo durante o desenvolvimento).*

---

# 🛠 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python 3 | Linguagem principal |
| Flask | Framework Web |
| SQLite | Banco de Dados |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização |
| Bootstrap 5 | Interface responsiva |
| Pytest | Testes automatizados |
| Git | Controle de versão |
| GitHub | Repositório do projeto |
| GitHub Actions | Integração Contínua (CI) |

---

# 📂 Estrutura do Projeto

```text
taskflow-project/

├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   └── uml/
├── instance/
├── src/
├── static/
├── templates/
├── tests/
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Descrição da Estrutura

| Pasta / Arquivo | Finalidade |
|-----------------|------------|
| .github/workflows | Configuração do GitHub Actions |
| docs/uml | Diagramas UML do projeto |
| instance | Banco de dados SQLite |
| src | Código-fonte da aplicação |
| templates | Páginas HTML |
| static | Arquivos estáticos |
| tests | Testes automatizados |
| app.py | Inicialização da aplicação |
| config.py | Configurações do projeto |
| requirements.txt | Dependências do projeto |

---

# ⚙️ Como executar o projeto

## Pré-requisitos

Para executar o projeto é necessário possuir instalado:

- Python 3.11 ou superior;
- Git;
- Pip (gerenciador de pacotes do Python).

Recomenda-se utilizar o Visual Studio Code ou outro editor de preferência.

---

## 1. Clonar o repositório

Abra um terminal e execute:

```bash
git clone https://github.com/thl8022/taskflow-project.git
```

---

## 2. Acessar a pasta do projeto

```bash
cd taskflow-project
```

---

## 3. Criar o ambiente virtual

Windows:

```bash
python -m venv venv
```

Será criada uma pasta chamada **venv**, responsável por isolar as dependências da aplicação.

---

## 4. Ativar o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Após ativado, o terminal deverá apresentar algo semelhante a:

```text
(venv) PS C:\Users\Usuario\taskflow-project>
```

---

## 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

Todas as bibliotecas necessárias serão instaladas automaticamente.

---

## 6. Executar a aplicação

```bash
python app.py
```

Na primeira execução será criado automaticamente o banco de dados SQLite na pasta **instance/**.

---

## 7. Acessar o sistema

Abra o navegador e acesse:

```
http://127.0.0.1:5000
```

A partir da página inicial será possível:

- acessar o Dashboard;
- cadastrar tarefas;
- editar tarefas;
- excluir tarefas;
- alterar prioridade;
- alterar status;
- filtrar tarefas por prioridade.

---

# 🧪 Testes Automatizados

O projeto utiliza **Pytest** para validar o funcionamento das principais funcionalidades da aplicação.

Os testes verificam:

- Página inicial;
- Dashboard;
- Página de cadastro de tarefas;
- Cadastro de tarefas;
- Exclusão de tarefas.

Para executar todos os testes:

```bash
python -m pytest
```

Todos os testes também são executados automaticamente pelo GitHub Actions sempre que um **push** ou **pull request** é realizado na branch principal.

---

# 🔄 Integração Contínua

O projeto utiliza **GitHub Actions** para automatizar a execução dos testes.

A cada alteração enviada para o repositório, o workflow executa automaticamente:

- instalação das dependências;
- execução dos testes automatizados;
- validação da aplicação.

Esse processo garante maior confiabilidade e estabilidade durante o desenvolvimento.

---

# 📋 Metodologia Utilizada

O desenvolvimento foi conduzido utilizando a metodologia ágil **Kanban**, por meio do **GitHub Projects**.

As atividades foram organizadas nas colunas:

- A Fazer;
- Em Progresso;
- Concluído.

Cada funcionalidade do sistema foi registrada, acompanhada e atualizada conforme a evolução do projeto.

---

# 📈 Roadmap

- [x] Estrutura inicial do projeto
- [x] Configuração do Flask
- [x] Banco de Dados SQLite
- [x] CRUD de Tarefas
- [x] Dashboard
- [x] Interface Web
- [x] Testes Automatizados
- [x] GitHub Actions
- [x] Diagramas UML
- [x] Documentação Técnica

---

# 📚 Diagramas UML

Os diagramas UML encontram-se na pasta:

```text
docs/uml/
```

Diagramas desenvolvidos:

- Diagrama de Casos de Uso;
- Diagrama de Classes.

---

# 📌 Mudança de Escopo

Durante o desenvolvimento do projeto, o cliente identificou a necessidade de facilitar a localização das tarefas cadastradas.

Como resposta a essa solicitação, foi implementado um **filtro de tarefas por prioridade**, permitindo ao usuário visualizar apenas as tarefas pertencentes à prioridade selecionada.

Essa funcionalidade foi registrada no Kanban do projeto, implementada na aplicação, documentada no histórico de commits e validada por meio dos testes automatizados.

---

# 📌 Observações

- O banco de dados SQLite é criado automaticamente na primeira execução da aplicação.
- O projeto utiliza integração contínua por meio do GitHub Actions.
- O gerenciamento das atividades foi realizado utilizando GitHub Projects (Kanban).
- A mudança de escopo foi implementada durante o desenvolvimento do projeto.
- O sistema foi desenvolvido exclusivamente para fins acadêmicos.

---

# 👨‍💻 Autor

**Thiago Lourenço**

Projeto desenvolvido para a disciplina de **Engenharia de Software**.

---

# 📄 Licença

Este projeto está licenciado sob a licença **MIT**.