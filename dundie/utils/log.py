import logging
import os
from logging import handlers
from typing import Union

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger("dundie")
fmt = logging.Formatter(
    "%(asctime)s  %(name)s  %(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s"
)


def get_logger(
    logfile: Union[str, os.PathLike[str]] = "dundie.log"
) -> logging.Logger:
    """Returns a configured logger."""
    fh = handlers.RotatingFileHandler(
        logfile,
        maxBytes=10**6,
        backupCount=10,
    )
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log
