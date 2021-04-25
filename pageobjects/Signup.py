
class Signup:
    button_click_signup_xpath="//body/div[3]/div[2]/div[1]/div[1]/div[3]/div[1]/a[1]/button[1]"
    textbox_firstname_id="first_name"
    textbox_middlename_id="middle_name"
    textbox_lastname_id="last_name"
    textbox_emailid_id="email_id"
    textbox_dob_id="dates2"
    textbox_mobileno="dates3"
    textbox_password_id="password"
    button_submit_id="submit"

    def __init__(self,driver):
        self.driver=driver

    def click_signup(self):
        self.driver.find_element_by_xpath(self.button_click_signup_xpath).click()

    def enter_first_name(self,firstname):
        self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(firstname)

    def enter_middle_name(self,middlename):
        self.driver.find_element_by_id(self.textbox_middlename_id).send_keys(middlename)

    def enter_lastname(self,lastname):
        self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(lastname)

    def enter_email_id(self,emailid):
        self.driver.find_element_by_id(self.textbox_emailid_id).send_keys(emailid)

    def enter_dob(self,dob):
        self.driver.find_element_by_id(self.textbox_dob_id).send_keys(dob)

    def enter_mobile_no(self,mobileno):
        self.driver.find_element_by_id(self.textbox_mobileno).send_keys(mobileno)

    def enter_pass_word(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def submit(self):
        self.driver.find_element_by_id(self.button_submit_id).click()