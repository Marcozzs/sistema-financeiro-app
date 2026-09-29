import logging

logger = logging.getLogger("SistemaFinanceiro")
logger.setLevel(logging.DEBUG)

molde_visual = logging.Formatter('%(asctime)s - [%(name)s] - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(molde_visual)

arquivo_handler = logging.FileHandler("extrato.log", encoding="utf-8")
arquivo_handler.setFormatter(molde_visual)

logger.addHandler(console_handler)
logger.addHandler(arquivo_handler)