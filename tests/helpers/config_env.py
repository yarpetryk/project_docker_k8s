import os
from dotenv import load_dotenv


def config_env():
    load_dotenv(dotenv_path='./config.env')
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    return {
        "login": login,
        "password": password
    }
