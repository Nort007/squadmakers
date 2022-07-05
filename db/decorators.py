import functools
from db.mixins import DatabaseMixin


def with_tx(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        self: DatabaseMixin = args[0]
        assert self is not None and isinstance(self, DatabaseMixin)
        assert len(args) == 1, 'only kwargs used with @with_tx'
        tx = kwargs.pop('tx') if 'tx' in kwargs else self.make_tx()
        try:
            return func(*args, **kwargs, tx=tx)
        except Exception as e:
            tx.rollback()
            raise e
        finally:
            tx.commit()
    return wrapped
