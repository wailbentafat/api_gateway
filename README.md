# FastAPI API Gateway 
## Overview

This is an API Gateway built with FastAPI that:
- Routes requests to different microservices
- Uses JWT authentication for secure access
- Implements a basic Load Balancer for microservices

## Features Implemented

### 1. Authentication (JWT)

* Users authenticate using JWT tokens.
* Tokens store username and role (e.g., admin, student).
* Every request must include a valid token.

### 2. API Gateway with Proxying

* Routes API requests to Auth, Users, Courses services.
* Supports dynamic routing for microservices.
* Verifies JWT before forwarding requests.


## 🛠️ Setup & Installation

### 1️⃣ Install Dependencies

```bash
pip install fastapi uvicorn httpx python-jose pydantic
```

### 2️⃣ Run the API Gateway

```bash
uvicorn app.main:app --reload
```

## 📂 Project Structure

```
app/
├── main.py             # API Gateway (Routes & Load Balancing)
├── auth.py             # JWT Authentication
├── config.py           # Microservice URLs & Config
└── logger.py           # Logging System
```

## 📌 Next Steps

- ✅ Implement API Key Authentication
- ✅ Add Role-Based Access Control (RBAC)
- ✅ Improve Load Balancer Algorithm

