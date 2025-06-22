import pytest
from selenium import webdriver

from api_client.http_client import HttpClient
from api_client.account_service import SignupService
from helpers.helpers import generate_email, generate_random_string
from pages.header_page import HeaderPage
from pages.recipe_details_page import RecipeDetailsPage
from pages.recipes_page import RecipesPage
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from pages.signup_page import BasePage
from pages.create_recipe_page import CreateRecipePage
from urls.urls import BASE_URL_BACK


@pytest.fixture(scope="session")
def client():
    return HttpClient(BASE_URL_BACK)


@pytest.fixture
def account_service(client):
    return SignupService(client)

@pytest.fixture
def driver(request):
    browser = get_browser("chrome")
    try:
        yield browser
    finally:
        browser.quit()


def get_browser(browser):
    if browser == "chrome":
        return webdriver.Chrome()
    else:
        raise ValueError("Неподдерживаемый браузер")

@pytest.fixture
def signin_data(account_service):
    first_name = generate_random_string(10)
    last_name = generate_random_string(10)
    username = generate_random_string(10)
    email = generate_email()
    password = generate_random_string(10)

    payload = account_service.build_signup_payload(email, password, username, first_name, last_name)
    account_service.signup_request(payload)

    yield {"email": email, "password": password}

@pytest.fixture
def token(signin_data, account_service, base_page):

    payload = account_service.build_signin_payload(signin_data["email"], signin_data["password"])
    response = account_service.signin_request(payload)

    return response.json()["auth_token"]


@pytest.fixture
def set_token(token, signin_page):
    signin_page.open_page_by_direct_url()
    signin_page.set_local_storage_variable('token', token)

@pytest.fixture
def base_page(driver):
    return BasePage(driver)

@pytest.fixture
def signup_page(driver):
    return SignupPage(driver)

@pytest.fixture
def signin_page(driver):
    return SigninPage(driver)

@pytest.fixture
def header_page(driver):
    return HeaderPage(driver)

@pytest.fixture
def recipes_page(driver):
    return RecipesPage(driver)

@pytest.fixture
def create_recipe_page(driver):
    return CreateRecipePage(driver)


@pytest.fixture
def recipe_details_page(driver):
    return RecipeDetailsPage(driver)

