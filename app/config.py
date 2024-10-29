import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='test_log_reg/.env')

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    print(f"SECRET_KEY: {SECRET_KEY}")
    print(f"SQLALCHEMY_TRACK_MODIFICATIONS: {SQLALCHEMY_TRACK_MODIFICATIONS}")
    if SQLALCHEMY_DATABASE_URI is None:
        print(f"SQLALCHEMY_DATABASE_URI: {SQLALCHEMY_DATABASE_URI}")
        print(load_dotenv(dotenv_path='test_log_reg/.env'))
        raise ValueError("SQLALCHEMY_DATABASE_URI is not set")
