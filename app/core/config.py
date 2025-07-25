# app/core/config.py

from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file contents into environment variables

class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    S3_BUCKET_NAME: str = os.getenv("S3_BUCKET_NAME")
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")

settings = Settings()
