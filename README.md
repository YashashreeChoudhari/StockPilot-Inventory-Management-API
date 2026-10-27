# StockPilot — Inventory Management API

StockPilot is a RESTful Inventory Management API built with Python, Django, and Django REST Framework. It helps manage products, warehouses, inventory levels, stock movements, and warehouse transfers through API endpoints.

## Features

- **Product Management** — Manage inventory products and their details.
- **Warehouse Management** — Organize inventory across multiple warehouses.
- **Inventory Tracking** — Monitor stock levels for each product and warehouse.
- **Stock In & Stock Out** — Record incoming and outgoing stock.
- **Stock Transfers** — Transfer inventory between warehouses.
- **JWT Authentication** — Secure API access using JSON Web Tokens.
- **Role-Based Permissions** — Control access to API operations.
- **Audit Trail** — Track stock movement history.
- **Low-Stock Reports** — Identify products that need restocking.
- **API Documentation** — Explore endpoints using Swagger/OpenAPI.
- **Automated Tests** — Test core inventory service functionality.

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Simple JWT
- drf-spectacular (Swagger/OpenAPI)

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/StockPilot-Inventory-Management-API.git
cd StockPilot-Inventory-Management-API
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and configure the required settings.

### 5. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an administrator

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

## API Documentation

Once the development server is running, visit:

- **Swagger UI:** http://127.0.0.1:8000/api/docs/
- **Django Admin:** http://127.0.0.1:8000/admin/

## Authentication

StockPilot uses JWT authentication. Obtain an access token through the configured authentication endpoint and include it in protected API requests:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Testing

Run the Django test suite:

```bash
python manage.py test
```

## Project Goal

The goal of StockPilot is to provide a structured and secure backend for inventory operations, with accurate stock tracking, warehouse management, and a traceable record of stock movements.

## Author

**YOUR NAME**

GitHub: # StockPilot — Inventory Management API

StockPilot is a RESTful Inventory Management API built with Python, Django, and Django REST Framework. It helps manage products, warehouses, inventory levels, stock movements, and warehouse transfers through API endpoints.

## 🚀 Features

- **Product Management** — Manage inventory products and their details.
- **Warehouse Management** — Organize inventory across multiple warehouses.
- **Inventory Tracking** — Monitor stock levels for each product and warehouse.
- **Stock In & Stock Out** — Record incoming and outgoing stock.
- **Stock Transfers** — Transfer inventory between warehouses.
- **JWT Authentication** — Secure API access using JSON Web Tokens.
- **Role-Based Permissions** — Control access to API operations.
- **Audit Trail** — Track stock movement history.
- **Low-Stock Reports** — Identify products that need restocking.
- **API Documentation** — Explore endpoints using Swagger/OpenAPI.
- **Automated Tests** — Test core inventory service functionality.

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Simple JWT
- drf-spectacular (Swagger/OpenAPI)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/StockPilot-Inventory-Management-API.git
cd StockPilot-Inventory-Management-API
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and configure the required settings.

### 5. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an administrator

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

## API Documentation

Once the development server is running, visit:

- **Swagger UI:** http://127.0.0.1:8000/api/docs/
- **Django Admin:** http://127.0.0.1:8000/admin/

## Authentication

StockPilot uses JWT authentication. Obtain an access token through the configured authentication endpoint and include it in protected API requests:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

##  Testing

Run the Django test suite:

```bash
python manage.py test
```

## Project Goal

The goal of StockPilot is to provide a structured and secure backend for inventory operations, with accurate stock tracking, warehouse management, and a traceable record of stock movements.

## Author

**Yashashree Choudhari*
GitHub: https://github.com/YashashreeChoudhari 
