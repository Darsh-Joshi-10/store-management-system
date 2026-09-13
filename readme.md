
# 🛒 Store Management System (Python + SQL Capstone)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-Multi--Tiered-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A multi-tiered, object-oriented Store Management System built with **Python 3** and **SQLite3**.

Developed as part of a 6-part capstone series on [D-Code it](https://www.youtube.com/@D-Code-It10), this project demonstrates clean software design principles, enterprise-layer decoupling, and safe SQL persistence.

---

## 🏛️ Architecture Overview

The application separates operational concerns into distinct layers:

- **Presentation Layer (`main.py`):** Interactive terminal UI handling menus, input validation, exception catching, and tabular output.
- **Service Layer (`services/`):** Core business logic, stock boundary validation, discount calculation, and domain exceptions (`OutOfStockError`, `InvalidOrderError`).
- **Repository Layer (`repositories/`):** Implements the Data Mapper pattern, executing parameterized SQL queries and mapping raw database rows into Python objects.
- **Domain Models (`models/`):** Object-oriented class hierarchy using Abstract Base Classes (`Product`, `PhysicalProduct`, `DigitalProduct`).
- **Database Layer (`database/`):** Context-managed SQLite connection handler ensuring atomic transactions and automatic rollbacks on error.

---

## 📂 Project Structure

```text
python-sql-capstone/
│
├── database/
│   ├── __init__.py
│   ├── schema.sql             # Database table initialization script
│   └── db_handler.py          # SQLite context manager connection handler
│
├── models/
│   ├── __init__.py
│   └── product.py             # Abstract Base Class and concrete subclasses
│
├── repositories/
│   ├── __init__.py
│   └── product_repository.py  # SQL CRUD queries and data mapping
│
├── services/
│   ├── __init__.py
│   └── store_service.py       # Business logic, discounts, and custom errors
│
├── main.py                    # Terminal UI application entrypoint
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or later
- SQLite3 (included with Python's standard library)

No external Python packages are required.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Darsh-Joshi-10/store-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd store-management-system
   ```

### Running the Application

Run the following command:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

> **Note:** The SQLite database file (`store.db`) is automatically initialized on the first run using `database/schema.sql`.

---

## 🖥️ Application Demo

The following is an example of the application's terminal interface:

```text
=============================================================
         Python + SQL Store Management System
=============================================================

--- MENU OPTIONS ---
1. View all products (inventory)
2. Add New Product
3. Purchase Product
4. Exit Application

Enter your choice (1-4): 1

=============================================================
ID   | Name                      | Price    | Stock    | Type
-------------------------------------------------------------
1    | Logitech MX Master 3S     | $99.99   | 8        | PHYSICAL
2    | FastAPI Masterclass       | $29.99   | 50       | DIGITAL
=============================================================
```

---

## 📺 YouTube Course Series

This capstone project was developed step by step in a tutorial series on D-Code it.

- **Channel:** [D-Code it on YouTube](https://www.youtube.com/@D-Code-It10)
- **Playlists:** Python & SQL Courses
- **Project Walkthrough:** Database Connection & Handler Tutorial

---

## 📜 License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.