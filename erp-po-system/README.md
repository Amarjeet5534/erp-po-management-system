# ERP Purchase Order Management System

## Overview
This project is a Purchase Order Management System built using FastAPI and PostgreSQL.

The system allows users to manage Vendors, Products, and Purchase Orders with automatic tax calculation.

## Tech Stack

Backend
- FastAPI
- Python
- SQLAlchemy
- PostgreSQL

Frontend
- HTML5
- Bootstrap
- JavaScript

Authentication
- JWT Token Authentication

## Features

✔ Vendor Management  
✔ Product Management  
✔ Purchase Order Creation  
✔ Automatic 5% Tax Calculation  
✔ Dashboard View  
✔ Dynamic Product Rows  
✔ JWT Authentication  

## Database Schema

Tables:

Vendors
- id
- name
- contact
- rating

Products
- id
- name
- sku
- unit_price
- stock_level

PurchaseOrders
- id
- reference_no
- vendor_id
- total_amount
- status

## Running the Project

Install dependencies

pip install fastapi uvicorn sqlalchemy psycopg2 python-jose

Run server

uvicorn main:app --reload

Open API documentation

http://127.0.0.1:8000/docs

Open frontend

frontend/index.html

## Author

Amarjeet kumar