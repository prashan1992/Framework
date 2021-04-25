from selenium import webdriver
import pytest
@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome(executable_path="C:/Users/91782/Desktop/Prashant/Driver/chromedriver.exe")
    driver.get("https://maatribhasha.com/")