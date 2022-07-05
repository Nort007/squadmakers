from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session


class DatabaseMixin:
    def __init__(self, engine: Engine):
        self._engine = engine
        self._make_tx = sessionmaker(bind=self._engine)

    def make_tx(self) -> Session:
        return self._make_tx()


