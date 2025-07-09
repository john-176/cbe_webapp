# CBE WebApp(Compentency Based Education)

A fullstack web application built with **Django** (backend) and **React + Vite** (frontend), designed for managing school operations like timetables, student showcases, events, and authentication.

---

## Project Structure
CBE_WEBAPP/
├── SERVER_SIDE/ # Django backend
│ ├── cbe_project/ # Django project settings and URLs
│ ├── session_app/ # Auth & user sessions
│ ├── timetable_app/ # Timetables per category
│ ├── content_app/ # Achiever, videos, and media
│ ├── media/ # Uploaded media files
│ └── staticfiles/ # Collected static files for deployment
├── CLIENT_SIDE/ # React frontend (Vite)
│ └── sessionFR/ # React source code
├── .env.example # Example environment variables
├── requirements.txt # Django dependencies
├── package.json # React project config
└── README.md # You're here!


---

## Features

- **Session-based Authentication** (Login, Signup, Logout)
- **Dynamic Timetable Editor** with Real-Time Highlighting
- **
Achievers** showcase (CRUD support)
- **Event Videos & Uploads** (with progress bar & pagination)
- CSRF/Security hardened for deployment
- Modular React frontend using **Vite** + **Axios**

---

## ⚙Installation

### 1. Clone the Repository
```bash
git clone https://github.com/john-176/CBE_WEBAPP.git
cd CBE_WEBAPP

