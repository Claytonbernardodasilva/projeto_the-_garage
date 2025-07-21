# app/rag_handler.py
import os
from sqlalchemy import func, desc, extract
from datetime import datetime
from app.database import SessionLocal # type: ignore
from app.models import Sale, Product # type: ignore
from langchain_openai import ChatOpenAI

# 🚨 Temporário: chave da API OpenRouter (oculte com .env futuramente)
os.environ["OPENAI_API_KEY"] = "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"

# Inicializa o modelo da OpenRouter (ou outro)
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="mistralai/mixtral-8x7b",
)

def process_question(question: str, mes: int = None, ano: int = None) -> str:
    db = SessionLocal()
    try:
        if "produto mais vendido" in question.lower():
            if mes is None or ano is None:
                return "Por favor, informe o mês e o ano desejados."

            result = db.query(
                Product.name,
                func.sum(Sale.quantity).label("total")
            ).join(Product)\
             .filter(
                extract('month', Sale.sale_date) == mes,
                extract('year', Sale.sale_date) == ano
             )\
             .group_by(Product.name)\
             .order_by(desc("total"))\
             .first()

            if result:
                return f"O produto mais vendido em {mes:02d}/{ano} foi: {result.name}, com {int(result.total)} unidades vendidas."
            return f"Nenhuma venda registrada para {mes:02d}/{ano}."

        return "Pergunta fora do escopo. Use: 'Qual foi o produto mais vendido no mês?'"
    finally:
        db.close()
