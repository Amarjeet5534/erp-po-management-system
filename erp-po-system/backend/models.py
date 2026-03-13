from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base


class Vendor(Base):

    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)
    rating = Column(Float)


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sku = Column(String)
    unit_price = Column(Float)
    stock_level = Column(Integer)


class PurchaseOrder(Base):

    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True, index=True)
    reference_no = Column(String)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    total_amount = Column(Float)
    status = Column(String)
