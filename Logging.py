import inspect
import logging

import pytest


class LogClass:

    def get_logger(self):
        logger = logging.getLogger(inspect.stack()[1][3])  # telling from where log came

        file_handler = logging.FileHandler('log_file.log')
        logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")

        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)  # change if you don't want to see all logs from DEBUG level
        return logger
