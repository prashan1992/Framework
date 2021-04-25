import pytest
from selenium import webdriver
from pageobjects.Signup import signup


class Test_001_Signup:
    def test_homepage(self):
        self.signup.click_signup()
        self.signup.enter_first_name("Prashant")
        self.signup.enter_middle_name("Kumar")
        self.signup.enter_lastname("Dwivedi")
        self.signup.enter_email_id("prashantkr.dwivedi@gmail.com")
        self.signup.enter_dob("07-09-1992")
        self.signup.enter_mobile_no("9451683489")
        self.signup.enter_pass_word("rudra@1234")
        self.signup.submit()
