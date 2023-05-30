"""Работа с главной страницей, на которой расположены кнопки для отправки соответствующего запроса."""
from typing import Any, Coroutine, Dict
from playwright.async_api import Page
from test_api_and_ui import config


class MainPage:
    LINK_TO_API = '//html/body/div[2]/div/div/section[1]/div[2]/div[1]/p/strong/a/span'
    LOCATOR_RESPONSE_STATUS_CODE_FROM_PAGE = '//html/body/div[2]/div/div/section[1]/div[2]/div[2]/p/strong/span'
    LOCATOR_RESPONSE_BODY_FROM_PAGE = '//html/body/div[2]/div/div/section[1]/div[2]/div[2]/pre'
    LOCATOR_OF_TEXT_FROM_PAGE_AFTER_CLICK = '//html/body'

    def open_main_page(self, page: Page) -> None:
        # Открыть главную страницу.
        page.goto(config.URL.DOMAIN,)

    def find_and_click_the_button(self, page: Page, button: str) -> None:
        # Найти и нажать нужную кнопку.
        page.locator(button).click()

    def get_the_text_from_the_link(self, page: Page) -> Coroutine[Any, Any, str | None]:
        # вернуть текст ссылки для перехода на страницу с json.
        return page.text_content(self.LINK_TO_API)

    def get_the_code_from_main_page(self, page: Page) -> Coroutine[Any, Any, str | None]:
        # Текст кода и тела ответа с главной страницы.
        return page.text_content(self.LOCATOR_RESPONSE_STATUS_CODE_FROM_PAGE)

    def get_the_body_from_main_page(self, page: Page) -> Coroutine[Any, Any, str | None]:
        # Текст кода и тела ответа с главной страницы.
        return page.text_content('//html/body/div[2]/div/div/section[1]/div[2]/div[2]/pre')

    def click_link_to_api(self, page: Page, link: str = LINK_TO_API):
        # Нажать на ссылку для перехода на страницу с json.
        page.locator(link).click()

    def get_the_text_from_html_page_after_click_link(self, page: Page) -> Coroutine[Any, Any, str | None]:
        return page.text_content(self.LOCATOR_OF_TEXT_FROM_PAGE_AFTER_CLICK)





