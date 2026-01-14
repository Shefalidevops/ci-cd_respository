# FastAPI Todo CI

A small FastAPI Todo API with automated tests and a GitHub Actions CI pipeline.  
This repository is part of my DevOps/Platform Engineering portfolio, showing how I design a Python service, containerize it, and validate it continuously with CI.

GitHub repo: https://github.com/Shefalidevops/ci-cd_respository

---

## Features

- FastAPI REST API with:
  - `GET /health` health check.
  - CRUD endpoints for Todo items (`/todos`).
- Pydantic v2 models for request/response validation.
- Automated tests using `pytest` and `TestClient`.
- GitHub Actions workflow that:
  - Sets up Python.
  - Installs dependencies from `requirements.txt`.
  - Runs the test suite (`pytest -vv`) on every push and pull request.
- Dockerfile to build a runnable container image of the API.

---

## Tech stack

- **Language:** Python 3.11  
- **Framework:** FastAPI + Starlette  
- **Data store:** In‑memory list (no external DB, ideal for CI)  
- **Testing:** `pytest`, `httpx`, FastAPI `TestClient`  
- **Deps:** `requirements.txt`  
- **CI:** GitHub Actions  
- **Container:** Docker

---

## Local development

### 1. Clone the repository

```bash
git clone https://github.com/Shefalidevops/ci-cd_respository.git
cd ci-cd_respository
2. Create and activate a virtual environment
bash
python -m venv .venv

# Windows (PowerShell / cmd)
.venv\Scripts\activate

# Git Bash / WSL / macOS / Linux
# source .venv/bin/activate
3. Install dependencies
bash
python -m pip install --upgrade pip
pip install -r requirements.txt
4. Run the API
bash
uvicorn app.main:app --reload
Then open:

Swagger UI: http://127.0.0.1:8000/docs

Health check: http://127.0.0.1:8000/health

API overview
Health
GET /health

Response: {"status": "ok"}

Todos (in‑memory)
GET /todos – List all todos.

POST /todos – Create a todo.

Example request body:

json
{
  "title": "Test todo",
  "description": "demo",
  "completed": false
}
GET /todos/{id} – Get a todo by id.

PUT /todos/{id} – Update an existing todo.

DELETE /todos/{id} – Delete a todo.

The store is in memory, so data resets on every server restart. This keeps the project simple and fully self‑contained for CI.

Running tests
bash
pytest -vv
The tests use FastAPI’s TestClient to verify:

The /health endpoint.

A full create‑and‑get flow for /todos.

GitHub Actions CI
This repo includes a workflow at .github/workflows/ci.yml.

On every push and pull request to main, the pipeline:

Checks out the repository:

text
- uses: actions/checkout@v4
Sets up Python:

text
- uses: actions/setup-python@v5
  with:
    python-version: "3.11"
Installs dependencies:

text
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
Runs tests:

text
- name: Run tests
  run: pytest -vv
The goal is that whatever passes on a local virtual environment also passes on the GitHub Actions runner.

Docker
You can build and run the app in Docker:

bash
# Build image
docker build -t fastapi-todo-ci .

# Run container
docker run -p 8000:8000 fastapi-todo-ci
This uses the Dockerfile in the project root to create an image that starts uvicorn app.main:app.

What this project demonstrates (DevOps focus)
This project is intentionally small but designed to show real DevOps/Platform Engineer skills:

Designing a simple, testable FastAPI service.

Structuring a Python project with clear separation between app/ and tests/.

Managing virtual environments and dependencies with requirements.txt.

Writing API tests and making them pass on both local and CI environments.

Debugging CI issues such as:

- Virtualenv path problems.

- ModuleNotFoundError for the application package.

- Missing test dependencies (httpx) on the CI runner.

- Pydantic v2 API changes (e.g., model_dump()).

Future enhancements (planned):

- Add linting and type‑checking (ruff/flake8, black, mypy) as additional CI steps.

- Build and push Docker images to GitHub Container Registry.

- Deploy the container to a cloud/Kubernetes environment with a small CD workflow.



