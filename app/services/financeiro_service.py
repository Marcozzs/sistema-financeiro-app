from app.repositories.financeiro_repo import buscar_dados_cliente
from app.utils.auditoria import logger
from redis import Redis
from rq import Queue

conexao_redis = Redis(host='localhost', port=6379)
fila_relatorio = Queue('fila_relatorios', connection=conexao_redis)

def gerar_relatorio_financeiro(cliente_id: int):
    dados_cliente = buscar_dados_cliente(cliente_id)

    if dados_cliente["status"] != "ativo":
        logger.warning(f"Recusado: Cliente {cliente_id} está inativo.")
        return {"erro": "O cliente não está ativo."}

    logger.info(f"Despachando o relatório do cliente {cliente_id} para a fila...")
    fila_relatorio.enqueue("app.worker.gerar_pdf", cliente_id)
    return {"status": "Aceito", "mensagem": "Relatório em processamento."}