# config.py
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

class Config:
    # Changed to lowercase settings to match Celery 5.x+ requirements
    broker_url = REDIS_URL
    result_backend = REDIS_URL
    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']