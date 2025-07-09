# 🏋️‍♂️ WorkoutAPI: Sua API de Crossfit com FastAPI e PostgreSQL!

![GitHub repo size](https://img.shields.io/github/repo-size/seu-usuario/workoutapi?color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/seu-usuario/workoutapi)
![GitHub license](https://img.shields.io/github/license/seu-usuario/workoutapi)
![Python version](https://img.shields.io/badge/python-3.11+-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue)

Seja bem-vindo(a) ao **WorkoutAPI**, um projeto _hands-on_ desenvolvido para desmistificar a criação de APIs robustas e de alta performance utilizando **FastAPI** e **PostgreSQL**.

Unindo a paixão por programar e por Crossfit, esta aplicação oferece uma experiência prática e moderna para quem quer dominar o desenvolvimento de APIs profissionais.

---

## 🚀 Por que FastAPI?

O [FastAPI](https://fastapi.tiangolo.com/) é um framework moderno para aplicações web em Python 3.6+ e oferece:

✅ **Alta Performance** com arquitetura assíncrona (baseada no Starlette)  
✅ **Fácil de Aprender** com excelente documentação e suporte a _autocompletion_  
✅ **Pronto para Produção** com validação de dados via Pydantic, OpenAPI e Swagger UI

---

## 🔄 Desvendando o Async

No coração do FastAPI está a **programação assíncrona**, que permite que sua API:

- Atenda múltiplas requisições simultaneamente
- Faça conexões paralelas com banco de dados ou APIs externas
- Mantenha-se rápida e responsiva mesmo sob carga pesada

---

## 🧱 O Projeto WorkoutAPI

A WorkoutAPI é uma API de competições de **Crossfit**, desenvolvida com um modelo de dados enxuto, mas funcional, ideal para quem quer:

- Aprender FastAPI na prática
- Dominar conexão com banco de dados usando SQLAlchemy + Alembic
- Trabalhar com boas práticas em projetos reais

---

## ⚙️ Stack Tecnológica

- **FastAPI** → Backend assíncrono moderno
- **SQLAlchemy** → ORM robusto para PostgreSQL
- **Alembic** → Controle de migrações
- **Pydantic** → Validação e serialização de dados
- **PostgreSQL** → Banco de dados relacional confiável
- **Docker** → Ambientes isolados para dev com `docker-compose`

---

## 🗺️ Diagrama de Arquitetura

```plaintext
+--------------------+        HTTP Requests        +----------------------+
|     Frontend /     | --------------------------> |      FastAPI App     |
|   API Client       |                             | (Rotas + Controllers)|
+--------------------+                             +----------+-----------+
                                                              |
                                                              v
                                                +--------------------------+
                                                |      SQLAlchemy ORM      |
                                                +--------------------------+
                                                              |
                                                              v
                                                +--------------------------+
                                                |      PostgreSQL DB       |
                                                +--------------------------+

