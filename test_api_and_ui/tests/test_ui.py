import json
import time

from test_api_and_ui.pages import main_page
import requests

URL = 'https://reqres.in'

BUTTON_LIST_USERS = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[1]'
BUTTON_SINGLE_USER = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[2]/a'
BUTTON_SINGLE_USER_NOT_FOUND = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[6]'
BUTTON_CREATE_USER = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[7]'
BUTTON_UPDATE_PUT_USER = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[8]'
BUTTON_UPDATE_PATCH_USER = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[9]'
BUTTON_DELETE_USER = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[10]'
BUTTON_REGISTER_SUCCESSFUL = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[11]'
BUTTON_REGISTER_UNSUCCESSFUL = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[12]'
BUTTON_LOGIN_SUCCESSFUL = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[13]'
BUTTON_LOGIN_UNSUCCESSFUL = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[14]/a'

class TestUsersUi:
    def test_get_list_users_through_browser(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_LIST_USERS)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = json.loads(main_page.get_the_body_from_main_page(page))
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.get(f'{URL}{text_of_link_to_api}')
        assert browser_status_code_after_click_button == 200
        assert browser_status_code_after_click_button == api_response.status_code
        assert browser_body_after_click_button == api_response.json()
        assert data_from_browser_after_click_link.status == 200
        assert browser_text_from_html_page_after_click_link == api_response.text

    def test_get_single_user_success_through_browser(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_SINGLE_USER)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = json.loads(main_page.get_the_body_from_main_page(page))
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.get(f'{URL}{text_of_link_to_api}')
        assert browser_status_code_after_click_button == 200
        assert browser_status_code_after_click_button == api_response.status_code
        assert browser_body_after_click_button == api_response.json()
        assert data_from_browser_after_click_link.status == 200
        assert browser_text_from_html_page_after_click_link == api_response.text

    def test_get_single_user_not_found_through_browser(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_SINGLE_USER_NOT_FOUND)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = json.loads(main_page.get_the_body_from_main_page(page))
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.get(f'{URL}{text_of_link_to_api}')
        assert browser_status_code_after_click_button == 404
        assert browser_status_code_after_click_button == api_response.status_code
        assert browser_body_after_click_button == api_response.json()
        assert data_from_browser_after_click_link.status == 404
        assert browser_text_from_html_page_after_click_link == api_response.text

    def test_create_user_through_browser(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_CREATE_USER)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = json.loads(main_page.get_the_body_from_main_page(page))
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.post(f'{URL}{text_of_link_to_api}', data={"name": "morpheus", "job": "leader"})
        assert browser_status_code_after_click_button == 201
        assert browser_status_code_after_click_button == api_response.status_code
        assert browser_body_after_click_button["name"] == api_response.json()["name"]
        assert browser_body_after_click_button["job"] == api_response.json()["job"]
        assert browser_body_after_click_button["id"] is not None
        assert browser_body_after_click_button["createdAt"] is not None
        assert data_from_browser_after_click_link.status == 200
        assert browser_text_from_html_page_after_click_link == requests.get(f'{URL}/api/users?page=1').text

    def test_update_user_throw_browser_put(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_UPDATE_PUT_USER)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = json.loads(main_page.get_the_body_from_main_page(page))
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.put(f'{URL}{text_of_link_to_api}', data={"name": "morpheus", "job": "zion resident"})
        assert browser_status_code_after_click_button == 200
        assert browser_status_code_after_click_button == api_response.status_code
        assert browser_body_after_click_button["name"] == api_response.json()["name"]
        assert browser_body_after_click_button["job"] == api_response.json()["job"]
        assert browser_body_after_click_button["updatedAt"] is not None
        assert data_from_browser_after_click_link.status == 200
        assert browser_text_from_html_page_after_click_link == requests.get(f'{URL}/api/users/2').text

    def test_update_user_throw_browser_patch(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_UPDATE_PATCH_USER)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = json.loads(main_page.get_the_body_from_main_page(page))
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.patch(f'{URL}{text_of_link_to_api}', data={"name": "morpheus", "job": "zion resident"})
        assert browser_status_code_after_click_button == 200
        assert browser_status_code_after_click_button == api_response.status_code
        assert browser_body_after_click_button["name"] == api_response.json()["name"]
        assert browser_body_after_click_button["job"] == api_response.json()["job"]
        assert browser_body_after_click_button["updatedAt"] is not None
        assert data_from_browser_after_click_link.status == 200
        assert browser_text_from_html_page_after_click_link == requests.get(f'{URL}/api/users/2').text

    def test_delete_user_throw_browser(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_DELETE_USER)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = main_page.get_the_body_from_main_page(page)
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.delete(f'{URL}{text_of_link_to_api}')
        assert browser_status_code_after_click_button == 204
        assert browser_status_code_after_click_button == api_response.status_code
        assert browser_body_after_click_button == ''
        assert data_from_browser_after_click_link.status == 200
        assert browser_text_from_html_page_after_click_link == requests.get(f'{URL}/api/users/2').text


class TestRegistrationUI:
    def test_register_successful_through_browser(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_REGISTER_SUCCESSFUL)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = json.loads(main_page.get_the_body_from_main_page(page))
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.post(f'{URL}{text_of_link_to_api}', data={'email': 'eve.holt@reqres.in',
                                                                          'password': 'pistol'})
        assert browser_status_code_after_click_button == 200
        assert browser_status_code_after_click_button == api_response.status_code
        assert browser_body_after_click_button["id"] is not None
        assert browser_body_after_click_button["token"] is not None
        assert data_from_browser_after_click_link.status == 200
        assert browser_text_from_html_page_after_click_link == requests.get(f'{URL}/api/register').text

    def test_register_unsuccessful_through_browser(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_REGISTER_UNSUCCESSFUL)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = json.loads(main_page.get_the_body_from_main_page(page))
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.post(f'{URL}{text_of_link_to_api}', data={'email': 'eve.holt@reqres.in'})
        assert browser_status_code_after_click_button == 400
        assert browser_status_code_after_click_button == api_response.status_code

        assert browser_body_after_click_button == api_response.json()
        assert data_from_browser_after_click_link.status == 200
        assert browser_text_from_html_page_after_click_link == requests.get(f'{URL}/api/register').text


class TestLoginUI:
    def test_login_successful_through_browser(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_LOGIN_SUCCESSFUL)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = json.loads(main_page.get_the_body_from_main_page(page))
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.post(f'{URL}{text_of_link_to_api}', data={'email': 'eve.holt@reqres.in',
                                                                          'password': 'cityslicka'})
        assert browser_status_code_after_click_button == 200
        assert browser_status_code_after_click_button == api_response.status_code
        assert browser_body_after_click_button["token"] is not None
        assert data_from_browser_after_click_link.status == 200
        assert browser_text_from_html_page_after_click_link == requests.get(f'{URL}/api/login').text

    def test_login_unsuccessful_through_browser(self, page):
        main_page.open_main_page(page)
        main_page.find_and_click_the_button(page, BUTTON_LOGIN_UNSUCCESSFUL)
        time.sleep(10)
        text_of_link_to_api = main_page.get_the_text_from_the_link(page)
        browser_status_code_after_click_button = int(main_page.get_the_code_from_main_page(page))
        browser_body_after_click_button = json.loads(main_page.get_the_body_from_main_page(page))
        main_page.click_link_to_api(page)
        data_from_browser_after_click_link = page.reload()
        browser_text_from_html_page_after_click_link = main_page.get_the_text_from_html_page_after_click_link(page)
        api_response = requests.post(f'{URL}{text_of_link_to_api}', data={'email': 'peter@klaven'})
        assert browser_status_code_after_click_button == 400
        assert browser_status_code_after_click_button == api_response.status_code
        assert browser_body_after_click_button == api_response.json()
        assert data_from_browser_after_click_link.status == 200
        assert browser_text_from_html_page_after_click_link == requests.get(f'{URL}/api/login').text



