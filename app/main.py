from fastapi import FastAPI
from app.routes.financeiro_routes import router as rotas_financeiras
import uvicorn

app = FastAPI(title="API do Sistema Financeiro")

app.include_router(rotas_financeiras, prefix="/api")

if __name__ == "__main__":
    # O Uvicorn aponta para a instância 'app' dentro de 'main.py'
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)