# communication.py
from celery import Celery
from config import Config

# Initialize the Celery app
communication_bus = Celery("MultiAgentSystem")
communication_bus.config_from_object(Config)

# CRITICAL FIX: Tell Celery to auto-discover your separate agents
communication_bus.autodiscover_tasks(['agents'], force=True)

print("[Communication Layer] Network bus initialized successfully.")