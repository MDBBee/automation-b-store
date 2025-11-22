import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("automationLogger")

        if not logger.handlers:  # prevents adding handlers repeatedly
            logger.setLevel(logging.INFO)

            # Ensure Logs directory exists
            os.makedirs("./Logs", exist_ok=True)

            fileHandler = logging.FileHandler("./Logs/automation.log", mode="a")
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                          datefmt='%m/%d/%Y %I:%M:%S %p')
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)

        return logger
