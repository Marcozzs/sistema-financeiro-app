import time
from app.utils.auditoria import logger

def gerar_pdf(cliente_id: int):
    logger.info(f"[WORKER] A iniciar a geração do relatório pesado para o cliente {cliente_id}...")
    
    time.sleep(10) 
    
    logger.info(f"[WORKER] Relatório do cliente {cliente_id} finalizado com sucesso!")
    return True