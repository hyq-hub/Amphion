import logging
import time
import os


def init_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Add file handler to save logs to a file
    log_date = time.strftime("%Y-%m-%d", time.localtime())
    log_time = time.strftime("%H-%M-%S", time.localtime())

    os.makedirs(f"logs/{log_date}", exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh = logging.FileHandler(f"logs/{log_date}/{log_time}.log")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # 创建一个自定义的日志格式器，将特定级别的日志设置为红色
    class ColorFormatter(logging.Formatter):
        def format(self, record):
            if record.levelno >= logging.ERROR:
                record.msg = "\033[1;31m" + str(record.msg) + "\033[0m"
            elif record.levelno >= logging.WARNING:
                record.msg = "\033[1;33m" + str(record.msg) + "\033[0m"
            elif record.levelno >= logging.INFO:
                record.msg = "\033[1;34m" + str(record.msg) + "\033[0m"
            elif record.levelno >= logging.DEBUG:
                record.msg = "\033[1;32m" + str(record.msg) + "\033[0m"
            return super().format(record)

    color_formatter = ColorFormatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch = logging.StreamHandler()
    ch.setFormatter(color_formatter)
    logger.addHandler(ch)

    return logger
