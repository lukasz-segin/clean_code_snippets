import logging

logger = logging.getLogger(__name__)  # creation of custom diary

handler = logging.StreamHandler()  # define a stream

# define logging levels
logger.setLevel(logging.WARNING)
handler.setLevel(logging.ERROR)
format_c = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format_c)  # define entry(input) format
logger.addHandler(handler)


def division(divider, divisor):
    try:
        return divider/divisor
    except ZeroDivisionError:
        logger.error("Dividing by 0")


num = division(4, 0)
