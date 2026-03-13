from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/products")
def create_product(name: str, sku: str, unit_price: float, stock_level: int, db: Session = Depends(get_db)):

    product = models.Product(
        name=name,
        sku=sku,
        unit_price=unit_price,
        stock_level=stock_level
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()
