# DevOps Capstone Project

[![Build Status](https://github.com/FarooqShabbir/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/FarooqShabbir/devops-capstone-project/actions)

## Customer Accounts Microservice

This project is the DevOps Capstone for the IBM DevOps and Software Engineering Professional Certificate. It implements a RESTful Customer Accounts microservice built with Flask, containerized with Docker, and deployed to Kubernetes via a Tekton CD pipeline.

## Features

- RESTful CRUD API for customer accounts
- SQLAlchemy ORM with PostgreSQL/SQLite
- Automated tests with 95%+ coverage (nosetests)
- Linting with Flake8 and Pylint
- Continuous Integration via GitHub Actions
- Security headers via Flask-Talisman, CORS via Flask-CORS
- Docker containerization
- Kubernetes deployment manifests
- Tekton CD pipeline

## API Endpoints

| Method | Endpoint           | Description                |
|--------|--------------------|----------------------------|
| GET    | `/`                | Service info               |
| GET    | `/health`          | Health check               |
| POST   | `/accounts`        | Create an account          |
| GET    | `/accounts`        | List all accounts          |
| GET    | `/accounts/<id>`   | Read an account            |
| PUT    | `/accounts/<id>`   | Update an account          |
| DELETE | `/accounts/<id>`   | Delete an account          |

## Running Locally

```bash
pip install -r requirements.txt
export FLASK_APP=wsgi:app
flask run
```

## License

Licensed under the Apache License 2.0.
