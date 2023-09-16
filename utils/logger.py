import logging


def configure_logger():
    """
    Настраивает и возвращает экземпляр логгера с записью в файл.
    """
    logger = logging.getLogger("automation_testing_logger")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    fh = logging.FileHandler("log_file.log", encoding="utf-8")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
