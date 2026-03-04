# python-crud
# PostgreSQL Employee Management App
## 📌 Description
This is a simple Python application that connects to a PostgreSQL database using psycopg2.  
It demonstrates how to:
- Establish a database connection
- Insert employee records
- Retrieve all employee records
- Use environment variables for secure configuration

This project follows proper backend structure using:
- Virtual Environment
- .env file for configuration
- requirements.txt for dependency management

---
## 🛠 Technologies Used
- Python 3.13
- PostgreSQL
- psycopg2
- python-dotenv
---

## 📂 Project Structure

employee_app/
│
├── main.py
├── requirements.txt
├── .env (not uploaded for security)
├── en/ (virtual environment - ignored)
├── .gitignore
└── README.md

---

## ⚙ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv en
en\Scripts\activate

```
install dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Create .env File

Create a file named .env and add:

DB_NAME=postgres
DB_USER=Username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5433
---
🔐 Security Note

Database credentials are stored in a .env file and are not hardcoded in the source code.
The .env file is excluded using .gitignore

---
#output:
<img width="675" height="361" alt="Screenshot 2026-03-04 143642" src="https://github.com/user-attachments/assets/d1b941f2-fe60-4336-bffe-c17c5baed3ee" />
<img width="402" height="260" alt="Screenshot 2026-03-04 143653" src="https://github.com/user-attachments/assets/97c04735-5205-41df-b3ef-d3691832af92" />
