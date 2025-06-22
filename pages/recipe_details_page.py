import re

import allure

from locators.locators import RECIPE_DETAILS_NAME
from pages.base_page import BasePage
from urls.urls import BASE_URL_FRONT, RECIPIE_DETAILS_PAGE


class RecipeDetailsPage(BasePage):
    page_url = f'{BASE_URL_FRONT}{RECIPIE_DETAILS_PAGE}'

    @allure.step('Проверить, что открыта страница деталей рецепта')
    def current_url_is_recipe_details(self):

        pattern = re.compile(rf"^{re.escape(self.page_url)}\d+$")

        return self.wait_for_current_url_match_pattern(pattern)


    @allure.step('Получить заголовок страницы')
    def get_page_header(self):
        return self.get_element_by_xpath(RECIPE_DETAILS_NAME).text


