"""Pydantic schema"""
from schemas.base_schema import BaseConfigModel


class JokeValidateSchema(BaseConfigModel):
    number: str
    value: str
    joke_from: str = None
