# 🛠️ Jyoti Electronics – Repair & Service Management System

A full-featured **electronics repair tracking system** built using **Python (Flask), SQL, HTML, CSS**, designed for service centers and repair shops to manage customer details, product issues, repair status, payments, and daily earnings.

---

## 🚀 Features

### 🔧 Product & Repair Management
- Add products with problem description  
- Track repair status (Pending, In-Progress, Completed)  
- Mark repairs completed instantly  

### 👥 Customer Management
- Store customer name, phone number, and address  
- Record expected delivery / pickup date  
- Maintain complete customer repair history  

### 💰 Payment Tracking
- Record advance payment  
- Auto-calculate remaining balance  
- Track daily and total revenue  

### 📅 Daily Report System
- View all products received on a specific day  
- Check total income generated per day  
- Track completed vs pending repairs  

### 🗂 Persistent History Storage
- All data stored in SQL database (SQLite + SQLAlchemy)  
- Data is preserved even after restarting the app  

### 📱 Mobile + Desktop Access
- Fully responsive UI (works on laptop + phone)  
- Access on mobile via local network or ngrok  
- Can be converted into an **Android APK** using WebView  

---

## 🧱 Tech Stack

| Layer | Technology |
|------|------------|
| **Frontend** | HTML, CSS |
| **Backend** | Python Flask |
| **Database** | SQLite (SQLAlchemy ORM) |
| **Deployment** | Flask Dev Server / Render / ngrok |
| **Optional Mobile App** | Android WebView APK |

---

## 📦 Project Structure
```
jyoti-electronics/
│── app.py
│── requirements.txt
│── Procfile
│── runtime.txt
│── migrate_add_job_columns.py
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── jobs.html
│ ├── job_detail.html
│ ├── expenses.html
│ ├── new_expense.html
│ └── invoice.html
│
└── static/
├── style.css
└── images/
└── reference.jpeg
```
## 🙌 Author

**Developed by:** Krunal Jadhav  
📧 **Email:** krunalj91@gmail.com  
🔗 **LinkedIn:** https://www.linkedin.com/in/krunal-jadhav3007/

---
