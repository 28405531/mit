# config.py
import os

class Config:
    SECRET_KEY = os.urandom(24)
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '#Nawu#*13'
    MYSQL_DB = 'api'
