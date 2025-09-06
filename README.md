# 🏥 Healthcare Backend

A backend system for a healthcare application built using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.  
It provides secure authentication and CRUD operations for managing **patients**, **doctors**, and their **mappings**.

---

## 🚀 Features
- User registration & login with **JWT authentication** (`djangorestframework-simplejwt`).
- Manage **patients** with CRUD operations.
- Manage **doctors** with CRUD operations.
- Map **patients ↔ doctors**.
- PostgreSQL database with Django ORM models.
- Secure endpoints (only authenticated users can modify data).

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL  
- **Authentication:** JWT (SimpleJWT)  

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/Di-Abhi/HealthCare-Django.git
cd healthcare-backend
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install Required Packages
Install dependencies manually:
```bash
pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt
```

### 4. Configure PostgreSQL
Create a database in PostgreSQL:
```sql
CREATE DATABASE healthcare_db;
```

Then, update your **`settings.py`** file with database details:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Also configure **JWT authentication** inside `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start Server
```bash
python manage.py runserver
```

---

## 🔑 Authentication APIs
| Method | Endpoint                  | Description |
|--------|---------------------------|-------------|
| POST   | `/api/auth/register/`     | Register a new user |
| POST   | `/api/auth/login/`        | Login & get JWT |
| POST   | `/api/auth/token/refresh/`| Refresh JWT |

---

## 👩‍⚕️ Patient APIs
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| POST   | `/api/patients/`       | Add new patient |
| GET    | `/api/patients/`       | List all patients of user |
| GET    | `/api/patients/{id}/`  | Get patient details |
| PUT    | `/api/patients/{id}/`  | Update patient |
| DELETE | `/api/patients/{id}/`  | Delete patient |

---

## 👨‍⚕️ Doctor APIs
| Method | Endpoint              | Description |
|--------|-----------------------|-------------|
| POST   | `/api/doctors/`       | Add new doctor |
| GET    | `/api/doctors/`       | List all doctors |
| GET    | `/api/doctors/{id}/`  | Get doctor details |
| PUT    | `/api/doctors/{id}/`  | Update doctor |
| DELETE | `/api/doctors/{id}/`  | Delete doctor |

---

## 🔗 Patient–Doctor Mapping APIs
| Method | Endpoint                         | Description |
|--------|----------------------------------|-------------|
| POST   | `/api/mappings/`                 | Assign doctor to patient |
| GET    | `/api/mappings/`                 | List all mappings |
| GET    | `/api/mappings/{patient_id}/`    | Get all doctors for a patient |
| DELETE | `/api/mappings/{id}/`            | Remove doctor from patient |

---

## ✅ Expected Outcome
- Users can **register & log in** with JWT.  
- Authenticated users can **manage patients and doctors**.  
- Patients can be **assigned to doctors**.  
- Data stored securely in **PostgreSQL**.  
