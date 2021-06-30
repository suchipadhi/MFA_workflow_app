import databases
import sqlalchemy
from functools import lru_cache
from api import config
from starlette.config import Config


# 1. Using Pydantic to load .env configuration file
# from api.models import metadata
#
#
# @lru_cache()
# def setting():
#     return config.Settings()
#
#
# def database_pgsql_url_config():
#     return str(setting().DB_CONNECTION + "://" + setting().DB_USERNAME + ":" + setting().DB_PASSWORD +
#                "@" + setting().DB_HOST + ":" + setting().DB_PORT + "/" + setting().DB_DATABASE)


# 2. Using starlette to load .env configuration file
from api.models import metadata


def database_pgsql_url_config():
    conf = Config(".env")
    return str(conf("DB_CONNECTION") + "://" + conf("DB_USERNAME") + ":" + conf("DB_PASSWORD") + "@" + conf("DB_HOST")
               + ":" + conf("DB_PORT") + "/" + conf("DB_DATABASE"))


database = databases.Database(database_pgsql_url_config())
engine = sqlalchemy.create_engine(database_pgsql_url_config())
metadata.create_all(engine)
