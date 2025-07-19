import allure

from locators.locators import SIGNIN_HEADER, SIGNIN_LOGIN_BUTTON, SIGNIN_PASSWORD_INPUT, SIGNIN_EMAIL_INPUT
from pages.base_page import BasePage
from urls.urls import BASE_URL_FRONT, SIGNIN_PAGE


class SigninPage(BasePage):
    page_url = f'{BASE_URL_FRONT}{SIGNIN_PAGE}'

    @allure.step('Открыть страницу авторизации')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Проверить отображение элементов формы авторизации')
    def is_displayed_sigin_form(self):
        elements = [
            self.element_is_displayed_by_xpath(SIGNIN_HEADER),
            self.element_is_displayed_by_xpath(SIGNIN_LOGIN_BUTTON),
            self.element_is_displayed_by_xpath(SIGNIN_PASSWORD_INPUT)
        ]
        return all(elements)


    @allure.step('Текущий URL соответсвует URL страницы авторизации')
    def is_expected_url(self):
        return super().is_expected_url(self.page_url)


    @allure.step('Заполнить форму авторизации')
    def fill_in_signin_form(self, email, password):
        self.fill_input_element_with_value(SIGNIN_EMAIL_INPUT, email)
        self.fill_input_element_with_value(SIGNIN_PASSWORD_INPUT, password)

    @allure.step('Кликнуть по ссылке "Войти"')
    def click_on_signin_button(self):
        self.click_on_element_by_xpath(SIGNIN_LOGIN_BUTTON)