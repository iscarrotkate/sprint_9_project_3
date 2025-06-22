import allure

from locators.locators import RECIPIES_HEADER
from pages.base_page import BasePage
from urls.urls import BASE_URL_FRONT, RECIPIES_PAGE


class RecipesPage(BasePage):
    page_url = f'{BASE_URL_FRONT}{RECIPIES_PAGE}'

    @allure.step('Открыть страницу рецептов')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Текущий URL соответсвует URL страницы рецептов')
    def is_expected_url(self):
        return super().is_expected_url(self.page_url)

    @allure.step('Проверить отображение элементов формы авторизации')
    def is_displayed_header(self):
        return self.element_is_displayed_by_xpath(RECIPIES_HEADER),
