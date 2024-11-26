import allure
from data import URLs, DEFAULT_WAIT_TIME
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    timeout = DEFAULT_WAIT_TIME
    url = URLs.BASE_URL

    @staticmethod
    def format_locators(locator_before_format, num):
        method, locator = locator_before_format
        locator = locator.format(num)
        return method, locator

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие веб-страницы.')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Получение текущего адреса веб-страницы.')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Поиск элемента с ожиданием.')
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Определение доступности элемента.')
    def element_is_available(self, locator):
        try:
            self.find_element_with_wait(locator)
        except TimeoutException:
            return False
        return True

    @allure.step('Клик по элементу с ожиданием.')
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Клик по элементу с ожиданием (при помощи js-скрипта).')
    def click_to_element_by_script(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script('arguments[0].click();', element)

    @allure.step('Ожидание появления кликабельности элемента.')
    def find_element_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Получение текста элемента.')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Запись текста в элемент.')
    def send_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('Скролл до элемента.')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем выполнения перехода на веб страницу, 0 - на текущей вкладке; 1 - редирект на другой вкладке.')
    def wait_for_redirect(self, expected_url, n=0):
        WebDriverWait(self.driver, self.timeout).until(lambda driver: len(driver.window_handles) != n)
        self.driver.switch_to.window(self.driver.window_handles[n])
        WebDriverWait(self.driver, self.timeout).until(lambda driver: expected_url in self.driver.current_url)

    @allure.step('Получение определённое кол-ва элементов с ожиданием.')
    def find_all_elements_with_wait(self, locator, n):
        WebDriverWait(self.driver, self.timeout).until(lambda driver: len(driver.find_elements(*locator)) == n)
        return self.driver.find_elements(*locator)

    @allure.step('Получение элементов без ожидания.')
    def find_all_elements_without_wait(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Ожидание появления определённого текста в элементе.')
    def wait_before_text_change(self, locator, def_value):
        WebDriverWait(self.driver, self.timeout).until(lambda driver: self.get_text_from_element(locator) != def_value)

    @allure.step('Drag and drop для браузеров firefox / chrome.')
    def drag_and_drop_element(self, locator_from, locator_to):
        element_from = self.find_element_with_wait(locator_from)
        element_to = self.find_element_with_wait(locator_to)

        self.driver.execute_script("""
               var source = arguments[0];
               var target = arguments[1];
               var evt = document.createEvent("DragEvent");
               evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
               source.dispatchEvent(evt);
               evt = document.createEvent("DragEvent");
               evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
               target.dispatchEvent(evt);

               evt = document.createEvent("DragEvent");
               evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
               target.dispatchEvent(evt);
               evt = document.createEvent("DragEvent");
               evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
               target.dispatchEvent(evt);
               evt = document.createEvent("DragEvent");
               evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
               source.dispatchEvent(evt);
            """, element_from, element_to)



