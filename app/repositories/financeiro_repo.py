from app.utils.auditoria import logger
from app.database.conexao import conexao_bd

def buscar_dados_cliente(cliente_id: int):
    with conexao_bd() as banco:
        logger.info("[DB] Buscando cliente...")
    return {"id": cliente_id, "saldo": 5000.0, "status": "ativo"}


