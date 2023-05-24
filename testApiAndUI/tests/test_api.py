import json

import pytest
import requests


# Константа - url сайта.
URL = 'https://reqres.in/api/'


class TestListUsers:
    """Проверить выдачу результатов при обращении к API со списком пользователей"""
    def test_get_list_users(self):
        # Получаем ответ при обращении к первой страницы.
        response_from_first_page = requests.get(f'{URL}users?page=1')
        assert response_from_first_page.status_code == 200  # Статус соединения.
        assert response_from_first_page.json().get('page') == 1  # Номер страницы.
        assert response_from_first_page.json().get('per_page') == 6  # Пагинация.

        # Получаем ответ при обращении ко второй странице.
        response_from_second_page = requests.get(f'{URL}users?page=2')
        assert response_from_second_page.status_code == 200
        assert response_from_second_page.json().get('page') == 2
        assert response_from_second_page.json().get('per_page') == 6

        # Данные полученные при обращении к первой и ко второй страницам должны отличаться друг от друга.
        assert response_from_first_page.json()['data'] != response_from_second_page.json()['data']

        # Высчитываем номер последней страницы и проверяем, что она возвращает пустой список.
        total_count_of_items = response_from_second_page.json().get('total')
        per_page_count_of_items = response_from_second_page.json().get('per_page')
        last_page = total_count_of_items / per_page_count_of_items + 1
        response_from_last_page = requests.get(f'{URL}users?page={last_page}')
        assert response_from_last_page.json()['data'] == []

        # При передаче в запросе на список пользователей вместо int строки должна вернуться первая страница.
        response_when_instead_of_int_str = requests.get(f'{URL}users?page=some_string')
        assert response_when_instead_of_int_str.status_code == 200  # Статус соединения.
        assert response_when_instead_of_int_str.json().get('page') == 1  # Номер страницы.


class TestSingleUser:
    """Проверить API с одним пользователем."""
    @pytest.mark.parametrize("id, first_name, last_name",
                             [(1, 'George', 'Bluth'), (2, 'Janet', 'Weaver'), (3, 'Emma', 'Wong')])
    def test_get_one_user_success(self, id: int, first_name: str, last_name: str) -> None:
        # Получить пользователя по id и проверить содержимое ответа.
        response = requests.get(f'{URL}users/{id}')
        assert response.status_code == 200
        assert response.json()["data"]["id"] == id
        assert response.json()["data"]["first_name"] == first_name
        assert response.json()["data"]["last_name"] == last_name

    @pytest.mark.parametrize("wrong_id, status_code",
                             [(23, 404), (1000, 404), ('some_string', 404)])
    def test_get_one_user_wrong_id(self, wrong_id: int | str, status_code: int) -> None:
        # Передать неверный id.
        response = requests.get(f'{URL}users/{wrong_id}')
        assert response.status_code == status_code
        assert response.json() == {}

    @pytest.mark.parametrize("data_for_post",
                             [{"name": "morpheus", "job": "leader"}, {"name": "connor", "job": "hero"}])
    def test_create_user(self, data_for_post: dict) -> None:
        response = requests.post(f'{URL}users', data=data_for_post)
        assert response.status_code == 201
        assert response.json()["name"] == data_for_post["name"]
        assert response.json()["job"] == data_for_post["job"]
        assert response.json()["id"] is not None
        assert response.json()["createdAt"] is not None

    @pytest.mark.parametrize("user_id, data_for_put",
                             [(1, {"name": "new_morpheus", "job": "new_president"}),
                              (2, {"name": "new_connor", "job": "new_hero"}),
                              (3, {"name": "john", "job": "lawyer"})])
    def test_update_user_put(self, user_id: int, data_for_put: dict) -> None:
        response = requests.put(f'{URL}users/{user_id}', data=data_for_put)
        assert response.status_code == 200
        assert response.json()["name"] == data_for_put["name"]
        assert response.json()["job"] == data_for_put["job"]
        assert response.json()["updatedAt"] is not None

    @pytest.mark.parametrize("user_id, data_for_patch",
                             [(1, {"job": "new_president"}), (2, {"job": "new_hero"}), (3, {"job": "lawyer"})])
    def test_update_user_patch(self, user_id: int, data_for_patch: dict) -> None:
        response = requests.patch(f'{URL}users/{user_id}', data=data_for_patch)
        assert response.status_code == 200
        assert response.json()["job"] == data_for_patch["job"]
        assert response.json()["updatedAt"] is not None

    @pytest.mark.parametrize("user_id", [(1, ), (2, ), (300, )])
    def test_delete_user(self, user_id: int) -> None:
        response = requests.delete(f'{URL}users/{user_id}')
        assert response.status_code == 204


class TestRegistration:
    """Проверить регистрацию пользователя."""
    @pytest.mark.parametrize("data_for_registration, status_code, result",
                             [
                                 ({'email': 'eve.holt@reqres.in', 'password': 'pistol'}, 200, 'id'),
                                 ({'email': 'rus.holt@reqres.in', 'password': 'password'}, 400,
                                  'Only defined users succeed registration'),
                                 ({'email': '', 'password': 'password'}, 400, 'Missing email or username'),
                                 ({'email': 'Max@mail.com', 'password': ''}, 400, 'Missing password'),
                                 ({'email': '', 'password': ''}, 400, 'Missing email or username')
                             ])
    def test_registrate(self, data_for_registration: dict, status_code: int, result: str) -> None:
        # Проверка на правильность ввода данных.
        response = requests.post(f'{URL}register/', data=data_for_registration)
        assert response.status_code == status_code
        assert result in response.text


class TestLogin:
    """Проверить вход пользователя."""
    @pytest.mark.parametrize("data_for_login, status_code, result",
                             [
                                 ({'email': 'eve.holt@reqres.in', 'password': 'pistol'}, 200, 'token'),
                                 ({'email': 'rus.holt@reqres.in', 'password': 'password'}, 400, 'user not found'),
                                 ({'email': '', 'password': 'password'}, 400, 'Missing email or username'),
                                 ({'email': 'Max@mail.com', 'password': ''}, 400, 'Missing password'),
                                 ({'email': '', 'password': ''}, 400, 'Missing email or username')
                             ])
    def test_registrate(self, data_for_login: dict, status_code: int, result: str) -> None:
        # Проверка на правильность ввода данных.
        response = requests.post(f'{URL}login/', data=data_for_login)
        assert response.status_code == status_code
        assert result in response.text







