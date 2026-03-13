from fastapi import FastAPI
from database import engine
import models

# routers
from routers import vendors, products, purchase_orders, auth

# create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ERP Purchase Order System")


# include routers
app.include_router(vendors.router)
app.include_router(products.router)
app.include_router(purchase_orders.router)
app.include_router(auth.router)


@app.get("/")
def home():
    return {"message": "ERP Purchase Order System Running"}
