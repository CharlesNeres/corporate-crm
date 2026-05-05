# Corporate CRM API

A full-stack backend system built with Django and Django REST Framework to manage clients and tasks in a corporate environment.

This project includes authentication, permissions, filtering, and API documentation using Swagger.

---

## 🚀 Technologies

- Python
- Django
- Django REST Framework (DRF)
- JWT Authentication
- SQLite (dev)
- drf-spectacular (Swagger/OpenAPI)

---

## ✅ Features

- User authentication (JWT)
- Clients and tasks management (CRUD)
- Data isolation per user
- Filtering, search, and ordering
- API documentation (Swagger & Redoc)

---

## 📡 API Endpoints

### Authentication
- POST `/api/token/`
- POST `/api/token/refresh/`

### Clients
- GET `/api/clients/`
- POST `/api/clients/`
- GET `/api/clients/{id}/`

### Tasks
- GET `/api/tasks/`
- POST `/api/tasks/`

---

## ⚙️ How to Run

```bash
git clone https://github.com/SEU_USUARIO/corporate-crm.git
cd corporate-crm

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver 
```

---

## 🔐 Authentication

1. Go to `/api/token/`
2. Send your username and password
3. Copy the access token
4. Use it in headers:

## 📚 API Documentation

- Swagger UI: `/api/docs/`
- Redoc: `/api/redoc/`

## 🧠 What I Learned

- Building REST APIs with Django REST Framework
- Implementing JWT authentication
- Structuring scalable backend systems
- Using Swagger/OpenAPI for API documentation

## 🔮 Future Improvements

- PostgreSQL integration
- Docker setup
- Deployment to cloud (AWS / Railway / Render)