# UNINTER AI

**Assistente de estudos com inteligência artificial e automação para o ambiente acadêmico UNIVIRTUS.**

O UNINTER AI é um projeto pessoal desenvolvido com Python e Django, com o objetivo de facilitar a organização e a análise de materiais acadêmicos por meio de inteligência artificial e automação de navegador.

A proposta é integrar diferentes tecnologias para auxiliar no acesso aos conteúdos das disciplinas e tornar o processo de estudo mais organizado.

## Objetivos do projeto

- Facilitar o acesso aos materiais acadêmicos.
- Utilizar inteligência artificial para auxiliar na compreensão dos conteúdos.
- Automatizar etapas de navegação no ambiente acadêmico.
- Centralizar recursos de estudo em uma única aplicação.

## Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Linguagem principal |
| Django | Estrutura da aplicação web |
| HTML e CSS | Interface e apresentação |
| JavaScript | Interações da interface |
| Google Gemini API | Integração com inteligência artificial |
| Playwright | Automação e interação com o navegador |
| SQLite | Banco de dados durante o desenvolvimento |
| Git e GitHub | Versionamento e organização do código |

## Funcionalidades desenvolvidas

- Estrutura inicial da aplicação web com Django.
- Sistema de autenticação de usuários.
- Painel principal para centralizar os recursos do projeto.
- Integração com a API do Google Gemini.
- Endpoint para envio de perguntas à inteligência artificial.
- Integração inicial com Playwright para automação do navegador.
- Configuração de ambiente e variáveis de acesso por arquivo `.env`.

## Em desenvolvimento

- Aprimoramento da navegação automatizada no UNIVIRTUS.
- Identificação e leitura dos materiais das disciplinas.
- Extração e organização de conteúdos textuais.
- Integração entre os materiais acadêmicos e a inteligência artificial.
- Expansão dos recursos de organização dos estudos.

## Estrutura do projeto

```text
UNINTER-AI/
│
├── academics/       # Recursos relacionados aos materiais acadêmicos
├── assistant/      # Integração com inteligência artificial
├── config/         # Configurações do Django
├── dashboard/      # Painel principal da aplicação
├── integrations/   # Integrações e automação do navegador
│
├── manage.py
├── .gitignore
└── README.md
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Thierrx/UNINTER-AI.git
cd UNINTER-AI
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

No Windows (CMD):

```cmd
venv\Scripts\activate.bat
```

### 3. Instalar as dependências

```bash
pip install django python-dotenv google-genai playwright pypdf
```

### 4. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DJANGO_SECRET_KEY=sua_chave_secreta
GEMINI_API_KEY=sua_chave_da_api
```

As chaves devem ser obtidas individualmente e não devem ser compartilhadas ou enviadas ao GitHub.

### 5. Executar as migrações

```bash
python manage.py migrate
```

### 6. Iniciar o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em:

`http://127.0.0.1:8000/`

## Sobre o desenvolvimento

Este projeto está em desenvolvimento e faz parte dos meus estudos em Engenharia de Software.

Durante sua construção, tenho trabalhado com desenvolvimento web, integração de APIs, automação de navegador, organização de código e resolução de problemas.

O objetivo é desenvolver uma aplicação funcional, evoluindo gradualmente sua estrutura e suas funcionalidades.

---

**Status:** Em desenvolvimento  
**Linguagem principal:** Python  
**Repositório:** [Thierrx/UNINTER-AI](https://github.com/Thierrx/UNINTER-AI)