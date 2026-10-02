# Medhira Research — Backend

This folder contains the backend we are building for Medhira Research. It is also a hands-on learning project: understand each piece, then extend it.

## Current milestone: API is alive

The first version has two endpoints:

- `GET /` — welcome message and link to API documentation.
- `GET /health` — basic health check.

Interactive API documentation is generated automatically by FastAPI at `/docs`.

## Run locally (Ubuntu / WSL)

From the repository root:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open these addresses in your browser:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

Stop the server with `Ctrl + C`.

## Run tests

Keep the virtual environment active:

```bash
pytest -q
```

## Learning sequence

1. Python foundations: variables, types, conditions, loops, functions, collections, files, exceptions, modules and virtual environments.
2. HTTP and APIs: requests, responses, methods, status codes, JSON and REST.
3. FastAPI: routes, path/query parameters, request bodies and validation.
4. PostgreSQL: tables, SQL, relationships and migrations.
5. Authentication and authorisation: password hashing, tokens, sessions and privacy rules.
6. Testing and reliability: unit tests, integration tests, logging and error handling.
7. Docker and deployment: images, containers, environment variables and production configuration.
8. CI/CD and cloud: automated checks, deployment, AWS fundamentals, monitoring and security.

We will add member accounts and personal journal entries only after the foundations are understood. Private entries must be enforced by the backend and database permissions, not merely hidden in the frontend.

## Current limitations

This is a learning scaffold, not a production service. It has no database, accounts, authentication, persistence, privacy controls or cloud deployment yet. Do not put real private journal content or secrets into it.
