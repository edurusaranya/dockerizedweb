# 🐳 Dockerized Web Application

> **CodTech IT Solutions — DevOps Internship Project**  
> A production-ready Dockerized web application using Python Flask, Gunicorn, and Nginx.

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=flat&logo=flask&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat&logo=nginx&logoColor=white)
![CI/CD](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat&logo=github-actions&logoColor=white)

---

## 📁 Project Structure

```
dockerized-webapp/
├── app/
│   ├── app.py                  # Flask application
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile              # Multi-stage Docker build
│   ├── .dockerignore
│   ├── templates/
│   │   └── index.html          # Main HTML page
│   └── static/
│       ├── css/style.css
│       └── js/main.js
├── nginx/
│   └── nginx.conf              # Nginx reverse proxy config
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD pipeline
├── docker-compose.yml          # Multi-container orchestration
├── .gitignore
└── README.md
```

---

## 🏗️ Architecture

```
User/Browser
     │
     ▼  Port 80
 ┌─────────┐
 │  Nginx  │  ← Reverse Proxy (nginx:alpine)
 └────┬────┘
      │ Internal Port 5000
      ▼
 ┌──────────────────┐
 │  Flask + Gunicorn│  ← WSGI App Server (python:3.11-slim)
 └──────────────────┘
      │
   app-network (Docker bridge)
```

---

## ⚙️ Prerequisites

Make sure these are installed on your machine:

| Tool | Version | Install |
|------|---------|---------|
| Docker | 24+ | [docs.docker.com](https://docs.docker.com/get-docker/) |
| Docker Compose | 2.0+ | Included with Docker Desktop |
| Git | any | [git-scm.com](https://git-scm.com/) |

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/dockerized-webapp.git
cd dockerized-webapp
```

### 2. Build and run with Docker Compose
```bash
docker-compose up --build
```

### 3. Open in your browser
```
http://localhost
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page — HTML dashboard |
| GET | `/health` | Health check — returns JSON |
| GET | `/api/info` | App metadata — returns JSON |

### Example responses

**GET /health**
```json
{
  "status": "healthy",
  "timestamp": "2025-01-01T10:00:00",
  "hostname": "abc123def456",
  "version": "1.0.0"
}
```

**GET /api/info**
```json
{
  "app": "Dockerized Web Application",
  "author": "CodTech Internship Project",
  "tech_stack": ["Python", "Flask", "Docker", "Nginx"],
  "environment": "production",
  "hostname": "abc123def456"
}
```

---

## 🐳 Docker Commands

```bash
# Build image only
docker build -t dockerized-webapp ./app

# Run with compose (detached)
docker-compose up -d --build

# View running containers
docker ps

# View logs
docker-compose logs -f

# Stop and remove containers
docker-compose down

# Stop and remove containers + images
docker-compose down --rmi all
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

The `.github/workflows/ci.yml` pipeline automatically runs on every push:

1. ✅ Checkout code  
2. 🔨 Build Docker image  
3. 🚀 Start all services  
4. 🧪 Run endpoint health checks  
5. 📋 Print logs  
6. 🧹 Tear down containers  

---

## 🔒 Security Features

- **Non-root user** inside the Docker container (`appuser`)
- **Multi-stage build** — smaller, cleaner final image
- **Security headers** via Nginx (X-Frame-Options, XSS Protection)
- **No secrets in code** — uses environment variables
- **`.dockerignore`** prevents leaking local files into image

---

## 🌍 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_VERSION` | `1.0.0` | Application version |
| `ENVIRONMENT` | `production` | Runtime environment |

Set them in `docker-compose.yml` or pass via CLI:
```bash
APP_VERSION=2.0.0 docker-compose up
```

---

## 👤 Author

**Your Name**  
CodTech IT Solutions — DevOps Internship  
📧 your.email@example.com  
🔗 [GitHub Profile](https://github.com/YOUR_USERNAME)

---

## 📄 License

This project is created as part of the CodTech IT Solutions DevOps Internship program.
