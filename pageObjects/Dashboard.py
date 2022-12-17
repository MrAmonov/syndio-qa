from selenium.webdriver.common.by import By


# This file is to store all the elements within the web UI and use it simply within the test cases

class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    # These variables hold elements from the UI
    gender = (By.XPATH, "//button[.='Gender']")
    race = (By.XPATH, "//button[.='Race']")
    dropdown = (By.XPATH, "//button[@id='dropdown-button']")
    dropdown_change = (By.XPATH, "//li[@class='labelOption']")
    function = (By.XPATH, "//li[.='Group by Function']")
    role = (By.XPATH, "//li[.='Group by Role']")
    pay_equity_gap = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[1]/p/strong[1]")
    employees = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/p/strong")
    budget = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/p/strong")

    # These methods use variables and extract the elements and return the elements when the method is called
    def get_gender(self):
        return self.driver.find_element(*Dashboard.gender)

    def get_race(self):
        return self.driver.find_element(*Dashboard.race)

    def get_dropdown(self):
        return self.driver.find_element(*Dashboard.dropdown)

    def get_dropdown_change(self):
        return self.driver.find_element(*Dashboard.dropdown_change)

    def get_function(self):
        return self.driver.find_element(*Dashboard.function)

    def get_role(self):
        return self.driver.find_element(*Dashboard.role)

    def get_pay_equity_gap(self):
        return self.driver.find_element(*Dashboard.pay_equity_gap)

    def get_employees(self):
        return self.driver.find_element(*Dashboard.employees)

    def get_budget(self):
        return self.driver.find_element(*Dashboard.budget)
