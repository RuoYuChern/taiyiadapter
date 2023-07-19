import logging

LOG_FMT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="../adp.log", level=logging.INFO, format=LOG_FMT)
logger = logging.getLogger("adp")
