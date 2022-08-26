import time # Добавлен для удобства рецензентов - нужно раскомментировать.
from selenium.webdriver.common.by import By

# В тесте проверяется наличие кнопки добавления в корзину
# Селектор кнопки добавления в карзину является уникальным только для проверяемой страницы
def test_guest_should_see_button_add_in_basket_on_the_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)  #Команда добавлена для удобства рецензентов - нужно раскомментировать.
    found_button_add_in_basket = browser.find_elements(By.XPATH, '//*[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert found_button_add_in_basket, "button add in basket not found!"




