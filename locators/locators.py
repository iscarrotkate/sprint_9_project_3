SIGNIN_HEADER = "//h1[contains(text(),'Войти на сайт')]"
SIGNIN_EMAIL_INPUT = "//input[@name='email']"
SIGNIN_PASSWORD_INPUT = "//input[@name='password']"
SIGNIN_LOGIN_BUTTON = "//button[contains(text(),'Войти')]"

SIGNUP_FIRSTNAME_INPUT = "//input[@name='first_name']"
SIGNUP_LASTNAME_INPUT = "//input[@name='last_name']"
SIGNUP_USERNAME_INPUT = "//input[@name='username']"
SIGNUP_EMAIL_INPUT = "//input[@name='email']"
SIGNUP_PASSWORD_INPUT = "//input[@name='password']"
SIGNUP_CREATE_ACCOUNT_BUTTON = "//button[contains(text(),'Создать аккаунт')]"

HEADER_SIGNIN_BUTTON = "//a[contains(text(),'Войти')]"

RECIPIES_HEADER = "//h1[contains(text(),'Рецепты')]"
RECIPIES_MENU = "//li[contains(@class, 'style_nav')]"

CREATE_RECIPE_NAME = "//div[text()='Название рецепта']/following-sibling::input"
CREATE_RECIPE_TAGS = "//div[contains(text(), 'Теги')]/ancestor::div//button[contains(@class, 'styles_checkbox')]"
CREATE_RECIPE_INGREDIENT_INPUT = "//input[contains(@class, 'ingredientsInput')]"
CREATE_RECIPE_INGREDIENT_DROPDOWN = "//div[contains(@class, 'styles_container')]"
CREATE_RECIPE_ADD_INGREDIENT_BUTTON = "//div[contains(@class, 'ingredientAdd') and text()='Добавить ингредиент']"
CREATE_RECIPE_INGREDIENT_QNT = "//input[contains(@class, 'ingredientsAmount')]"
CREATE_RECIPE_DURATION = "//div[contains(text(),'Время приготовления')]/following-sibling::input"
CREATE_RECIPE_DESCRIPTION = "//div[contains(text(),'Описание рецепта')]/following-sibling::textarea"
CREATE_RECIPE_IMAGE_INPUT = "//input[contains(@class, 'styles_fileInput')]"
CREATE_RECIPE_CREATE_BUTTON = "//button[contains(text(),'Создать рецепт')]"

RECIPE_DETAILS_NAME = "//h1[contains(@class, 'styles_single-card__title')]"