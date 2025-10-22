import os

class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # saldırılara karşı koruma sağlamak için kullanır.
    