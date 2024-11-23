import mysql.connector
from core.config import settings

def db_connection():
    connection = mysql.connector.connect(
        user=settings.MYSQL_USERNAME,
        password=settings.MYSQL_PASSWORD,
        host=settings.MYSQL_HOST,
        database=settings.MYSQL_DB,
        port=settings.MYSQL_PORT
    )
    return connection