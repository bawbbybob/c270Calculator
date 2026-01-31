# C270 Todo List Application

A Flask-based todo list application with CI/CD pipeline, Docker containerization, and Docker Swarm orchestration.

## 🚀 Features

- Flask web application with calculator functionality
- Automated testing with pytest
- CI/CD pipeline using GitHub Actions
- Docker containerization
- Docker Swarm orchestration definition
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
   pytest
   ```

## 🐳 Docker Deployment

```bash
docker build -t c270todolist:latest .
docker run -p 8080:8080 c270todolist:latest
```

Visit https://c270todolist.onrender.com/ (production) or http://localhost:8080 (local)

## 🔄 Docker Swarm Orchestration

The [docker-compose.yml](docker-compose.yml) file defines orchestration settings:
- 3 replicas
- load balancing
- restart policies
- health checks
- resource limits

### Manual Swarm Commands (for presentation)

```bash
# Initialize Swarm
docker swarm init

# Deploy stack
docker stack deploy -c docker-compose.yml todolist-stack

# View services
docker service ls
docker service ps todolist-stack_todolist-app

# Scale service
docker service scale todolist-stack_todolist-app=5

# Remove stack
docker stack rm todolist-stack

# Leave swarm
docker swarm leave --force
```

## 🔁 CI/CD Pipeline

GitHub Actions workflow includes:

1. **Test Job** - installs Python 3.10, installs deps, runs pytest
2. **Docker Build & Test** - builds image and verifies container runs
3. **Deploy** - triggers Render deploy hook on push to main

### GitHub Secrets Required

- `RENDER_DEPLOY_HOOK` (Render deploy hook URL)

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

Educational project for C270.
