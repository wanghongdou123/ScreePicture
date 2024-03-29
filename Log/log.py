# encoding = utf-8
import logging.config

logging.config.fileConfig("logger.conf")


def debug(message):
    # 打印debug级别的日志方法
    logging.debug(message)

def warning(message):
    # 打印warning级别的方法
    logging.warning(message)

def info(message):
    # 打印info级别的日志方法
    logging.info(message)

