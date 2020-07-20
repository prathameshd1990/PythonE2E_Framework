from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    icecream_check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR, "input[class*='btn-success']")
    alert = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def shopItems(self):
        return self.driver.find_element(*Homepage.shop)

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getPassword(self):
        return self.driver.find_element(*Homepage.password)

    def checkIcecream(self):
        return self.driver.find_element(*Homepage.icecream_check)

    def genderSelection(self):
        return self.driver.find_element(*Homepage.gender)

    def submitButton(self):
        return self.driver.find_element(*Homepage.submit)

    def getAlert(self):
        return self.driver.find_element(*Homepage.alert)