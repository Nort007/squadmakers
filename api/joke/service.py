import re
import random
import requests
from core.config import API_CHUCK_NORRIS, API_DAD_JOKE
from schemas.joke_schema import JokeValidateSchema
from api.joke.storage import joke_storage
from api.exceptions.exception import InvalidParamsUsage


def joke_to_dict(response: dict, joke_from: str) -> dict:
    value = list(filter(
        re.compile(r'(joke)|(value)').match,
        response.keys()))[0]
    return {
        "number": response['id'],
        "value": response[value],
        "joke_from": joke_from,
    }


def responser(url: str) -> requests.Response.json:
    """Simple request to api."""
    with requests.Session() as session:
        session.headers.update({'Accept': 'application/json'})
        response = session.get(url)
        return response.json()


def get_random_joke(joke_from: str = None) -> joke_to_dict:
    """Only for random joke."""
    url_api: str | None = None
    apis = {'dad': API_DAD_JOKE, 'chuck': API_CHUCK_NORRIS}
    if joke_from is None:
        joke_from = random.choice(list(apis.keys()))
    match joke_from:
        case 'dad':
            url_api = apis[joke_from]
        case 'chuck':
            url_api = apis[joke_from] + '/' + 'random'
    response = responser(url=url_api)
    return joke_to_dict(response=response, joke_from=joke_from)


def service_save_joke(number: str = None, value: str = None, joke_from: str | None = None):
    """The function implements save new joke
    :param number:* unique ID into db
    :type number:
    :param value: * It's Joke
    :type value:
    :param joke_from: optional [dad, chuck] or None
    :type joke_from:
    :return:
    :rtype:
    """
    try:
        joke_validate = JokeValidateSchema(number=number, value=value, joke_from=joke_from)
    except InvalidParamsUsage:
        raise InvalidParamsUsage(number=number, value=value, joke_from=joke_from)
    joke_storage.create_joke(number=joke_validate.number, value=joke_validate.value, joke_from=joke_validate.joke_from)
    return joke_validate.json()


def service_update_joke(number: str | None = None, value: str | None = None) -> dict:
    """
    :param number: * Joke ID to update
    :type number:
    :param value: * New Text Joke
    :type value:
    :return:
    :rtype:
    """
    try:
        joke_validate = JokeValidateSchema(number=number, value=value)
    except InvalidParamsUsage:
        raise InvalidParamsUsage(number=number, value=value)
    joke_storage.update_joke(number=joke_validate.number, value=joke_validate.value)
    return {"msg": "Updated"}


def service_delete_joke(number: str | None = None) -> dict:
    """The function implements simple delete a row from DB
    :param number: * It's ID on delete
    :type number:
    :return:
    :rtype:
    """
    if len(number) > 0:
        joke_storage.delete_joke(number=number)
    else:
        raise InvalidParamsUsage(number=number)
    return {"msg": "Deleted"}
