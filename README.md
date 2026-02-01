RPL To-Do List — Django
A simple To-Do List web application built using Python & Django with user authentication and task management.

📍 Live Deployment:
🔗 https://rpl-to-do-list-django.onrender.com/

📌 About
This Django-based application allows users to:

Create an account and log in

Add, view, edit, and delete to-do tasks

Track the status of tasks

Manage personal task lists

Backend is powered by Django’s ORM with SQLite database (development).

🚀 Features
✔ User Authentication (Login / Logout)
✔ Create, Read, Update, Delete (CRUD) tasks
✔ Personal task list per user
✔ Deployed on Render
✔ Responsive Bootstrap UI

📁 Project Structure
├── myproject/
├── myapp/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md
myproject/ – Django project configuration

myapp/ – Core app for tasks & auth

db.sqlite3 – Default database

requirements.txt – Python dependencies

💻 Local Setup
Clone the repository:

git clone https://github.com/antra1947/RPL-To-do-list-Django.git
Navigate into directory:

cd RPL-To-do-list-Django
Create & activate virtual environment:

python3 -m venv venv
source venv/bin/activate         # macOS / Linux
venv\Scripts\activate            # Windows
Install dependencies:

pip install -r requirements.txt
Run migrations:

python manage.py migrate
Create superuser (optional):

python manage.py createsuperuser
Start server:

python manage.py runserver
Visit http://127.0.0.1:8000/ to use the app.

🛠 Dependencies
See requirements.txt for full list, typically:

Django==4.x
python-dotenv
…
📦 Deployment
This project is deployed on Render at:

👉 https://rpl-to-do-list-django.onrender.com/

If deployment fails or shows errors, make sure:

Environment variables are set (SECRET_KEY, DEBUG, etc.)

Database migrations ran successfully

Static files are correctly collected

🙌 Contributors
Built by Antra (GitHub: antra1947)

📄 License
This project is open-source. Feel free to use or modify it.
