import pytest
from selenium import webdriver
from main_page import MainPage
from menu_items import MenuItems


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_navigation(driver):
    driver.get("https://www.sans.org")
    full_course_url = "https://www.sans.org/cyber-security-courses/?msc=main-nav"

    main_page = MainPage(driver)
    menu_items = MenuItems()

    main_page.move_to_menu_item(menu_items.menu_item_train_and_certify)
    main_page.move_to_menu_item(menu_items.menu_item_courses)
    main_page.click_menu_item(menu_items.menu_item_full_course_list)
    assert full_course_url == driver.current_url
