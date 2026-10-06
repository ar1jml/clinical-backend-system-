 Clinical Management REST API

A secure backend system for managing patients and medical records, built with Django and Django REST Framework.

This API provides authentication, patient management, and medical record tracking using token-based authentication.

---

Features

- User Registration
- User Login
- Token Authentication
- Patient CRUD (Create, Read, Update, Delete)
- Medical Records CRUD
- Protected Endpoints
- Clean & Extendable Architecture

---

 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

---

⚙️ Installation Guide

1️⃣ Clone Repository

git clone https://github.com/yourusername/clinical-backend-system.git
cd clinical-backend-system

 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate

 3️⃣ Install Dependencies

pip install -r requirements.txt

 4️⃣ Apply Migrations

python manage.py migrate

 5️⃣ Run Server

python manage.py runserver

Server runs at:
http://127.0.0.1:8000/

---

🔐 Authentication Flow

This project uses Token Authentication.

Steps:
1. Register a user
2. Login to receive token
3. Add token in request headers

Header format:

Authorization: Token YOUR_TOKEN_HERE

Without token → API returns 401 Unauthorized.

---

 API Testing Guide (Postman)

---

Register

POST  
http://127.0.0.1:8000/api/accounts/register/

Body → Raw → JSON

{
  "username": "doctor1",
  "email": "doctor1@test.com",
  "password": "123456"
}

Expected Response:

{
  "id": 1,
  "username": "doctor1",
  "email": "doctor1@test.com"
}

---
 2️⃣ Login

POST  
http://127.0.0.1:8000/api/accounts/login/

Body:

{
  "username": "doctor1",
  "password": "123456"
}

Expected Response:

{
  "token": "your_generated_token_here"
}

Copy the token.

---

3️⃣ Create Patient

POST  
http://127.0.0.1:8000/api/patients/

Headers:

Authorization: Token YOUR_TOKEN_HERE

Body:

{
  "first_name": "Ahmed",
  "last_name": "Ali",
  "date_of_birth": "1998-02-10",
  "phone": "0912345678",
  "address": "Addis Ababa"
}

Expected Response:

{
  "id": 1,
  "first_name": "Ahmed",
  "last_name": "Ali"
}

---

 4️⃣ Create Medical Record

POST  
http://127.0.0.1:8000/api/records/

Headers:

Authorization: Token YOUR_TOKEN_HERE

Body:

{
  "patient": 1,
  "diagnosis": "Flu",
  "treatment": "Rest + Paracetamol",
  "notes": "Mild fever"
}

Expected Response:

{
  "id": 1,
  "patient": 1,
  "diagnosis": "Flu"
}

---

 5️⃣ Get Patients

GET  
http://127.0.0.1:8000/api/patients/

(Add token in headers)

---

 6️⃣ Get Records

GET  
http://127.0.0.1:8000/api/records/

(Add token in headers)

---
7️⃣ Update Patient

PUT  
http://127.0.0.1:8000/api/patients/1/

(Add token in headers)

---
 8️⃣ Delete Patient

DELETE  
http://127.0.0.1:8000/api/patients/1/

(Add token in headers)

---

👨‍💻 Author

Arafat  
Python Backend Developer



This backend system is:

- Secure
- Scalable
- Ready for frontend integration (React, Vue, Mobile App)
- Easily extendable (Appointments, Billing, Roles)
