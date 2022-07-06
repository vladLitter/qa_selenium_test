from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    basket = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert basket, "No button add to basket"
