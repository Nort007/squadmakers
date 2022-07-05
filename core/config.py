import os
from pathlib import Path
from dotenv import load_dotenv
from core.logger_config import logger


env = Path(os.path.dirname(__file__)).parent.resolve().joinpath('.env.example')
logger.debug('env path: %s', env)
if os.path.isfile(env):
    load_dotenv(env)


ENDPOINT_V1 = 'v1'
DEBUG = True
DATABASE_HOST = os.getenv('DATABASE_HOST', None)
DATABASE_PORT = os.getenv('DATABASE_PORT', None)
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', None)
DATABASE_USER = os.getenv('DATABASE_USER', None)
DATABASE_NAME = os.getenv('DATABASE_NAME', None)
API_DAD_JOKE = os.getenv('API_DAD_JOKE', 'https://icanhazdadjoke.com')
API_CHUCK_NORRIS = os.getenv('API_CHUCK_NORRIS', 'https://api.chucknorris.io/jokes')
DB_URI = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
