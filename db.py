import os
from dotenv import load_dotenv

load_dotenv()

config_read = {
    'host': os.getenv('DB_HOST_R'),
    'user': os.getenv('DB_USER_R'),
    'password': os.getenv('DB_PASSWORD_R'),
    'database': os.getenv('DB_NAME_R'),
}


config_write = {
    'host': os.getenv('DB_HOST_W'),
    'user': os.getenv('DB_USER_W'),
    'password': os.getenv('DB_PASSWORD_W'),
    'database': os.getenv('DB_NAME_W'),
}





