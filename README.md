# 📚 Bookstores

Sistema de gerenciamento de livrarias desenvolvido com Django, PostgreSQL e integração contínua via GitHub Actions. Este projeto serve como base para estudos de back-end com foco em APIs REST, testes automatizados e boas práticas de desenvolvimento.

## 🔧 Tecnologias Utilizadas

- Python 3.13
- Django 4.x
- PostgreSQL 16
- Poetry
- Docker & Docker Compose
- GitHub Actions (CI)
- Wemake Python Styleguide

## ⚙️ Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/MateusMalves/bookstores.git
cd bookstores
```

### 2. Configure o ambiente virtual com Poetry

```bash
poetry install
poetry shell
```

### 3. Copie o arquivo `.env`

```bash
cp env.dev .env
```

> O arquivo `.env.dev` já contém variáveis de ambiente de desenvolvimento como `DEBUG`, `SECRET_KEY`, e informações do banco de dados.

### 4. Suba o banco de dados com Docker

```bash
docker-compose up -d
```

### 5. Rode as migrações e o servidor local

```bash
python manage.py migrate
python manage.py runserver
```

Acesse em: [http://localhost:8000](http://localhost:8000)

## 🧪 Rodando os testes

Execute:

```bash
python manage.py test
```

Ou, se estiver usando Poetry:

```bash
poetry run python manage.py test
```

## 🚀 Integração Contínua (CI)

Este projeto está integrado com o GitHub Actions. A pipeline de testes é acionada automaticamente em Pull Requests para a branch `main`, garantindo a qualidade e padronização do código.

## ✅ Estilo de Código

Utilizamos o [wemake-python-styleguide](https://wemake-python-stylegui.de) para garantir qualidade de código. O linting é aplicado automaticamente nos PRs.

## 📁 Estrutura do Projeto

```
bookstores/
├── .github/workflows         # Pipelines do GitHub Actions
├── bookstore/                # Configurações globais do Django
├── order/                    # App responsável pelos pedidos
├── product/                  # App responsável pelos produtos
├── env.dev                   # Variáveis de ambiente
├── docker-compose.yml        # Banco de dados PostgreSQL
├── manage.py                 # Entry point do Django
```

## 🚀 Deploy no Heroku (via CLI)

Certifique-se de ter o Heroku CLI instalado:  
👉 https://devcenter.heroku.com/articles/heroku-cli

### 1. Faça login no Heroku

```bash
heroku login
```

### 2. Crie o app no Heroku

```bash
heroku create nome-do-seu-app
```

### 3. Adicione o PostgreSQL como add-on

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

### 4. Configure as variáveis de ambiente

```bash
heroku config:set \
  DJANGO_SECRET_KEY='sua-secret-key' \
  DJANGO_ALLOWED_HOSTS='nome-do-seu-app.herokuapp.com' \
  DEBUG=0
```

### 5. Faça o deploy

```bash
git push heroku main
```

> Se sua branch principal não se chama `main`, use o nome correto no lugar.

### 6. Rode as migrações no servidor

```bash
heroku run python manage.py migrate
```

### 7. Acesse sua aplicação

Abra no navegador:

```
https://nome-do-seu-app.herokuapp.com
```

## 👤 Autor

**Mateus Malves**  
Desenvolvedor Fullstack com foco em Python, Django e Inteligência Artificial.  
📫 Contato: [LinkedIn](https://www.linkedin.com/in/devmateusmalves)

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
