from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from a file to the database"""
    try:
        with open(filepath, "r") as file_:
            return [line.strip() for line in file_.readlines()]
    except FileNotFoundError as e:
        log.error(str(e))
        raise e
