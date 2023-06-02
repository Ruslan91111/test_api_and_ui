from ..register.api import Register
from ..register.models import RegisterUser
from ..schemas.registration import valid_schema


URL = 'https://reqres.in/api/'


class TestRegistration:
    def test_registration(self):
        body = RegisterUser.random()
        response = Register(url=URL).register_user(body=body, schema=valid_schema)
        assert response.status_code == 201
        assert response.json().get('name') == body["name"]
        assert response.json().get("job") == body["job"]
        assert response.json().get("id")
        assert response.json().get("createdAt")



