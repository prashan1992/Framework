import pytest
from selenium import webdriver
from pageobjects.Signup import Signup

class Test_001_Signup:
    def test_homepage(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/91782/Desktop/Prashant/Driver/chromedriver.exe")
        self.driver.get("https://maatribhasha.com/")
        print("prashant")