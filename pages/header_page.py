import allure

from locators.locators import HEADER_SIGNIN_BUTTON, RECIPIES_MENU
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Кликнуть по ссылке "Войти"')
    def click_on_signin_button(self):
        self.click_on_element_by_xpath(HEADER_SIGNIN_BUTTON)


    @allure.step('Кликнуть по табу')
    def click_on_tab_option(self, tab_name):
        tabs = self.get_list_of_elements_by_xpath(RECIPIES_MENU)

        for tab in tabs:
            if tab.text == tab_name:
                return tab.click()

        raise Exception(f"Не удалось найти вкладку с текстом '{tab_name}'")