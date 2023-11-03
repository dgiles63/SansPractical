import pytest
from selenium import webdriver
from filter_page import FilterPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_search(driver):
    driver.get("https://www.sans.org/cyber-security-courses/?per-page=10")

    filter_page = FilterPage(driver)

    filter_page.check_focus_checkbox("Cloud Security")
    filter_page.check_skill_checkbox("Essentials")
    results = filter_page.get_search_results()
    assert any("SEC488" in result.text for result in results)


"""
/*  Testing Methodologies
 There are many ways to devise a test plan that would test the matrices of checkbox filters
 to generate results that would give a team confidence in the functionality of the system.
 Those could include:
 1. Random Sampling. Choose 5 to 8 randomly selected combinations, choosing judiciously to cover as many
    individual checkmarks as possible.
 2. Pareto Chart (marketing driven). Agile development has a market driver. Use data to determine
    the most popular purchases and put the emphasis on selections that contain those elements.
 3. Domain Knowledge Testing. Get advice from those who have the most experience with the app as to which
    elements are the most strategic.
 4. The other methodologies include: Endpoint testing (firsts and lasts, gaps and null, etc.), Regression
    based (using past failures to determine what needs the most attention), Latest and Greatest (emphasis
    on the latest additions to the code), Risk-Based (which selections might be the riskiest?), Usability
    Based (What are the most likely selections that users will make based on ease of use)

 What determines the best methodology is whatever the team selects. But let that selection be based on 
 some criteria or objective so that the testing has a purpose and measurable results and can be revised
 to better meet the purpose or objective.

*/
"""