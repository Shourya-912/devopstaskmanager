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
├── docker_setup.sh
├── nginx_setup.sh
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

## 🐳 Project Setup

To clone this project and run it, do as instructed in **projectsetup.md**

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

🔜 **Final Setup**
   - [ ] NGINX reverse proxy setup
   - [ ] HTTPS with Let's Encrypt
   - [ ] Final Dynatrace dashboard setup

---

## 📬 API Endpoints

| API Type       | Method      | Endpoint                                    | Description           | Auth Required |
|----------------|-------------|---------------------------------------------|------------------------|----------------|
| Flask (User) | POST | `http://<ec2_ip_address>/api/login`               | Login user            | No             |
| Flask (User) | POST | `http://<ec2_ip_address>/api/users`               | Create user           | No             |
| Flask (User) | GET | `http://<ec2_ip_address>/api/showusers`           | View all users        | Yes (JWT)      |
| Flask (User) | GET | `http://<ec2_ip_address>/api/<id>`           | View single user      | Yes (JWT)      |
| Flask (User) | PUT | `http://<ec2_ip_address>/api/<id>`         | Update user           | Yes (JWT)      |
| Flask (User) | DELETE | `http://<ec2_ip_address>/api/<id>`           | Delete user           | Yes (JWT)      |
| Node.js (Task) | POST | `http://<ec2_ip_address>/task/createtask`    | Create task           | Yes (JWT)      |
| Node.js (Task) | GET | `http://<ec2_ip_address>/task/showusers`     | View all tasks        | Yes (JWT)      |
| Node.js (Task) | GET | `http://<ec2_ip_address>/task/user`          | View user's tasks     | Yes (JWT)      |
| Node.js (Task) | PUT | `http://<ec2_ip_address>/task/updatetask`    | Update task           | Yes (JWT)      |
| Node.js (Task) | DELETE | `http://<ec2_ip_address>/task/delete`        | Delete task           | Yes (JWT)      |

---

🔐 Protected by JWT: send token in Authorization: Bearer <token>

🧑‍💻 **Author**

👩‍💻 **Shourya**

Cloud & DevOps Enthusiast | Python & Node.js Developer

📜 **License :**
MIT License
 
---

 
