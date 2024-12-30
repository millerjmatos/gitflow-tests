# Python CI/CD Pipeline Example

A practical demonstration of a Continuous Integration and Continuous Delivery (CI/CD) pipeline using Python, automated testing, Docker, and GitHub Actions. This project showcases development best practices as part of my portfolio.

## Pipeline Overview

The pipeline automates:

1. **Testing**: Runs unit tests on feature, develop, and main branch pushes, plus pull requests to main. Generates test coverage reports with `pytest-cov` and checks code quality using `flake8`.

2. **Docker Build & Push**: Automatically builds and pushes Docker images to Docker Hub when changes are merged to `main`.

## Tech Stack

- Python
- pytest & pytest-cov
- flake8
- Docker
- GitHub Actions
- Gitflow

## Key Skills Demonstrated

- Python development and automated testing
- CI/CD pipeline configuration with GitHub Actions
- Docker containerization and registry management
- Version control and branch management with Git

## Links

- View the complete pipeline in the Actions tab
- Docker image: [docker.com/repository/docker/millerjmatos/gitflow-pipeline-test](https://hub.docker.com/repository/docker/millerjmatos/gitflow-pipeline-test)
