from testApiAndUI.pages import index_page
from .test_api import TestSingleUser


BUTTON_LIST_USERS = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[1]'
BUTTON_SINGLE_USER = '//html/body/div[2]/div/div/section[1]/div[1]/ul/li[2]/a'


class TestUI:

    def test_list_of_users(self, page):
        # Открыть главную страницу
        index_page.open_index_page(page)
        index_page.find_and_press_the_desired_button(page, BUTTON_SINGLE_USER)
        index_page.press_link_to_api(page)
        result_from_ui = index_page.get_and_return_the_json_data(page)

        result_from_api = TestSingleUser().test_get_one_user_success(2, 'Janet', 'Weaver')
        print('result_FROM-API', result_from_api)
        assert result_from_api == result_from_ui




        # actual_result = index_page.press_list_users(page)
        #
        # print(actual_result)
        #
        #
        # assert actual_result == None





