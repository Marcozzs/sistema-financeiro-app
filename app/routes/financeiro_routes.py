from fastapi import APIRouter
from app.services.financeiro_service import gerar_relatorio_financeiro

# O router assume o papel de encaminhador HTTP
router = APIRouter()

@router.post("/relatorios/{cliente_id}")
def solicitar_relatorio(cliente_id: int):
    # A rota capta o pedido da internet e delega o trabalho ao Serviço
    resposta = gerar_relatorio_financeiro(cliente_id)
    return resposta