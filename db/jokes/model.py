from db.base.model import BaseModel
from sqlalchemy import Column, String, Text, Enum
from db.enums.joke import JokeFormat


class JokeModel(BaseModel):
    __tablename__ = 'jokes'

    number: str = Column('number', String(256), nullable=False)
    value: str = Column('value', Text(), nullable=False)
    joke_from = Column(
        'joke_from',
        Enum(JokeFormat),
        nullable=True
    )
