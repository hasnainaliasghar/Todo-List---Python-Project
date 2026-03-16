<div align="center">

# ✅ Flask ToDo App

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=4A90D9&center=true&vCenter=true&width=435&lines=Simple+Task+Management+App;Built+with+Flask+%2B+SQLAlchemy;Clean+%26+Minimal+UI+with+Bootstrap+5" alt="Typing SVG" />

<br/>

[![Flask](https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&logo=python&logoColor=white)](https://www.sqlalchemy.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

> 🗂️ A lightweight, no-fuss task manager — add tasks, check them off, and stay organized.

</div>

---

## ✨ Features

<div align="center">

| 🔧 Feature | 📋 Description |
|:---:|:---|
| ➕ **Add Tasks** | Quickly add tasks from the input field |
| ✅ **Mark as Done** | Move tasks to the completed section with one click |
| 🗑️ **Delete Tasks** | Remove completed tasks to keep your list clean |
| 💾 **Persistent Storage** | Tasks are saved to a local SQLite database |
| 📱 **Responsive UI** | Clean Bootstrap 5 layout that works on any screen |

</div>

---

## 🛠️ Tech Stack

<div align="center">

```
┌─────────────────────────────────────────────────┐
│                  Flask ToDo App                 │
├──────────────┬──────────────┬───────────────────┤
│   Frontend   │   Backend    │     Database      │
│  Bootstrap 5 │    Flask     │      SQLite       │
│   Jinja2     │  SQLAlchemy  │   (via ORM)       │
└──────────────┴──────────────┴───────────────────┘
```

</div>

---

## 📁 Project Structure

```
flask-todo/
│
├── 📄 app.py                  # Main Flask application & routes
├── 📁 instance/
│   └── 🗄️  task.db            # SQLite database (auto-generated)
└── 📁 templates/
    └── 🌐 index.html          # Jinja2 HTML template
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/flask-todo.git
cd flask-todo
```

### 2️⃣ Create & activate a virtual environment

```bash
python -m venv venv
```

```bash
# 🪟 Windows
venv\Scripts\activate

# 🍎 macOS / 🐧 Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install flask flask-sqlalchemy
```

### 4️⃣ Run the app

```bash
python app.py
```

<div align="center">

🌐 Open your browser and go to **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

</div>

---

## 🗄️ Database Schema

The SQLite database is **auto-created** in the `instance/` folder on first run — no setup needed!

<div align="center">

```
┌──────────────────────────────────┐
│           task (table)           │
├────────┬─────────┬───────────────┤
│  id    │  task   │    status     │
│  INT   │ STRING  │    STRING     │
│  PK    │NOT NULL │pending / done │
└────────┴─────────┴───────────────┘
```

</div>

---

## 📌 API Routes

<div align="center">

| Method | Route | Description |
|:---:|:---|:---|
| `GET` | `/` | 🏠 Home — display all tasks |
| `POST` | `/add` | ➕ Add a new task |
| `GET` | `/done/<id>` | ✅ Mark a task as done |
| `GET` | `/delete/<id>` | 🗑️ Delete a completed task |

</div>

---

## 🔮 Future Improvements

- [ ] 🔐 User authentication & login
- [ ] 📅 Task due dates & reminders
- [ ] 🏷️ Task categories / tags
- [ ] 🌙 Dark mode toggle
- [ ] 🔃 Drag-and-drop task reordering

---

<div align="center">

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!<br/>
Feel free to open an [issue](https://github.com/your-username/flask-todo/issues) or submit a pull request.

<br/>

⭐ **If you found this project helpful, please give it a star!** ⭐

<br/>

[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red?style=for-the-badge)](https://github.com/hasnainaliasghar)
[![GitHub followers](https://img.shields.io/github/followers/your-username?style=for-the-badge&logo=github)](https://github.com/hasnainaliasghar)

<br/>

📄 This project is licensed under the **[MIT License](LICENSE)**

</div>
