from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterPage:
    def __init__(self, driver):
        self.driver = driver

    # The course catalogue can be reduced by four separate filter categories. This is separated into
    # the four groups of filters, namely Focus Areas, Skill Levels, Status, and Training Formats.
    # Focus Areas
    def check_focus_checkbox(self, focus_item_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, f"//label[contains(@class, 'checkbox') and contains(text(), '{focus_item_text}')]")))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def check_skill_checkbox(self, skill_item_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, f"//label[contains(@class, 'checkbox') and contains(text(), '{skill_item_text}')]")))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def check_status_checkbox(self, status_item_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, f"//label[contains(@class, 'checkbox') and contains(text(), '{status_item_text}')]")))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def check_training_checkbox(self, training_item_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, f"//label[contains(@class, 'checkbox') and contains(text(), '{training_item_text}')]")))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def get_search_results(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='result-list']//h4")