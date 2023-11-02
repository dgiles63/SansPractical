from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# pageObjects/MainMenu.py
class MainMenu:
    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get('https://www.sans.org/')

    def hoverTrainAndCertify(self):
        train_and_certify = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Train and Certify')))
        ActionChains(self.driver).move_to_element(train_and_certify).perform()
        courses = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Courses')))
        ActionChains(self.driver).move_to_element(courses).perform()
        full_course_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Full Course List')))
        full_course_list.click()

# pageObjects/AssertClassList.py
class ClassAssertions:
    def __init__(self, driver):
        self.driver = driver

    def assertionListOfClasses(self):
        assert "https://www.sans.org/cyber-security-courses/?msc=main-nav" == self.driver.current_url

# tests/navigation_test.py
def test_navigation():
    driver = webdriver.Chrome()
    main_menu = MainMenu(driver)
    class_assertions = ClassAssertions(driver)

    main_menu.visit()
    main_menu.hoverTrainAndCertify()
    class_assertions.assertionListOfClasses()

    driver.quit()