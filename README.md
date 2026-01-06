# SAAS Application for Docker Container Management using Flask

## 📌 Project Overview

This project is a **Software as a Service (SAAS)** web application that allows users to manage **Docker containers** through a **web interface** instead of using the command line.  
The application is developed using **Python** and the **Flask** framework and runs **exclusively on Linux**.

The system enables users to:
- Create Docker containers
- Start and stop containers
- Delete containers
- Run **Nginx containers** serving a **custom HTML page**


## 🛠 Technologies Used

| Technology | Description |
|------------|------------|
| Python 3   | Backend programming language |
| Flask      | Web framework for backend |
| Docker     | Containerization platform |
| Nginx      | Web server running inside containers |
| HTML / CSS | Frontend interface |
| Linux      | Required OS |

---

## 🏗 System Architecture

The application uses a **three-layer architecture**:

1. **Frontend**: HTML/CSS, sends HTTP requests to the backend  
2. **Backend**: Flask handles user actions and Docker operations (`app.py`)  
3. **Infrastructure**: Docker Engine manages container lifecycle via Docker SDK for Python

---

## 📂 Project Structure
- `app.py` → Flask backend  
- `templates/` → HTML templates for web interface  
- `static/` → CSS and other static files  
- `nginx/` → custom HTML page for Nginx containers  
- `venv/` → Python virtual environment

---

## 🚀 Quick Setup & Commands

Activate Python virtual environment:
python3 -m venv venv
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt


Installation de Docker et dépendances :
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker


nstallation de Python et création de l’environnement virtuel:
sudo apt install python3-venv


Création et activation de l’environnement virtuel :
python3 -m venv venv
source venv/bin/activate


nstallation de Flask et Docker SDK :
pip install flask docker
pip freeze > requirements.txt


Développement du backend Flask:
nano app.py


Développement de l’interface web:
nano templates/index.html


Page Nginx personnalisée:
nano nginx/index.html


Start Docker daemon (if not running):
sudo systemctl start docker


Run the Flask application:
export FLASK_APP=app.py
flask run --host=0.0.0.0



