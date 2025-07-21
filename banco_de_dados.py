from app.database import SessionLocal, init_db
from app.models import Sale
from datetime import date
import random

init_db()
db = SessionLocal()

produtos = ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E"]
for i in range(50):
    db.add(Sale(
        produto=random.choice(produtos),
        quantidade=random.randint(1, 10),
        preco=random.uniform(10.0, 100.0),
        data=date(2025, 7, random.randint(1, 15))
    ))
db.commit()
db.close()
