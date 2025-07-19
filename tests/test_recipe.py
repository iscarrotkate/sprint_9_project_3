import allure

from resources.test_data import recipe_1


class TestRecipe:

    @allure.title('Создание рецепта')
    @allure.description('В тесте проверяется, что после заполнения формы создания рецепта открывается карточка рецепта с указанным при создании названием')
    def test_create_recipe(self, set_token, recipes_page, header_page, create_recipe_page, recipe_details_page):

        recipes_page.open_page_by_direct_url()

        header_page.click_on_tab_option('Создать рецепт')
        create_recipe_page.fill_create_recipe_form(recipe_1)
        create_recipe_page.click_on_create_recipe_button()

        assert recipe_details_page.current_url_is_recipe_details()
        assert recipe_details_page.get_page_header() == recipe_1['name']
