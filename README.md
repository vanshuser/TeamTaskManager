# Team Task Manager

A full-stack Django web application where users can create projects, assign tasks,
track progress, and manage work efficiently with role-based access control.

🚀 Features

## 🔐 Authentication

* User Signup & Login
* Logout functionality
* Protected routes using `login_required`
* Role-based access (Admin / Member)

## 📁 Project Management

* Create Projects
* Edit Projects
* Delete Projects
* Admin-only project creation

## ✅ Task Management

* Create Tasks
* Assign tasks to users
* Task status tracking
* Priority management
* Deadline management
* Edit/Delete tasks
* Past deadline validation

## 📊 Dashboard

* Total Projects
* Total Tasks
* Completed Tasks
* Pending Tasks
* Overdue Tasks
* Recent Tasks section

## 🎨 UI Features

* Modern Glassmorphism UI
* Bootstrap responsive design
* Attractive gradients and colors
* Dynamic navbar authentication buttons
* Delete confirmation popup

## 🌐 Deployment

* Deployed using Railway
* Gunicorn server configuration
* WhiteNoise static file handling

# 🛠️ Tech Stack

## Backend

* Python
* Django
* Django ORM
* Django REST Framework

## Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

## Database

* SQLite (Development)
* PostgreSQL compatible for deployment

## Deployment

* Railway
* Gunicorn
* WhiteNoise

# 📂 Project Structure

```bash
TeamTaskManager/
│
├── taskmanager/
├── users/
├── projects/
├── tasks/
├── templates/
├── static/
├── requirements.txt
├── Procfile
├── manage.py
```
# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone <your-github-repo-link>
cd TeamTaskManager
```

## 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

## 3️⃣ Run Migrations

```bash
python manage.py migrate
```

## 4️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

## 5️⃣ Run Server

```bash
python manage.py runserver
```
# 🌐 Deployment Steps (Railway)

1. Push project to GitHub
2. Create Railway project
3. Connect GitHub repository
4. Add PostgreSQL database
5. Configure environment variables
6. Deploy application

# 🔒 Validations Implemented

* Authentication required for protected pages
* Admin-only project creation
* Past deadline restriction
* Delete confirmation popup
* Dynamic Login/Logout navbar

# 🎥 Demo Video

The demo video includes:

* Signup/Login
* Project creation
* Task assignment
* Dashboard overview
* Role-based functionality
* Deployment demo

# 👨‍💻 Author

Vansh Sharma

# 📌 Future Improvements

* Email notifications
* Task comments
* File uploads
* Search & filters
* Team chat system
* REST API expansion
* Real-time updates

# ⭐ Conclusion

Team Task Manager is a complete Django-based project management application that demonstrates authentication, 
CRUD operations, role-based access control, validations, dashboard analytics, and deployment skills.
