from testApiAndUI.pages import index_page
import requests

URL = 'https://reqres.in'

BUTTON_LIST_USERS = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[1]'
BUTTON_SINGLE_USER = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[2]/a'
BUTTON_SINGLE_USER_NOT_FOUND = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[6]'


class TestUI:

    def test_get_list_users_by_ui(self, page):
        index_page.open_index_page(page)
        index_page.find_and_press_the_desired_button(page, BUTTON_LIST_USERS)
        text_of_link_to_api = index_page.get_the_text_from_link(page)
        index_page.press_link_to_api(page)
        ui_response = index_page.get_the_text_after_ui_click(page)
        ui_status_code = page.reload().status
        api_response = requests.get(f'{URL}{text_of_link_to_api}')
        assert ui_status_code == 200
        assert ui_status_code == api_response.status_code
        assert ui_response == api_response.text

    def test_get_single_user_success_by_ui(self, page):
        index_page.open_index_page(page)
        index_page.find_and_press_the_desired_button(page, BUTTON_SINGLE_USER)
        text_of_link_to_api = index_page.get_the_text_from_link(page)
        index_page.press_link_to_api(page)
        ui_response = index_page.get_the_text_after_ui_click(page)
        ui_status_code = page.reload().status
        api_response = requests.get(f'{URL}{text_of_link_to_api}')
        assert ui_status_code == 200
        assert ui_status_code == api_response.status_code
        assert ui_response == api_response.text

    def test_get_single_user_not_found(self, page):
        index_page.open_index_page(page)
        index_page.find_and_press_the_desired_button(page, BUTTON_SINGLE_USER_NOT_FOUND)
        text_of_link_to_api = index_page.get_the_text_from_link(page)
        index_page.press_link_to_api(page)
        ui_response = index_page.get_the_text_after_ui_click(page)
        ui_status_code = page.reload().status
        api_response = requests.get(f'{URL}{text_of_link_to_api}')
        assert ui_status_code == 404
        assert ui_status_code == api_response.status_code
        assert ui_response == api_response.text










