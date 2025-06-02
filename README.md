# 🛠️ DevOps Task Manager Project


# 🌐 Full Stack Task Manager API with DevOps Integration

 
This project is a **cloud-based Task Management System** built using two backend APIs:
 
- 🐍 **Flask + MySQL** for user authentication and registration
- 🟢 **Node.js + MongoDB** for task CRUD operations
 
It demonstrates **DevOps best practices** including containerization, CI/CD, monitoring, and deployment on AWS EC2.

 
---

## 🚀 Features

 
- 🔐 JWT Authentication and Secure API
- 🧰 User Management via Flask + MySQL
- 🛢️ Task CRUD via Node.js + MongoDB
- 📦 Dockerized microservices
- 📤 Automated deployment using GitHub Actions
- 📈 Real-time monitoring with Dynatrace
- 🌍 EC2-hosted services with public access
- ⚙️ Planned NGINX reverse proxy with HTTPS support

  
---
 
## 🧱 Tech Stack
 
| Layer           | Tools Used               |
|-----------------|--------------------------|
| Backend (Users) | pythonFlask, MySQL       |
| Backend (Tasks) | Node.js, Express, MongoDB|
| Auth            | JWT (JSON Web Tokens)    |
| DevOps          | Docker, GitHub Actions   |
| Cloud           | AWS EC2 (Amazon Linux)   |
| Monitoring      | Dynatrace                |
| reverse proxy   | NGINX (planned)          |

 
---
 
## 🗂️ Project Structure

```
/task-manager-devops/
├──.github/workflows
|   └──deploy.yml
├── flask-user-api/
| ├── .env
| ├── __init__.py
│ ├── app.py 
│ ├── auth.py 
│ ├── config.py
| ├── db.py 
| ├── routes.py 
│ ├── models.py 
│ └── Dockerfile 
├── node-task-api/
│ ├── app.js 
│ ├── routes/ 
|      └── taskroutes.js
| ├── middleware/ 
|      └── auth.js
│ ├── models/ 
|      └──Task.js
| ├──.dockerignore
| ├──.env
│ └── Dockerfile 
├── docker-compose.yml 
├── .env 
├── setup.sh
└── README.md
```
---

## ⚙️ How It Works
 
### ✅ Flask API
 
- Handles user APIs and login with JWT.
- user can only register without token
- Connected to MySQL via SQLAlchemy.
- Runs on port **5000**.
 
### ✅ Node API
 
- Handles task creation, updates, and deletion.
- require JWT token while performing any **CRUD** operation 
- Connected to MongoDB using Mongoose.
- Runs on port **3000**.
 
--- 

## 🐳 Docker Setup

```
docker-compose up --build
```

🔁 **CI/CD with GitHub Actions**
1. Trigger: On push to main branch.
2. Steps:
    - Build Docker images
    - SCP files to EC2
    - Run containers on remote server
🖥️ **EC2 Deployment**
  - Hosted on Amazon Linux EC2
  - Flask: http://:5000
  - Node.js: http://:3000
📈 **Monitoring**
   - Integrated with Dynatrace OneAgent installed on EC2.
   - Real-time metrics and logs are sent to Dynatrace.
   - Custom dashboard in progress.
🔜 **Upcoming**
- [ ] NGINX reverse proxy setup
- [ ] HTTPS with Let's Encrypt
- [ ] Final Dynatrace dashboard setup

---
## 📬 API Endpoints

| Flask (User API)                                                       |
|----------------------|--------------------------------------------|
| For User Login       | http://localhost:5000/login            |
| To Post User         | http://127.0.0.1:5000/users           |
| To view all Users    | http://localhost:5000/showusers + JWT Token | 
| To view Single User  | http://127.0.0.1:5000/user/<:id> + JWT Token      |
| To Update User       | http://127.0.0.1:5000/update/<:id> + JWT Token    |
| To Delete User       | http://127.0.0.1:5000/users/<:id + JWT Token     |
|----------------------|--------------------------------------------|
| Node.js (Task API)                                                |
|----------------------|--------------------------------------------|
| To Post Task         | [](http://localhost:5001/tasks/createtask) + JWT Token |
| To view all Tasks    | [](http://localhost:3000/tasks/showusers) + JWT Token  | 
| To view User's Task  | [](http://localhost:3000/tasks/user) + JWT Token      |
| To Update Task       | [](http://localhost:3000/tasks/updatetask) + JWT Token |
| To Delete Task       | [](http://localhost:3000/tasks/delete) + JWT Token    |

---

🔐 Protected by JWT: send token in Authorization: Bearer <token>
🧑‍💻 **Author**
👩‍💻 **Shourya**
Cloud & DevOps Enthusiast | Python & Node.js Developer

📜 **License :**
MIT License
 
---

 
