import allure
import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import url_to_be
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу по прямому URL')
    def open_page_by_direct_url(self, url):
        self.driver.get(url)

    @allure.step('Ждать указанный таймаут')
    def wait_for_timeout(self, timeout):
        time.sleep(timeout)

    def type_slowly(self, element, text, delay=0.1):
        action = ActionChains(self.driver)
        action.click(element)
        for char in text:
            action.send_keys(char).perform()
            self.wait_for_timeout(delay)

    @allure.step('Заполнить поле для ввода значением')
    def fill_input_element_with_value(self, xpath, value):
        try:
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath))
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().send_keys(value).perform()
        except Exception as e:
            raise Exception(f"Не удалось определить видимость элемента: {str(e)}")

    @allure.step('Получить элемент по xpath')
    def get_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element(By.XPATH, xpath)
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")

    @allure.step('Получить скрытый элемент по xpath')
    def get_hidden_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath))
            )
            return self.driver.find_element(By.XPATH, xpath)
        except Exception as e:
            raise Exception(f"Не удалось найти элемент по xpath: {xpath}.")


    @allure.step('Кликнуть по элементу')
    def click_on_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            self.get_element_by_xpath(xpath).click()
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")


    @allure.step('Проверить текущий url')
    def is_expected_url(self, expected_url):
        try:
            WebDriverWait(self.driver, 10).until(url_to_be(expected_url))
            return self.driver.current_url == expected_url
        except:
            return False


    @allure.step('Проверить отображается ли элемент')
    def element_is_displayed_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element(By.XPATH, xpath).is_displayed()
        except:
            return False

    @allure.step('Установить переменную local storage')
    def set_local_storage_variable(self, key, value):
        self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")


    @allure.step('Получить список элементов по xpath')
    def get_list_of_elements_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return self.driver.find_elements(By.XPATH, xpath)
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")


    @allure.step('Получить список дочерних элементов по xpath родительского')
    def get_list_of_child_elements_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            parent = self.driver.find_element(By.XPATH, xpath)
            return parent.find_elements(By.XPATH, "./*")
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")

    @allure.step('Кликнуть на элемент по индексу')
    def click_on_element_by_index(self, elements, index):
        try:

            elements[index].click()

        except Exception:
            raise Exception(f"Не удалось выбрать элемент по индексу")

    def wait_for_current_url_match_pattern(self, pattern, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)

            def url_matches_pattern(driver):
                return bool(pattern.match(driver.current_url))

            wait.until(url_matches_pattern,
                       message="URL не соответствует ожидаемому паттерну")
            return True

        except TimeoutException:
            current_url = self.driver.current_url
            print(f"Ошибка: URL {current_url} не соответствует ожидаемому паттерну")
            return False