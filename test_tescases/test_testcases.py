import pytest
from selenium import webdriver
from pageobjects.Signup import Signup
from utilities.BaseClass import BaseClass


class Test_001_Signup(BaseClass):

    def test_homepage(self):
        signup = Signup(self.driver)
        signup.click_signup()
        signup.enter_first_name("Prashant")
        signup.enter_middle_name("Kumar")
        signup.enter_lastname("Dwivedi")
        signup.enter_email_id("prashantkr.dwivedi@gmail.com")
        signup.enter_dob("07-09-1992")
        signup.enter_mobile_no("9451683489")
        signup.enter_pass_word("rudra@1234")
        signup.submit()
    
