# 📋 TaskFlow

Atualização de documentação para fins de entrega acadêmica.

> 🚧 **Status do Projeto:** Em desenvolvimento

> **Sistema Web de Gerenciamento Ágil de Tarefas**

Projeto desenvolvido para a disciplina de **Engenharia de Software**, com o objetivo de aplicar conceitos de desenvolvimento colaborativo, versionamento de código, metodologias ágeis, integração contínua e boas práticas de desenvolvimento utilizando Python e Flask.

---

## 📖 Sobre o Projeto

A **TechFlow Solutions** foi contratada pela empresa **FastRoute Logistics** para desenvolver um sistema web capaz de gerenciar tarefas de maneira simples, organizada e eficiente.

O sistema permitirá que usuários acompanhem suas atividades por meio de um painel intuitivo, podendo criar, editar, excluir e atualizar o status das tarefas.

Este projeto também tem como objetivo demonstrar a aplicação prática de conceitos de Engenharia de Software, como:

- Desenvolvimento incremental
- Metodologia Ágil (Kanban)
- Versionamento com Git e GitHub
- Testes automatizados
- Integração Contínua (GitHub Actions)
- Documentação técnica
- Diagramas UML

---

# 🚀 Funcionalidades

O sistema contará com as seguintes funcionalidades:

- 🔐 Login de usuário
- 📋 Listagem de tarefas
- ➕ Cadastro de tarefas
- ✏️ Edição de tarefas
- 🗑️ Exclusão de tarefas
- 🚦 Controle de prioridade
- 📌 Controle de status
- 🔍 Filtro de tarefas *(Mudança de Escopo)*

---

# 🛠 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python 3 | Linguagem principal |
| Flask | Framework Web |
| SQLite | Banco de Dados |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização |
| Bootstrap 5 | Interface Responsiva |
| Pytest | Testes Automatizados |
| Git | Controle de Versão |
| GitHub | Repositório |
| GitHub Actions | Integração Contínua |

---

# 📂 Estrutura do Projeto

```text
taskflow-project/

├── .github/
├── docs/
├── instance/
├── src/
├── static/
├── templates/
├── tests/
├── app.py
├── config.py
├── README.md
├── requirements.txt
└── LICENSE
```

---

# ⚙️ Como executar o projeto

## Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/taskflow-project.git
```

## Acesse a pasta

```bash
cd taskflow-project
```

## Crie o ambiente virtual

Windows

```bash
python -m venv venv
```

## Ative o ambiente

```bash
venv\Scripts\activate
```

## Instale as dependências

```bash
pip install -r requirements.txt
```

## Execute a aplicação

```bash
python app.py
```

---

# 🧪 Testes

Os testes automatizados serão desenvolvidos utilizando **Pytest**.

Para executá-los:

```bash
pytest
```

---

# 🔄 Integração Contínua

O projeto utilizará **GitHub Actions** para:

- Executar testes automaticamente;
- Validar commits;
- Garantir a estabilidade do projeto.

---

# 📋 Metodologia

O desenvolvimento seguirá a metodologia ágil **Kanban**, utilizando GitHub Projects para gerenciamento das atividades.

As principais etapas do projeto são:

- Planejamento
- Desenvolvimento
- Testes
- Documentação
- Entrega

---

# 📈 Roadmap

- [x] Estrutura inicial do projeto
- [ ] Configuração do Flask
- [ ] Banco de Dados
- [ ] CRUD de Tarefas
- [ ] Interface Web
- [ ] Testes Automatizados
- [ ] GitHub Actions
- [ ] Diagramas UML
- [ ] Documentação Final

---

# 📚 Diagramas

Os diagramas UML serão disponibilizados em:

```
docs/uml/
```

Incluindo:

- Diagrama de Casos de Uso
- Diagrama de Classes

---

# 📌 Mudança de Escopo

Durante o desenvolvimento, foi planejada uma evolução do sistema para permitir o **filtro de tarefas por prioridade**, simulando uma solicitação do cliente durante a execução do projeto.

Essa alteração será registrada no Kanban, no histórico de commits e na documentação do projeto.

---

# 👨‍💻 Autor

**Thiago Lourenço**

Projeto desenvolvido para fins acadêmicos na disciplina de Engenharia de Software.

---

# 📄 Licença

Este projeto está licenciado sob a licença **MIT**.