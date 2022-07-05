"""Base Pydantic schema"""
from pydantic import BaseModel
from utils.camel_case import to_camel_case


class BaseConfigModel(BaseModel):
    number: str = None
    value: str = None
    joke_from: str = None

    class Config:
        orm_mode = True
        alias_generator = to_camel_case
        allow_population_by_field_name = True

