from api_client.http_client import HttpMethods


class SignupService:
    SIGNUP_ENDPOINT = "/api/users/"
    SIGNIN_ENDPOINT = "/api/auth/token/login/"

    def __init__(self, http_client):
        self.http_client = http_client

    def signup_request(self, payload):
        return self.http_client.send_request(HttpMethods.POST, self.SIGNUP_ENDPOINT, json=payload, headers={'Content-Type': 'application/json'})

    def signin_request(self, payload):
        return self.http_client.send_request(HttpMethods.POST, self.SIGNIN_ENDPOINT, json=payload, headers={'Content-Type': 'application/json'})


    @staticmethod
    def build_signup_payload(email, password, username, first_name, last_name):
        payload = {"email":email,
                   "password":password,
                   "username":username,
                   "first_name":first_name,
                   "last_name":last_name}
        return payload


    @staticmethod
    def build_signin_payload(email, password):
        payload = {"email":email,
                   "password":password}
        return payload