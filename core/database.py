import pymysql
from contextlib import contextmanager
from core.config import settings

@contextmanager
def db_connection():
    connection = None
    try:
        connection = pymysql.connect(
            host=settings.MYSQL_HOST,
            user=settings.MYSQL_USERNAME,
            password=settings.MYSQL_PASSWORD,
            database=settings.MYSQL_DB,
            port=settings.MYSQL_PORT
        )
        yield connection
    finally:
        if connection:
            connection.close()
