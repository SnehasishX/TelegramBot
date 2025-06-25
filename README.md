# 🧠 Django Internship Project — API + Celery + Telegram Bot

This project was built as part of an internship assignment. It demonstrates:

* ✅ JWT-based Authentication
* ✅ Django REST Framework APIs
* ✅ Redis + Celery for background task processing
* ✅ Telegram bot integration using `python-telegram-bot`

---

## 📁 Features

* ✅ `api/register/` — Create user & trigger welcome email (via Celery)
* ✅ `api/token/` — Get access/refresh tokens
* ✅ `api/protected/` — Secured endpoint (JWT required)
* ✅ Telegram bot that can send messages directly to users

---

## 🚀 Technologies Used

| Tech         | Purpose                             |
| ------------ | ----------------------------------- |
| Django       | Backend web framework               |
| DRF          | Build RESTful APIs                  |
| SimpleJWT    | Token-based authentication          |
| Celery       | Asynchronous task queue             |
| Redis        | Celery broker                       |
| Telegram Bot | External messaging via Telegram API |

---

## ⚙️ Setup Instructions

### 🔧 1. Clone & setup virtualenv

```bash
git clone https://github.com/yourusername/assignment_1.git
cd assignment_1
python -m venv venv
venv\Scripts\activate  # for Windows
pip install -r requirements.txt
```

---

### 🗄️ 2. Database migration

```bash
python manage.py migrate
```

---

### 🧪 3. Run Redis

Make sure Redis is running locally:

```bash
redis-server
```

---

### ⚙️ 4. Run Celery

```bash
celery -A core worker --loglevel=info --pool=solo
```

---

### 🌐 5. Run Django server

```bash
python manage.py runserver
```

---

### 💬 6. Telegram Bot Setup

* Create a bot via [@BotFather](https://t.me/BotFather)
* Add your token to :`settings.py`

```python
TELEGRAM_BOT_TOKEN = "your_bot_token_here"
```

* Test it by running:

```bash
python manage.py send_bot_message
```

---

## ✅ API Endpoints

| Endpoint              | Method | Auth Required | Description                     |
| --------------------- | ------ | ------------- | ------------------------------- |
| `/api/public/`        | GET    | ❌ No          | Public info                     |
| `/api/register/`      | POST   | ❌ No          | Register new user               |
| `/api/token/`         | POST   | ❌ No          | Get JWT access & refresh tokens |
| `/api/token/refresh/` | POST   | ❌ No          | Refresh access token            |
| `/api/protected/`     | GET    | ✅ Yes         | Requires Bearer access token    |

---

## 👤 Created By

**Snehasish Bala**
Internship Project 2025
Telegram bot: [@MyInternship_TestBot]((https://t.me/MyInternship_TestBot))
