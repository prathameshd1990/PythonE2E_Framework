from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import Checkoutpage
from pageObjects.HomePage import Homepage
from utilities.Baseclass import Baseclass


class TestOne(Baseclass):
    def test_e2e(self):
        log = self.getLogger()
        home = Homepage(self.driver)
        home.shopItems().click()
        checkout = Checkoutpage(self.driver)
        log.info("Getting all products")
        products = checkout.productsList()

        i = -1
        for product in products:
            i = i + 1
            product_text = product.text
            log.info(product_text)
            if product_text == "Samsung Note 8":
                checkout.addProduct()[i].click()

        checkout.checkoutButton().click()

        self.driver.find_element_by_css_selector("button[class*='btn-success']").click()

        self.driver.find_element_by_id("country").send_keys("ind")
        log.info("Country: India")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        alert_text = self.driver.find_element_by_css_selector("div[class*='alert-success']").text
        log.info("Alert" + alert_text)
        assert "Success!" in alert_text

