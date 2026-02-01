# C270 Calculator Application

A Flask-based Calculator application with CI/CD pipeline, Docker containerization, and Docker Swarm orchestration.

## 🚀 Features

- Flask web application with calculator functionality
- Automated testing with pytest
- Code quality checks with pylint
- CI/CD pipeline using GitHub Actions
- Docker containerization with smoke tests
- Docker Swarm orchestration for scaling and high availability
- Deployed to Render for production hosting

## 📋 Prerequisites

- Python 3.10+
- Docker Desktop (for local development and Swarm demo)
- Git

## 🛠️ Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Run tests:**
   ```bash
   pytest -v
   ```

4. **Run linting:**
   ```bash
   pylint calculator.py app.py
   ```

## 🐳 Docker Deployment

```bash
docker build -t c270todolist:latest .
docker run -p 8080:8080 c270todolist:latest
```

Visit https://yesdaddycalculator.onrender.com/ (production) or http://localhost:8080 (local)

## 🔄 Docker Swarm Orchestration

The [docker-compose.yml](docker-compose.yml) file defines orchestration settings:
- 3 replicas
- load balancing
- restart policies
- health checks
- resource limits

### Manual Swarm Commands (for presentation)

```bash
# Step 1: Initialize Swarm
docker swarm init

# Step 2: Build the image
docker build -t c270todolist:latest .

# Step 3: Deploy stack (starts 3 replicas)
docker stack deploy -c docker-compose.yml yesdaddy-calc-stack

# Step 4: View services and replicas
docker service ls
docker service ps yesdaddy-calc-stack_todolist-app

# Step 5: Scale UP to 5 replicas (horizontal scaling)
docker service scale yesdaddy-calc-stack_todolist-app=5

# Step 5: View updated replicas
docker service ps yesdaddy-calc-stack_todolist-app

# Step 6: Scale DOWN to 2 replicas
docker service scale yesdaddy-calc-stack_todolist-app=2

# Step 7: View service logs
docker service logs yesdaddy-calc-stack_todolist-app

# Cleanup: Remove stack
docker stack rm yesdaddy-calc-stack 

# Cleanup: Leave swarm
docker swarm leave --force
```

## 🔁 CI/CD Pipeline

GitHub Actions workflow ([.github/workflows/ci.yml](.github/workflows/ci.yml)) includes:

### Pipeline Jobs:

1. **Test & Lint Job:**
   - Checks out code from GitHub
   - Sets up Python 3.10 environment
   - Installs dependencies from requirements.txt
   - **Lints code with pylint** (code quality gate)
   - **Runs unit tests with pytest** (functional verification)

2. **Docker Build & Test Job:**
   - Builds Docker image from Dockerfile
   - Starts container on port 8080
   - **Performs smoke test** (curl health check)
   - Validates container logs
   - Cleans up test container

### Pipeline Triggers:
- **Push to main branch** - runs all jobs
- **Pull requests to main** - runs all jobs

### Quality Gates:
- ✅ Pylint must pass (code quality standards)
- ✅ All unit tests must pass
- ✅ Docker image must build successfully
- ✅ Container must start and respond to HTTP requests

This ensures **only tested, linted, and containerized code** reaches production.

## 📁 Project Structure

```
c270todolist/
├── .github/workflows/ci.yml
├── app.py
├── calculator.py
├── test_calculator.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── static/
└── templates/
```

## 🎯 Scalability, Availability & Security

- **Scalability:** Swarm replicas scale horizontally
- **Availability:** restart policies + health checks
- **Security:** secrets managed in GitHub Actions

## 📝 License

Educational project for C270 CA2.
