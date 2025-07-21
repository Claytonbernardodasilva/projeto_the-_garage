from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()  # type: ignore

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)  # type: ignore
async def selecionar_mes(request: Request):
    return templates.TemplateResponse("selecionar_mes.html", {"request": request})

