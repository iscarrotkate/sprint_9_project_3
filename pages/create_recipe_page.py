import allure

from helpers.helpers import get_resource_path
from locators.locators import CREATE_RECIPE_TAGS, CREATE_RECIPE_INGREDIENT_INPUT, CREATE_RECIPE_INGREDIENT_DROPDOWN, \
    CREATE_RECIPE_ADD_INGREDIENT_BUTTON, CREATE_RECIPE_INGREDIENT_QNT, CREATE_RECIPE_NAME, CREATE_RECIPE_DURATION, \
    CREATE_RECIPE_DESCRIPTION, CREATE_RECIPE_IMAGE_INPUT, CREATE_RECIPE_CREATE_BUTTON
from pages.base_page import BasePage
from urls.urls import BASE_URL_FRONT, CREATE_RECIPIE_PAGE


class CreateRecipePage(BasePage):
    page_url = f'{BASE_URL_FRONT}{CREATE_RECIPIE_PAGE}'

    @allure.step('Открыть страницу рецептов')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)


    @allure.step('Сбросить тэги по умолчанию')
    def clear_default_tags(self):
        tags = self.get_list_of_elements_by_xpath(CREATE_RECIPE_TAGS)
        for tag in tags:
            tag.click()


    @allure.step('Выбрать тэг по индексу')
    def select_tag_by_index(self, index):
        tags = self.get_list_of_elements_by_xpath(CREATE_RECIPE_TAGS)
        self.click_on_element_by_index(tags, index)


    @allure.step('Добавить ингредиент по первому совпадению')
    def add_ingredient_by_first_match(self, name, qnt):
        input = self.get_element_by_xpath(CREATE_RECIPE_INGREDIENT_INPUT)

        self.type_slowly(input, name)
        ingredient = self.get_list_of_child_elements_by_xpath(CREATE_RECIPE_INGREDIENT_DROPDOWN)
        self.click_on_element_by_index(ingredient, 0)

        self.fill_input_element_with_value(CREATE_RECIPE_INGREDIENT_QNT, qnt)

        self.click_on_element_by_xpath(CREATE_RECIPE_ADD_INGREDIENT_BUTTON)


    @allure.step('Ввести название рецепта')
    def fill_recipe_name(self, name):
        self.fill_input_element_with_value(CREATE_RECIPE_NAME, name)


    @allure.step('Ввести время приготовления блюда')
    def fill_recipe_duration(self, duration):
        self.fill_input_element_with_value(CREATE_RECIPE_DURATION, duration)


    @allure.step('Ввести описание рецепта')
    def fill_recipe_description(self, text):
        self.fill_input_element_with_value(CREATE_RECIPE_DESCRIPTION, text)


    @allure.step('Выбрать изображение блюда')
    def set_recipe_image(self, image_path):
        file_input = self.get_hidden_element_by_xpath(CREATE_RECIPE_IMAGE_INPUT)

        file_path = get_resource_path(image_path)

        file_input.send_keys(file_path)


    @allure.step('Заполнить форму создания рецепта')
    def fill_create_recipe_form(self, recipe_data):

        name = recipe_data['name']
        tags = recipe_data['tags']
        ingredients = recipe_data['ingredients']
        time = recipe_data['time']
        description = recipe_data['description']
        image = recipe_data['image']

        self.clear_default_tags()

        self.fill_recipe_name(name)

        for tag in tags:
            self.select_tag_by_index(tag)

        for ingredient in ingredients:
            self.add_ingredient_by_first_match(ingredient['name'], ingredient['qnt'])

        self.fill_recipe_duration(time)
        self.fill_recipe_description(description)
        self.set_recipe_image(image)


    @allure.step('Кликнуть по кнопке "Создать рецепт"')
    def click_on_create_recipe_button(self):
        self.click_on_element_by_xpath(CREATE_RECIPE_CREATE_BUTTON)

