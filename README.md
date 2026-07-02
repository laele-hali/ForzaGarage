# 🚗 Forza Garage API

A personal learning project created to gain practical experience with the technologies commonly used when deploying and supporting modern Redis-based applications.

Rather than learning Redis in isolation, this project explores how it fits into a complete backend stack alongside **FastAPI**, **MongoDB**, **Docker**, and eventually **Kubernetes**.

The application stores and manages a collection of vehicles from **Forza Horizon 6**, while serving as a hands-on environment for understanding caching, containerisation, service communication and cloud-native application architecture.

---

# Why This Project Exists

I created this project to gain practical experience with technologies frequently found in modern backend environments, particularly those surrounding Redis Enterprise deployments.

Instead of following isolated tutorials, the goal is to build, test and troubleshoot a complete application from scratch while documenting each stage of development.

Areas of focus include:

- REST API design
- Redis caching strategies
- NoSQL database design
- Docker containerisation
- Container networking
- Kubernetes orchestration
- Git workflows
- Linux administration
- Troubleshooting distributed applications

---

# Technology Stack

| Technology | Purpose | Status |
|------------|---------|:------:|
| Python | Backend application | ✅ |
| FastAPI | REST API framework | ✅ |
| MongoDB | Primary NoSQL database | ✅ |
| Redis | In-memory cache | ✅ |
| Docker | Container platform | ✅ |
| Docker Compose | Local multi-container environment | ✅ |
| Kubernetes (k3d/k3s) | Local orchestration | 🚧 Planned |
| Git | Version control | ✅ |
| GitHub | Source code hosting | ✅ |

---

# Current Architecture

```text
                    Client
                       │
                       ▼
                 FastAPI Application
                  /               \
                 ▼                 ▼
          Redis Cache       MongoDB Database
```

MongoDB stores the permanent application data.

Redis stores frequently requested data in memory, reducing database queries and improving response times.

---

# Redis Cache Demonstration

The application currently implements the **Cache Aside** pattern.

```text
GET /cars/{id}

          │
          ▼
      Redis Cache
          │
    ┌─────┴─────┐
    │           │
 Cache HIT   Cache MISS
    │           │
 Return     MongoDB Query
                │
         Store in Redis
                │
             Return
```

Example application logs:

```text
2026-07-02 11:39:06 INFO [forza_garage.cache] Cache MISS for key: car:6a463612094d3a01df384e80
2026-07-02 11:39:06 INFO [forza_garage.cache] Stored key in Redis: car:6a463612094d3a01df384e80 with TTL: 300 seconds
2026-07-02 11:39:06 INFO [forza_garage.cache] Cache HIT for key: car:6a463612094d3a01df384e80
```

The first request retrieves the vehicle from MongoDB and stores it in Redis.

Subsequent requests are served directly from Redis until the cache expires, demonstrating the cache-aside pattern commonly used in production applications.

---

# Current Features

## API

### Health

- `GET /`
- `GET /health`
- `GET /health/db`
- `GET /health/redis`

### Cars

- `POST /cars`
- `GET /cars`
- `GET /cars/{id}`

---

# Example Vehicle Document

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
├── cache.py
├── config.py
├── crud.py
├── database.py
├── main.py
├── models.py
├── schemas.py
└── routers/
    ├── cars.py
    └── health.py

docker-compose.yml
README.md
requirements.txt
```

---

# Development Roadmap

## ✅ Stage 1 – Project Setup

- GitHub repository
- Git configuration
- Project structure
- FastAPI application
- Swagger/OpenAPI documentation

---

## ✅ Stage 2 – MongoDB Integration

- MongoDB via Docker Compose
- Database connection
- Vehicle schema
- Create endpoint
- List endpoint
- Retrieve endpoint
- Database health endpoint

---

## ✅ Stage 3 – Redis Integration

- Redis via Docker Compose
- Redis health endpoint
- Cache Aside implementation
- Configurable cache TTL
- Cache hit/miss logging

---

## 🚧 Stage 4 – CRUD Completion

- Update endpoint
- Delete endpoint
- Cache invalidation
- Search
- Filtering

---

## 🚧 Stage 5 – Containerisation

- Containerise FastAPI
- Multi-container deployment
- Production-ready image

---

## 🚧 Stage 6 – Kubernetes

- Local k3d cluster
- Deploy FastAPI
- Deploy MongoDB
- Deploy Redis
- Kubernetes Services
- Ingress
- Health probes

---

# Future Improvements

- Authentication
- Pagination
- Vehicle images
- Statistics
- Background jobs
- Metrics
- GitHub Actions CI/CD
- Monitoring

---

# Learning Objectives

The purpose of this project is to build practical experience with technologies commonly found in enterprise support and cloud-native environments.

This includes:

- REST API development
- Python backend development
- Redis caching
- NoSQL databases
- Docker
- Kubernetes
- Linux-based deployment
- Container networking
- Logging and observability
- Troubleshooting
- Git workflows

The emphasis is on understanding **how these technologies work together** rather than learning each component independently.

---

# Current Status

🚧 **Active Development**

This repository is being developed incrementally as a learning project.

Each completed stage represents a working milestone committed to Git, with the goal of understanding not only how to build an application, but how to deploy, troubleshoot and support it using modern backend technologies.

---

# License

Licensed under the MIT License.
