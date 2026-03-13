from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import json

router = APIRouter()


# DATABASE DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE PURCHASE ORDER
@router.post("/purchase-orders")
def create_po(reference_no: str, vendor_id: int, items: str, db: Session = Depends(get_db)):

    try:
        items = json.loads(items)
    except:
        raise HTTPException(status_code=400, detail="Invalid JSON format for items")

    # check vendor exists
    vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()

    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    total = 0

    for item in items:

        product = db.query(models.Product).filter(
            models.Product.id == item["product_id"]
        ).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        subtotal = item["quantity"] * product.unit_price
        total += subtotal

    # apply 5% tax
    tax = total * 0.05
    total_amount = total + tax

    po = models.PurchaseOrder(
        reference_no=reference_no,
        vendor_id=vendor_id,
        total_amount=total_amount,
        status="Pending"
    )

    db.add(po)
    db.commit()
    db.refresh(po)

    return {
        "po_id": po.id,
        "reference_no": po.reference_no,
        "total_amount": po.total_amount,
        "status": po.status
    }


# GET ALL PURCHASE ORDERS (WITH VENDOR NAME)
@router.get("/purchase-orders")
def get_purchase_orders(db: Session = Depends(get_db)):

    pos = db.query(models.PurchaseOrder).all()

    result = []

    for po in pos:

        vendor = db.query(models.Vendor).filter(
            models.Vendor.id == po.vendor_id
        ).first()

        result.append({
            "id": po.id,
            "reference_no": po.reference_no,
            "vendor_id": po.vendor_id,
            "vendor_name": vendor.name if vendor else "Unknown",
            "total_amount": po.total_amount,
            "status": po.status
        })

    return result


# DELETE PURCHASE ORDER
@router.delete("/purchase-orders/{po_id}")
def delete_po(po_id: int, db: Session = Depends(get_db)):

    po = db.query(models.PurchaseOrder).filter(
        models.PurchaseOrder.id == po_id
    ).first()

    if not po:
        raise HTTPException(status_code=404, detail="Purchase Order not found")

    db.delete(po)
    db.commit()

    return {"message": "Purchase Order deleted successfully"}


# UPDATE PURCHASE ORDER STATUS
@router.put("/purchase-orders/{po_id}/status")
def update_po_status(po_id: int, status: str, db: Session = Depends(get_db)):

    po = db.query(models.PurchaseOrder).filter(
        models.PurchaseOrder.id == po_id
    ).first()

    if not po:
        raise HTTPException(status_code=404, detail="Purchase Order not found")

    po.status = status

    db.commit()
    db.refresh(po)

    return {
        "message": "Status updated successfully",
        "po_id": po.id,
        "status": po.status
    }