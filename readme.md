# 🛒 Store Management System (Python + SQL Capstone)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-Multi--Tiered-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A multi-tiered, object-oriented Store Management System built with **Python 3** and **SQLite3**. Developed as part of a 6-part capstone series on **D-Code it** to demonstrate clean software design principles, enterprise layer decoupling, and safe SQL persistence.

---

## 🏛️ Architecture Overview

The application strictly separates operational concerns into distinct layers:

* **Presentation Layer (`main.py`):** Interactive terminal UI handling menus, input validation, exception catching, and tabular output.
* **Service Layer (`services/`):** Core business logic, stock boundary validation, discount calculation, and domain exceptions (`OutOfStockError`, `InvalidOrderError`).
* **Repository Layer (`repositories/`):** Data Mapper pattern that executes parameterized SQL queries and maps raw database rows into Python objects.
* **Domain Models (`models/`):** Object-Oriented class hierarchy using Abstract Base Classes (`Product`, `PhysicalProduct`, `DigitalProduct`).
* **Database Layer (`database/`):** Context-managed SQLite connection handler ensuring atomic transactions and automatic rollbacks on error.

---

## 📂 Project Structure

```text
python-sql-capstone/
│
├── database/
│   ├── __init__.py
│   ├── schema.sql           # Database table initialization script
│   └── db_handler.py        # SQLite context manager connection handler
│
├── models/
│   ├── __init__.py
│   └── product.py           # Abstract Base Class Product & concrete subclasses
│
├── repositories/
│   ├── __init__.py
│   └── product_repository.py # SQL CRUD queries and Data Mapping
│
├── services/
│   ├── __init__.py
│   └── store_service.py     # Business logic, discounts, and custom errors
│
├── main.py                  # Terminal UI application entrypoint
├── .gitignore
├── LICENSE
└── README.md

🚀 Quick Start
Prerequisites

    Python 3.10+ (Uses standard library modules sqlite3 and sys).

Installation & Execution

    Clone the repository:
    Bash

    git clone [https://github.com/YOUR_USERNAME/python-sql-capstone.git](https://github.com/YOUR_USERNAME/python-sql-capstone.git)
    cd python-sql-capstone

    Run the application:
    Bash

    python main.py

    (Or py main.py on Windows)

    Note: The SQLite database file (store.db) is automatically initialized on the first run using database/schema.sql.

🖥️ Application Demo
Plaintext

=============================================================
         Python + SQL Store Management System        
=============================================================

 --- MENU OPTIONS --- 
1. View all products (inventory)
2. Add New Product
3. Purchase Product
4. Exit Application

Enter your choice (1-4) : 1

=============================================================
ID   | Name                      | Price    | Stock    | Type
-------------------------------------------------------------
1    | Logitech MX Master 3S     | $99.99   | 8        | PHYSICAL
2    | FastAPI Masterclass       | $29.99   | 50       | DIGITAL
=============================================================