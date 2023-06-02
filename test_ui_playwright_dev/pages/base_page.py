"""BasePage - абстрактный класс, не описывает какую-то конкретную страницу или компонент,
а описывает базовые методы работы со страницей. Сама BasePage не используется в тестах,
она наследуется конкретными страницами."""
import allure
from playwright.sync_api import Page, Response
from abc import ABC

from test_ui_playwright_dev.components.navbar import Navbar


class BasePage(ABC):
    def __init__(self, page: Page) -> None:
        self.page = page
        self.navbar = Navbar(page)

    def visit(self, url: str) -> Response | None:
        with allure.step(f'Opening the url "{url}"'):
            return self.page.goto(url, wait_until='networkidle')

    def reload(self) -> Response | None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')

