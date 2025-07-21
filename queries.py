# app/queries.py
from sqlalchemy import func, desc, extract
from app.database import SessionLocal # type: ignore
from app.models import Sale, Product # type: ignore

def get_top_products(mes: int, ano: int):
    db = SessionLocal()
    try:
        results = db.query(
            Product.name,
            func.sum(Sale.quantity).label("total_vendas")
        ).join(Product, Sale.product_id == Product.id)\
         .filter(
             extract('month', Sale.sale_date) == mes,
             extract('year', Sale.sale_date) == ano
         )\
         .group_by(Product.name)\
         .order_by(desc("total_vendas"))\
         .limit(5).all()

        return [{"nome": r.name, "total_vendas": int(r.total_vendas)} for r in results]
    finally:
        db.close()

