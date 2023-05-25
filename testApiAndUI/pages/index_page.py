from playwright.async_api import Page
from testApiAndUI import config


class IndexPage:
    _BUTTON_LIST_USERS = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[2]'

    def open_index_page(self, page: Page) -> None:
        # Открываем нужный нам URL.
        page.goto(config.URL.DOMAIN, )

    def get_text_from_list_users_button(self, page: Page):
        return page.locator(self._BUTTON_LIST_USERS).get_attribute('value')






