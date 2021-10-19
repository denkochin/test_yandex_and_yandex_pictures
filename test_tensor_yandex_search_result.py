import pytest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print("\nstart browser for test..")
    #global browser
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(2)
    yield browser
    print("\nquit browser..")
    # time.sleep(2)
    browser.quit()

class TestYandex():
    link = "https://yandex.ru/"
    
    # @pytest.mark.skip
    def test_yandex_main_page(self, browser):
        # 1) Зайти на yandex.ru
        link = "https://yandex.ru/"
        browser.get(link)
        # time.sleep(1)
        # 2) Проверить наличия поля поиска (is_search_box_present)
        search_box = browser.find_element(By.CSS_SELECTOR, "input#text")
        # time.sleep(1)
        # 3) Ввести в поиск Тензор (input_tensor_to_search_box)
        search_box.send_keys("тензор")
        search_box.click()
        # time.sleep(1)
        # 4) Проверить, что появилась таблица с подсказками (suggest) (does_suggest_appear)
        browser.find_element(By.CSS_SELECTOR, "div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile.mini-suggest__popup_visible")
        search_box.send_keys(Keys.ENTER)
        # 5) При нажатии Enter появляется таблица результатов поиска (does_results_appear_after_enter)
        # time.sleep(5)
        # 6) В первых 5 результатах есть ссылка на tensor.ru (is_tensor_in_top_5_results)
        search_results = browser.find_elements(By.XPATH, '//*[@id="search-result"]/li/div/div[1]/div[1]/a/b')
        search_results_text = [i.text for i in search_results]
        assert "tensor.ru" in search_results_text, f"expected true, got true"
        # time.sleep(5)
    
    # @pytest.mark.skip
    def test_yandex_pictures(self, browser):
        # 1) Зайти на yandex.ru
        link = "https://yandex.ru/"
        browser.get(link)
        # time.sleep(1)
        # 2) Ссылка «Картинки» присутствует на странице
        pictures_link = browser.find_element(By.XPATH, "//li[3]/a/div[1]")
        # 3) Кликаем на ссылку
        pictures_link.click()
        # time.sleep(1)
        new_window = browser.window_handles[1]
        # time.sleep(1)
        # 4) Проверить, что перешли на url https://yandex.ru/images/
        # time.sleep(1)
        browser.switch_to.window(new_window)
        print(browser.current_url)
        # time.sleep(1)
        # 5) Открыть 1 категорию, проверить что открылась, в поиске верный текст
        browser.find_element(By.CLASS_NAME, "PopularRequestList-Item_pos_0").click()
        # time.sleep(1)
        # 6) Открыть 1 картинку , проверить что открылась
        browser.find_element(By.CLASS_NAME, "serp-item_pos_0").click()
        # time.sleep(1)
        # 7) При нажатии кнопки вперед  картинка изменяется
        browser.find_element(By.CSS_SELECTOR, "div.CircleButton.CircleButton_type_next").click()
        # time.sleep(1)
        # 8) При нажатии кнопки назад картинка изменяется на изображение из шага 6. Необходимо проверить, что это то же изображение.
        browser.find_element(By.CSS_SELECTOR, "div.CircleButton_type_prev").click()
        # time.sleep(5)

        

'''
browser.get(link)
# time.sleep(1)

input = browser.find_element_by_css_selector("input#text")
input.send_keys("тензор")
input.click()
suggest = browser.find_element_by_css_selector("ul#suggest-list-miytf5kimf.mini-suggest__popup-content.")
input.send_keys(Keys.ENTER)
'''

# 1) Зайти на yandex.ru
# 2) Проверить наличия поля поиска (is_search_box_present)
# input = browser.find_element_by_css_selector("input#text")
# 3) Ввести в поиск Тензор (input_tensor_to_search_box)
# 4) Проверить, что появилась таблица с подсказками (suggest) (does_suggest_appear)
# 5) При нажатии Enter появляется таблица результатов поиска (does_results_appear_after_enter)
# 6) В первых 5 результатах есть ссылка на tensor.ru (is_tensor_in_top_5_results)

# 1) Зайти на yandex.ru
# 2) Ссылка «Картинки» присутствует на странице
# 3) Кликаем на ссылку
# 4) Проверить, что перешли на url https://yandex.ru/images/
# 5) Открыть 1 категорию, проверить что открылась, в поиске верный текст
# 6) Открыть 1 картинку , проверить что открылась
# 7) При нажатии кнопки вперед  картинка изменяется
# 8) При нажатии кнопки назад картинка изменяется на изображение из шага 6. Необходимо проверить, что это то же изображение.


# num1 = num1_tag.text
# num2_tag = browser.find_element_by_css_selector("#num2")
# num2 = num2_tag.text
# y = int(num1) + int(num2)

# select = Select(browser.find_element_by_tag_name("select"))
# # select.select_by_value("1")  # ищет элемент с текстом "Python"
# select.select_by_visible_text(str(y)) # ищет элемент по видимому тексту
# # select.select_by_index(0)  # ищет элемент по его индексу или порядковому номеру (ндексация начинается с нуля)

# # Отправляем заполненную форму
# button = browser.find_element_by_css_selector("button.btn")
# button.click()
time.sleep(5)


# закрываем браузер после всех манипуляций
# browser.quit()