from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __int__(self, driver):
        self.driver = driver

    def move_to_menu_item(self, menu_item_text):
        menu_item = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, menu_item_text)))
        ActionChains(self.driver).move_to_element(menu_item).perform()

    def click_menu_item(self, menu_item_text):
        menu_item = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, menu_item_text)))
        menu_item.click()

    def enter_search_term(self, search_term):
        search_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "search-field")))
        search_box.clear()
        search_box.send_keys(search_term)

    def get_search_results(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='result-list']//h4")

