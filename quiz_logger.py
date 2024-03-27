import logging

import coloredlogs


# DEBUG iti afiseaza toate tipurile de erori
# INFO iti face un fisier text cu loggins

logger = logging.getLogger(__name__)
# logging.basicConfig(filename="quiz_log.log", filemode="w", format='%(asctime)s| %(filename)s| %(levelname)s |line: %(lineno)d| %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s| %(filename)s| %(levelname)s |line: %(lineno)d| %(message)s', level=logging.DEBUG)
coloredlogs.install(level='DEBUG', logger=logger)


logger.debug("Aici e un debug00")
logger.info("Aici e un info print")
logger.warning("Aici e un warning")
logger.error("Aici e o eroare")

