#  Django Assignment: Building a Healthcare Backend

##  Objective
The goal of this assignment is to create a backend system for a healthcare application using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.  
The system should allow users to register, log in, and manage patient and doctor records securely.  

---

## ⚙ Requirements
- Django & Django REST Framework (DRF) for backend development  
- PostgreSQL as the database  
- JWT authentication with `djangorestframework-simplejwt`  
- RESTful API endpoints for managing patients and doctors  
- Django ORM for database modeling  
- Proper error handling and validation  
- Environment variables for sensitive configurations (`.env`)  

---

##  APIs to be Implemented

###  Authentication APIs
- `POST /api/auth/register/` → Register a new user with name, email, and password  
- `POST /api/auth/login/` → Log in a user and return a JWT token  

---

###  Patient Management APIs
- `POST /api/patients/` → Add a new patient (**Authenticated users only**)  
- `GET /api/patients/` → Retrieve all patients created by the authenticated user  
- `GET /api/patients/<id>/` → Get details of a specific patient  
- `PUT /api/patients/<id>/` → Update patient details  
- `DELETE /api/patients/<id>/` → Delete a patient record  

---

###  Doctor Management APIs
- `POST /api/doctors/` → Add a new doctor (**Authenticated users only**)  
- `GET /api/doctors/` → Retrieve all doctors  
- `GET /api/doctors/<id>/` → Get details of a specific doctor  
- `PUT /api/doctors/<id>/` → Update doctor details  
- `DELETE /api/doctors/<id>/` → Delete a doctor record  

---

###  Patient–Doctor Mapping APIs
- `POST /api/mappings/` → Assign a doctor to a patient  
- `GET /api/mappings/` → Retrieve all patient-doctor mappings  
- `GET /api/mappings/<patient_id>/` → Get all doctors assigned to a specific patient  
- `DELETE /api/mappings/<id>/` → Remove a doctor from a patient  

---

##  Instructions

1. **Set up project**  
   ```bash
   django-admin startproject healthcare_backend
   cd healthcare_backend
   python manage.py startapp api
   ```

2. **Install dependencies**  
   ```bash
   pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt python-decouple
   ```

3. **Configure PostgreSQL** in `settings.py`  
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'healthcare_db',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

4. **Use environment variables** with `.env` file  
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_NAME=healthcare_db
   DATABASE_USER=your_username
   DATABASE_PASSWORD=your_password
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

5. **Apply migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run server**  
   ```bash
   python manage.py runserver
   ```

7. **Test APIs** using Postman or any API client.  

---

##  Expected Outcome
- Users can **register and log in** with JWT authentication  
- Authenticated users can **add/manage patients and doctors**  
- Patients can be **assigned to doctors**  
- Data is stored securely in **PostgreSQL**  

---

## 🚀 Good luck with your assignment!
