import logging

import mytwitter.config

CONF = mytwitter.config.CONF


def get_logger():
    return logging.getLogger('mytwitter')


def configure_logging():
    print("configuring logging.")
    log_level = logging.DEBUG if CONF.log.debug else logging.INFO
    formatter = logging.Formatter(CONF.log.log_format)

    logger = get_logger()
    logger.setLevel(log_level)

    def add_handler(h):
        h.setFormatter(formatter)
        h.setLevel(log_level)
        logger.addHandler(h)

    if CONF.log.console_log:
        handler = logging.StreamHandler()
        add_handler(handler)

    if CONF.log.log_file:
        handler = logging.FileHandler(CONF.log.log_file)
        add_handler(handler)
