from selenium.webdriver.common.by import By
import time


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/reviews/add/#addreview"


def test_guest_should_see_basket(browser):
    browser.get(link)
    time.sleep(30)
    basket = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert basket is not None, "No button add to basket"
