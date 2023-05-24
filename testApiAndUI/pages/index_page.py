from playwright.async_api import Page
from testApiAndUI import config


class IndexPage:
    def open_index_page(self, page: Page) -> None:
        # Открываем нужный нам URL.
        page.goto(config.URL.DOMAIN)




