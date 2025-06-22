import allure

class TestRegistration:

    @allure.title('Открытие страницы авторизации после регистрации нового пользователя')
    @allure.description('В тесте проверяется, произошёл ли переход на страницу авторизации, отображается ли форма авторизации.')
    def test_registration_with_valid_data(self, signup_page, signin_page):

        signup_page.open_page_by_direct_url()
        signup_page.fill_in_signup_form()
        signup_page.click_on_signup_button()

        assert signin_page.is_expected_url()
        assert signin_page.is_displayed_sigin_form()


    @allure.title('Открытие главной страницы при успешной авторизации')
    @allure.description('В тесте проверяется, произошёл ли переход на главную страницу, отображается ли кнопка «Выход»')
    def test_authorization_with_valid_data(self, header_page, signin_data, signin_page, recipes_page):

        signin_page.open_page_by_direct_url()
        signin_page.fill_in_signin_form(signin_data["email"], signin_data["password"])

        signin_page.click_on_signin_button()

        assert recipes_page.is_expected_url()
        assert recipes_page.is_displayed_header()
