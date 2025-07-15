# 🚀 KPA Wheel Specification API

A clean **FastAPI + PostgreSQL** backend for managing wheel specifications with two REST endpoints.

---

## ⚙️ Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Postman Collection](#postman-collection)
- [Demo Video](#demo-video)
- [Project Structure](#project-structure)
- [License](#license)
- [Contact](#contact)

---

## Overview
This project delivers two simple yet functional API endpoints:

- **POST**/wheel-specification` – Create a new wheel specification entry.
- **GET** `/wheel-specification/{id}` – Retrieve an existing entry by its generated ID.

The API is modular, using separate files for database models, validation schemas, CRUD operations, and routing.

---

## Tech Stack
- **FastAPI** – for API development  
- **SQLAlchemy** – ORM for PostgreSQL  
- **Pydantic** – input/output validation  
- **PostgreSQL** – data storage  
- **Uvicorn** – application server  
- **python-dotenv** – environment variable management

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/kpa-wheel-spec-api.git
   cd kpa-wheel-spec-api
# kpa-wheel-spec-api200
FastAPI &amp; PostgreSQL Wheel Specification API – Implements two endpoints to create and fetch wheel specifications as per the KPA assignment.
Usage
POST /wheel-specification
Request Body:
{
  "tread_diameter": 30.5,
  "condemning_dia": 20.0,
  "last_shop_issue_size": 25.0,
  "wheel_gauge": 15.0,
  "variation_same_axle": 0.5
}
Success Response (201 Created):
{
  "id": 1,
  "tread_diameter": 30.5,
  "condemning_dia": 20.0,
  "last_shop_issue_size": 25.0,
  "wheel_gauge": 15.0,
  "variation_same_axle": 0.5
}
GET /wheel-specification/{id}
GET http://127.0.0.1:8000/wheel-specification/1
Success Response (200 OK):
{
  "id": 1,
  "tread_diameter": 30.5,
  "condemning_dia": 20.0,
  "last_shop_issue_size": 25.0,
  "wheel_gauge": 15.0,
  "variation_same_axle": 0.5
}
Postman Collection
Included as KPA_form_collection.json with pre-configured POST and GET requests.
Demo Video
https://drive.google.com/file/d/1BPZK5UZwDrvayuIDqSEPYxws2_NFbDvf/view?usp=sharing
Project Structure
kpa-wheel-spec-api/
├── main.py                     # API routes
├── models.py                   # Database models
├── schemas.py                  # Validation schemas
├── crud.py                     # DB operations
├── database.py                 # DB setup
├── .env.example                # Environment variables template
├── KPA_form_collection.json    # Postman collection
├── requirements.txt            # Dependencies
└── README.md                   # This file
Contact
Name – Ashwini K B
Email - kbashwini450@gmail.com
GitHub Profile - https://github.com/Ashwini-200
