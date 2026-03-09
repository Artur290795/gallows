"""
Модуль с классом конфигурации приложения
"""
from pathlib import Path


class Config:
    """
    Содержит настройки путей к файлам и параметры игры.
    
    Attributes:
        WORDS_FILE_PATH (Path): Путь к файлу со словами для игры
        MAX_ATTEMPTS (int): Максимальное количество попыток (ошибок)
    """
    WORDS_FILE_PATH = Path(__file__).parent / "words.txt"
    MAX_ATTEMPTS = 6
