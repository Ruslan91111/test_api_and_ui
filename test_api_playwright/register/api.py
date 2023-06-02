import logging
from jsonschema import validate

from test_api_playwright.requests import Client
from .models import ResponseModel


logger = logging.getLogger("api")


class Register:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_REGISTER_USER = 'users'

    def register_user(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.POST_REGISTER_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, body=response.json())





