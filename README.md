WorkoutAPI: Desenvolva uma API de Crossfit com FastAPI e PostgreSQL
Este projeto, WorkoutAPI, é uma API de competição de Crossfit desenvolvida para ser um guia prático no uso do FastAPI, um framework Python moderno e de alta performance. Unindo minha paixão por codificar e treinar, criei uma API simplificada, mas completa o suficiente para você dominar os conceitos essenciais do FastAPI.

Por que FastAPI?
O FastAPI é um framework web Python moderno, rápido e fácil de usar, ideal para construir APIs com alta performance. Sua principal característica é a utilização de type hints do Python 3.6+ para garantir validação de dados, serialização, e documentação automática (OpenAPI/Swagger UI).

O Poder do Código Assíncrono (async)
Neste projeto, utilizamos código assíncrono, o que permite que a API lide com múltiplas operações simultaneamente, sem bloquear a execução enquanto espera por respostas de I/O (como chamadas de banco de dados). Isso é crucial para construir APIs responsivas e escaláveis.

Estrutura do Projeto: WorkoutAPI
A WorkoutAPI é uma API de Crossfit com poucas tabelas, focando no essencial para um aprendizado eficaz do FastAPI. Ela demonstra como integrar e usar as principais ferramentas do ecossistema Python para desenvolvimento de APIs.

Stack Tecnológica
A API foi construída com:

FastAPI: O framework web principal para a API.

SQLAlchemy: Um poderoso ORM (Object-Relational Mapper) para interagir com o banco de dados.

Alembic: Uma ferramenta para gerenciar migrações de banco de dados, garantindo que o esquema do seu DB evolua de forma controlada.

Pydantic: Utilizado para validação de dados e serialização, aproveitando os type hints do Python.

PostgreSQL: O banco de dados relacional robusto e amplamente utilizado, rodando via Docker para facilitar a configuração e o gerenciamento.

Como Executar o Projeto
Siga estes passos para colocar a WorkoutAPI em funcionamento na sua máquina:

Configuração do Ambiente Virtual (Pyenv recomendado):
Recomendo usar o pyenv para gerenciar as versões do Python.

Bash

pyenv virtualenv 3.11.4 workoutapi
pyenv activate workoutapi
pip install -r requirements.txt
Subir o Banco de Dados (Docker Compose):
Certifique-se de ter o Docker e o Docker Compose instalados.

Bash

make run-docker
Para conectar-se diretamente ao PostgreSQL, use as credenciais: host: localhost, porta: 5433, usuário: workout, senha: workout, banco de dados: workout.

Criar Migrações (Alembic):
Para gerar uma nova migração de banco de dados:

Bash

make create-migrations d="nome_da_migration"
Aplicar Migrações (Banco de Dados):
Para criar as tabelas no banco de dados:

Bash

make run-migrations
Iniciar a API:

Bash

make run
Após iniciar, acesse a documentação interativa da API em: http://127.0.0.1:8000/docs

Desafio Final (Para Aprimorar suas Habilidades)
Este projeto também propõe alguns desafios para você aprofundar seus conhecimentos:

Query Parameters nos Endpoints:

Atleta: Adicione filtros por nome e cpf.

Customizar Respostas de Endpoints (GET all):

Atleta: Altere o retorno para incluir nome, centro_treinamento e categoria.

Manipulação de Exceção de Integridade:

Capture sqlalchemy.exc.IntegrityError e retorne a mensagem customizada: "Já existe um atleta cadastrado com o cpf: x" com status_code: 303.

Paginação:

Implemente paginação usando a biblioteca fastapi-pagination com limit e offset.
