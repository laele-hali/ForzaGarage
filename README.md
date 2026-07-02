# 🚗 Garage API

A personal learning project focused on building a modern cloud-native REST API using Python, FastAPI, MongoDB, Redis, Docker and Kubernetes.

The application stores and manages a collection of cars, initially from **Forza Horizon 6**, while serving as a practical platform for learning backend development, containerisation and Kubernetes deployment.

---

# Project Goals

This project is designed to gain hands-on experience with:

* Building REST APIs
* Working with NoSQL databases
* Implementing Redis caching
* Containerising applications with Docker
* Deploying applications to Kubernetes
* Using Git and GitHub effectively
* Understanding cloud-native architecture

The application itself is intentionally simple so the focus remains on learning the surrounding technologies.

---

# Planned Technology Stack

| Technology           | Purpose                       |
| -------------------- | ----------------------------- |
| Python               | Primary programming language  |
| FastAPI              | REST API framework            |
| MongoDB              | Primary NoSQL database        |
| Redis                | In-memory cache               |
| Docker               | Containerisation              |
| Kubernetes (k3d/k3s) | Local container orchestration |
| Git                  | Version control               |
| GitHub               | Source code hosting           |

---

# Planned Architecture

```text
                    Client
                       │
                       ▼
                 FastAPI Application
                  /             \
                 /               \
                ▼                 ▼
          Redis Cache       MongoDB Database
```

MongoDB stores the permanent data.

Redis stores temporary cached data to improve performance and reduce database queries.

---

# Development Roadmap

## Stage 1 - Project Setup

* [ ] Create GitHub repository
* [ ] Configure Git
* [ ] Create project structure
* [ ] Build initial FastAPI application

---

## Stage 2 - MongoDB Integration

* [ ] Deploy MongoDB
* [ ] Connect FastAPI
* [ ] Create Car model
* [ ] Implement CRUD endpoints

---

## Stage 3 - Redis Caching

* [ ] Deploy Redis
* [ ] Cache individual car lookups
* [ ] Implement cache invalidation
* [ ] Configure cache expiration

---

## Stage 4 - Docker

* [ ] Build application image
* [ ] Containerise MongoDB
* [ ] Containerise Redis
* [ ] Test local deployment

---

## Stage 5 - Kubernetes

* [ ] Create local k3d cluster
* [ ] Deploy MongoDB
* [ ] Deploy Redis
* [ ] Deploy FastAPI
* [ ] Configure networking
* [ ] Verify communication between services

---

## Stage 6 - Application Improvements

* [ ] Search
* [ ] Filtering
* [ ] Pagination
* [ ] Validation
* [ ] Logging
* [ ] Configuration management

---

## Stage 7 - Advanced Features

* [ ] Authentication
* [ ] User accounts
* [ ] Vehicle images
* [ ] Statistics
* [ ] Background jobs
* [ ] Health checks
* [ ] API rate limiting

---

# Example Car Document

```json
{
  "manufacturer": "Nissan",
  "model": "Skyline GT-R",
  "model_year": 1999,
  "class": "A",
  "type": "Sports Car",
  "rating": 800
}
```

---

# Learning Objectives

By completing this project I aim to understand:

* REST API design
* CRUD operations
* NoSQL databases
* Redis caching strategies
* Docker fundamentals
* Kubernetes deployments
* Container networking
* API testing
* Git workflows
* Cloud-native application architecture

---

# Status

🚧 Work in Progress

This repository is being developed incrementally as a learning exercise. Each stage builds on the previous one, with the goal of understanding not just how to write an application, but how to build, deploy and manage it using modern backend technologies.

---

# License

This project is licensed under the MIT License.
