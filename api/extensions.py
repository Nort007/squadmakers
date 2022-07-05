"""Only engine creator"""
from core import config
from sqlalchemy import create_engine

engine = create_engine(config.DB_URI, echo=True, pool_pre_ping=True, pool_recycle=60 * 20)
