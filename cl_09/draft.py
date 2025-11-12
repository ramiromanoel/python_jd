from loguru import logger
from sys import stderr

logger.add("meu_log.log", level="CRITICAL")

def soma(x, y):
    try:
        soma = x + y
        logger.info(f"voce digitou os valores correto, parabens {soma}")
        return soma
    except:
        logger.critical("voce tem que digitar valores corretos")

soma(2, 3)
soma(2, 7)
soma(2, "3")