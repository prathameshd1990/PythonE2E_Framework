from selenium.webdriver.common.by import By


class Checkoutpage:
    # self.driver.find_element_by_css_selector("a[class*='btn-primary']")
    def __init__(self, driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, ".card-title a")
    product_footer = (By.CSS_SELECTOR, ".card-footer button")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def productsList(self):
        return self.driver.find_elements(*Checkoutpage.products)

    def addProduct(self):
        return self.driver.find_elements(*Checkoutpage.product_footer)

    def checkoutButton(self):
        return self.driver.find_element(*Checkoutpage.checkout_button)