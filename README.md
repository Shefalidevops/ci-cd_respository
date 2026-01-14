# FastAPI Todo CI

A small FastAPI Todo API with automated tests and a GitHub Actions CI pipeline.  
This project is designed as a DevOps/Platform Engineer portfolio piece to demonstrate setting up a Python service, testing it, and validating it with CI on every push.

---

## Features

- FastAPI REST API with:
  - `GET /health` health check.
  - CRUD endpoints for Todo items (`/todos`).  
- Pydantic v2 models for request/response validation.
- Automated tests using `pytest` and `TestClient`. [web:46][web:144]
- GitHub Actions workflow that:
  - Sets up Python.
  - Installs dependencies from `requirements.txt`.
  - Runs the test suite (`pytest -vv`) on every push and pull request. [web:23][web:173]
- Dockerfile for containerizing the app.

---

## Tech stack

- **Language:** Python 3.11
- **Framework:** FastAPI + Starlette [web:137][web:172]
- **Data store:** In‑memory list (no external DB, ideal for CI examples)
- **Testing:** `pytest`, `httpx`/`TestClient` [web:46][web:144]
- **Packaging/deps:** `requirements.txt`
- **CI:** GitHub Actions
- **Container:** Docker

---

## Local development

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/fastapi-todo-ci.git
cd fastapi-todo-ci
