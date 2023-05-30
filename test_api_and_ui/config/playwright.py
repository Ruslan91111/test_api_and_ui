"""Параметры браузера."""
import os


class Playwright:
    PAGE_VIEWPORT_SIZE = {'width': 1920, 'height': 1080}
    ENV = os.getenv('ENV') if os.getenv('ENV') is not None else 'stage'
    BROWSER = os.getenv('BROWSER') if os.getenv('BROWSER') is not None else 'firefox'
    # Параметр HEADLESS определяет - будет ли виден браузер во время тестирования.
    IS_HEADLESS = os.getenv('HEADLESS') if os.getenv('HEADLESS') is not None else False
    # Параметр SlowMo: замедленное движение: уменьшает скорость переключения между действиями на странице, значение в мс
    SLOW_MO = int(os.getenv('SLOW_MO')) if os.getenv('SLOW_MO') is not None else 50
    LOCALE = 'en-US'


