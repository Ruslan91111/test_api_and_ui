from faker import Faker


fake = Faker()


class RegisterUser:
    @staticmethod
    def random():
        name = fake.name()
        job = fake.job()
        return {"name": name, "job": job}


class ResponseModel:
    def __init__(self, status: int, body: dict = None):
        self.status = status
        self.body = body



