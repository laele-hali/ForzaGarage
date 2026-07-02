# 🚗 Forza Garage API

A personal learning project focused on building a modern cloud-native REST API using Python, FastAPI, MongoDB, Redis, Docker and Kubernetes.

The application stores and manages a personal collection of cars from **Forza Horizon 6**, while providing a practical platform for learning backend development, containerisation, caching and Kubernetes.

---

# Project Goals

This project is designed to gain practical experience with:

- Building REST APIs
- Working with NoSQL databases
- Implementing Redis caching
- Containerising applications with Docker
- Deploying applications with Kubernetes
- Using Git and GitHub effectively
- Understanding cloud-native application architecture

The application is intentionally simple so the focus remains on understanding the technologies behind modern backend development.

---

# Current Technology Stack

| Technology | Purpose | Status |
|------------|---------|--------|
| Python | Primary programming language | ✅ |
| FastAPI | REST API framework | ✅ |
| MongoDB | Primary NoSQL database | ✅ |
| Redis | In-memory cache | 🚧 Planned |
| Docker | Container platform | ✅ |
| Docker Compose | Local multi-container environment | ✅ |
| Kubernetes (k3d/k3s) | Local orchestration | 🚧 Planned |
| Git | Version control | ✅ |
| GitHub | Remote repository | ✅ |

---

# Current Architecture

```text
                 Client
                    │
                    ▼
             FastAPI Application
                    │
                    ▼
               MongoDB Database
```

### Planned Architecture

```text
                 Client
                    │
                    ▼
             FastAPI Application
              /               \
             ▼                 ▼
        Redis Cache      MongoDB Database
```

MongoDB stores the permanent vehicle data.

Redis will cache frequently requested data to reduce database queries and improve performance.

---

# Current Features

## Health

- GET `/`
- GET `/health`
- GET `/health/db`

## Cars

- POST `/cars`
- GET `/cars`
- GET `/cars/{id}`

---

# Example Car Document

```json
{
  "manufacturer": "Nissan",
  "model": "Skyline GT-R V-Spec II",
  "model_year": 1999,
  "performance_class": "A",
  "pi": 800,
  "rarity": "Rare",
  "drivetrain": "AWD",
  "is_new": false,
  "nickname": "Grip Build",
  "garage_slot": 1
}
```

---

# Project Structure

```text
app/
├── config.py
├── crud.py
├── database.py
├── main.py
├── models.py
├── schemas.py
└── routers/
    ├── cars.py
    └── health.py
```

---

# Development Roadmap

## ✅ Stage 1 - Project Setup

- GitHub repository
- Git configuration
- Project structure
- FastAPI application
- Swagger documentation

---

## ✅ Stage 2 - MongoDB Integration

- MongoDB via Docker Compose
- Database connection
- Car schema
- Create car endpoint
- List cars endpoint
- Retrieve single car endpoint
- Database health check

---

## 🚧 Stage 3 - Redis Integration

- Deploy Redis
- Cache GET `/cars/{id}`
- Cache invalidation
- Cache expiration (TTL)

---

## 🚧 Stage 4 - Docker

- Containerise FastAPI
- Multi-container development environment
- Build application image

---

## 🚧 Stage 5 - Kubernetes

- Create local k3d cluster
- Deploy MongoDB
- Deploy Redis
- Deploy FastAPI
- Configure Services
- Configure Ingress
- Health probes

---

## Future Improvements

- Update endpoint
- Delete endpoint
- Search
- Filtering
- Pagination
- Authentication
- Vehicle images
- Statistics
- Background jobs
- Logging
- CI/CD with GitHub Actions

---

# Learning Objectives

By completing this project I aim to understand:

- REST API design
- CRUD operations
- NoSQL databases
- Redis caching
- Docker
- Docker Compose
- Kubernetes
- Container networking
- API testing
- Git workflows
- Cloud-native application architecture

---

# Current Progress

### Completed

- FastAPI application
- MongoDB integration
- Docker Compose
- Create car endpoint
- List cars endpoint
- Retrieve single car endpoint
- GitHub SSH authentication

### Next Milestone

Implement Redis caching for individual car lookups.

---

# License

This project is licensed under the MIT License.
