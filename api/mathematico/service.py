from core.logger_config import logger
import math
from api.exceptions.exception import InvalidParamsUsage


def get_lcm(numbers: str) -> dict:
    """The function implements return 'LCM' by standard module of python
    :param numbers: * List of numbers
    :type numbers:
    :return: Returns the lowest common multiple
    :rtype: dict
    """
    lcm: int | None = None
    if numbers is not None:
        try:
            logger.debug(f'numbers is not None: {numbers}')
            numbers = list(
                map(
                    int,
                    numbers.strip('][').replace(' ', '').split(',')
                )
            )
            lcm = math.lcm(*numbers)
            logger.debug(f'LCM: {lcm}')
        except InvalidParamsUsage:
            raise InvalidParamsUsage(numbers=numbers)
    return {
        "result": {
            "lcm": lcm
        }
    }


def increment_value(number: int | str) -> dict:
    """The function implements increment obtained value on one
    :param number: * The value of type int
    :type number:
    :return:
    :rtype:
    """
    if number.isnumeric():
        number = int(number)
        logger.debug(f'number is int: {number}')
    else:
        raise InvalidParamsUsage(number=number)
    return {
        "result": {
            "increment_number": number + 1
        }
    }
