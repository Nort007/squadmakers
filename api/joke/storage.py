from db.jokes.model import JokeModel
from db.mixins import DatabaseMixin
from db.decorators import with_tx
from sqlalchemy.orm import Session
from api.extensions import engine


class JokeStorageSql(DatabaseMixin):
    @with_tx
    def create_joke(self, tx: Session, number: str, value: str, joke_from: str | None = None):
        joke = JokeModel(number=number, value=value, joke_from=joke_from)
        try:
            tx.add(joke)
            tx.commit()
        except Exception:
            tx.rollback()
            raise

    @with_tx
    def update_joke(self, tx: Session, number: str, value: str):
        tx.query(JokeModel).filter_by(number=number).update({'value': value})
        try:
            tx.commit()
        except Exception:
            tx.rollback()
            raise

    @with_tx
    def delete_joke(self, tx: Session, number: str):
        tx.query(JokeModel).filter_by(number=number).delete()
        try:
            tx.commit()
        except Exception:
            tx.rollback()
            raise


joke_storage = JokeStorageSql(engine=engine)
