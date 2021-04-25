from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:/Users/91782/Desktop/Prashant/Driver/chromedriver.exe")
    driver.get("https://maatribhasha.com/")
    request.cls.driver = driver
    yield
    driver.quit()
