from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from calendar import monthrange
from datetime import datetime, timedelta
from app.database import SessionLocal # type: ignore

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def selecionar_mes(request: Request):
    return templates.TemplateResponse("selecionar_mes.html", {"request": request})

@app.get("/resumo-vendas", response_class=HTMLResponse)
async def resumo_vendas(request: Request, mes: int = Query(...), ano: int = Query(...)):
    db: Session = SessionLocal()
    start_month = datetime(ano, mes, 1)
    end_month = datetime(ano, mes, monthrange(ano, mes)[1])
    last_week_start = end_month - timedelta(days=6)
    last_week_end = end_month

    query_week = text("""
        SELECT p.name, SUM(s.quantity) as total
        FROM sales s
        JOIN products p ON p.id = s.product_id
        WHERE s.sale_date BETWEEN :start AND :end
        GROUP BY p.name
        ORDER BY total DESC
        LIMIT 1
    """)
    result_week = db.execute(query_week, {"start": last_week_start, "end": last_week_end}).fetchone()

    query_top = text("""
        SELECT p.name, SUM(s.quantity) as total
        FROM sales s
        JOIN products p ON p.id = s.product_id
        WHERE strftime('%m', s.sale_date) = :mes AND strftime('%Y', s.sale_date) = :ano
        GROUP BY p.name
        ORDER BY total DESC
        LIMIT 5
    """)
    result_top = db.execute(query_top, {"mes": f"{mes:02d}", "ano": str(ano)}).fetchall()

    return templates.TemplateResponse("resumo_dinamico.html", {
        "request": request,
        "mes": mes,
        "ano": ano,
        "produto_semana": result_week,
        "top5": result_top,
        "inicio_semana": last_week_start.date(),
        "fim_semana": last_week_end.date()
    })
