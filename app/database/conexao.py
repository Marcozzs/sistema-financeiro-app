from contextlib import contextmanager
from app.utils.auditoria import logger

@contextmanager
def conexao_bd():
    logger.info("[DB] Abrindo conexão com o banco de dados...")
    conexao = "Conexao_BD"
    try: 
        yield conexao
    except Exception as erro: 
        logger.info(f"[DB] Falha no banco: {erro}")
    finally:
        logger.info("[DB] Fechando conexão com segurança.")