from playwright.async_api import Page
from testApiAndUI import config


class IndexPage:
    LINK_TO_API = '//html/body/div[2]/div/div/section[1]/div[2]/div[1]/p/strong/a/span'
    LOCATOR_OF_DATA_TO_RESPONSE = '//html/body'

    def open_index_page(self, page: Page):
        # Открываем главную страницу.
        page.goto(config.URL.DOMAIN,)

    def find_and_press_the_desired_button(self, page: Page, button: str) -> None:
        # Найти и нажать нужную кнопку.
        page.locator(button).click()

    def get_the_text_from_link(self, page: Page):
        # вернуть текст ссылки для перехода на страницу с json.
        text_from_link = page.locator(self.LINK_TO_API).text_content()
        return text_from_link

    def press_link_to_api(self, page: Page):
        # Нажать на ссылку для перехода на страницу с json.
        page.locator(self.LINK_TO_API).click()

    def get_the_text_after_ui_click(self, page: Page):
        text_after_ui_click = page.locator(self.LOCATOR_OF_DATA_TO_RESPONSE).text_content()
        return text_after_ui_click





