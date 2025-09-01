import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    d = webdriver.Chrome()        # Launch Chrome (needs Chrome + chromedriver)
    d.maximize_window()
    yield d
    d.quit()

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    # Enter username and password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Assert that we are on the inventory page
    assert "inventory" in driver.current_url
