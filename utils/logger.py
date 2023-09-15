import logging


def configure_logger():
    """
    Настраивает и возвращает экземпляр логгера.
    """
    logger = logging.getLogger("automation_testing_logger")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
