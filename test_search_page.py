import pytest
from selenium import webdriver
from search_page import SearchPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_search(driver):
    driver.get("https://www.sans.org/cyper-secureity-courses")

    search_page = SearchPage()

    search_page.enter_search_term("SEC504")
    results = search_page.get_search_results()
    assert any("SEC504" in result.text for result in results)


"""  
Search Feature Tests
The following are standard input field tests:
1. Error testing. There are a number of error test that should be performed. Injecting escape sequences, SQL code, Javascript code, html code,
   special characters (*,",'), wildcard characters, and APIs or portions of APIs are among the things that often break input fields.
2. Null, empty, empty+backspace. Test for ways to enter nothing or less.
3. Too Long, buffer over-run. Endpoints of how many characters can go on the input field. Testing the max, then the max + 1. Test with
   many more characters than the maximum.
4. Unicode or Localization tests.
5. Performamce testing.

A test plan for implementing the tests above that are vetted and prioritized by the team should include:
  1. An overview and objectives of what the test will accomplish.
  2. Team roles and responsibilites with respect to the test to be implimented.
  3. Testing strategy and methodologies.
  4. The test environment and test data.
  5. An estimated schedule.
  6. Test cases and scenarios.
  7. Expected tools and frameworks.
  8. How to manage defects.
  9. How to manage progress and tracking.
  10. Important metrics and milestones.
  11. Expected risks and how to mitigate those.
  12. Continuous Improvement.
  13. Approvals.
  
  """