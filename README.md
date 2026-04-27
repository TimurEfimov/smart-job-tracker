🚀 Smart Job Tracker API

Backend приложение для отслеживания откликов на вакансии.
Помогает организовать процесс поиска работы, управлять статусами и анализировать результаты.

---

## 🧠 О проекте

**Smart Job Tracker** — это REST API, которое позволяет:

* 📥 сохранять вакансии
* 📊 отслеживать статус откликов
* 🔍 фильтровать и искать вакансии
* 🔐 работать с авторизацией пользователей

---

## 🛠️ Технологии

* ⚡ FastAPI
* 🗄️ SQLAlchemy
* 🐍 Python 3.11+
* 🔐 JWT авторизация
* 📦 Pydantic / pydantic-settings
* 🧪 SQLite (на старте) / PostgreSQL 

---

## 📂 Структура проекта

```
app/
 ├── api/            # endpoints
 ├── core/           # config и настройки
 ├── db/             # модели и подключение к БД
 ├── repositories/   # работа с БД
 ├── services/       # бизнес-логика
 ├── schemas/        # Pydantic схемы
 └── main.py         # точка входа
```

---

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий

```
git clone https://github.com/your-username/smart-job-tracker.git
cd smart-job-tracker
```

---

### 2. Создать виртуальное окружение

```
python -m venv .venv
```

Активировать:

**Windows:**

```
.venv\Scripts\activate
```

**Mac/Linux:**

```
source .venv/bin/activate
```

---

### 3. Установить зависимости

```
pip install -r requirements.txt
```

---

### 4. Создать `.env`

В корне проекта:

Для SQLite:
```
DATABASE_URL=sqlite:///./jobs.db
SECRET_KEY=supersecretkey
```

Для PostgreSQL:
```
DATABASE_URL=postgresql+psycopg2://postgres:1234@localhost:5432/job_db
SECRET_KEY=supersecretkey
```
Для PostgreSQL нужно установить сам postgres и через pgAdmin (устанавливается вместе с postgres) создать базу данных и назвать ее job_db, также при регистрации указать пароль 1234 или какой вы хотите, но в строке DATABASE_URL нужно будет поменять 1234 на ваш пароль



---

### 5. Запуск сервера

```
uvicorn app.main:app --reload
```

---

## 📘 API документация

После запуска доступно:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## 🔑 Основные endpoints

### 📦 Jobs

* `POST /jobs` — создать вакансию
* `GET /jobs` — получить список вакансий
* `GET /jobs/my` - получить список ваканский, созданных тобой, то есть привзяанные к твоему аккаунта(логину и паролю)
* `GET /jobs/{id}` — получить вакансию по id
* `DELETE /jobs/{id}` — удалить вакансию по id 
* `PATCH /jobs/{id}/status` - отклик на статус вакансии, его может выполнять только тот аккаунт, на котором создавалось резюме(больше предусмотрено для frontend, чем для демонстрации на backend)

---

### 👤 Auth

* `POST /register` — регистрация
* `GET /me` - получение данных о своем аккаунте 
* `POST /login` — получение токена

---

## 📊 Пример данных
JobResponse
```json
{
  "title": "Backend Developer",
  "company": "Google",
  "status": "applied"
}
```

UserResponse
```json user
{
  "username": "user",
  "password": "$argon2id$v=19$m=65536,t=3,p=4$L4VQai3lPKf0fi+F8B6DsA$L5wppsyqsUWT6SzypzfdxDttpvRi70Ai3IdLkNkFdUY",
  "id": 3
}

password - зашифрованный пароль
```

---

## 🔮 Планы по развитию

* 📊 аналитика откликов
* 🧠 AI анализ вакансий
* 📎 загрузка резюме
* 🔔 уведомления

---

## 🧑‍💻 Автор

Разработано в рамках обучения backend разработке на FastAPI.

---

## ⭐ Зачем этот проект

Цель проекта — продемонстрировать:

* архитектуру backend-приложения
* работу с базой данных
* реализацию REST API
* понимание слоёв (API / Service / Repository)

---
