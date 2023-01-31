from selenium.webdriver.common.by import By


class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[normalize-space()='Log in']"
    button_logout_Linktext="Logout"

    def __init__(self,driver):     #initializing driver
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(By.ID,"Email").clear()
        self.driver.find_element(By.ID,"Email").send_keys(username)

    def password(self,password):
        self.driver.find_element(By.ID,"Password").clear()
        self.driver.find_element(By.ID,"Password").send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,'Logout').click()





