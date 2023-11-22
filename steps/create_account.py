import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from steps.browser import Browser
class sign_in_page(Browser):
    log_email = (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    password = (By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]')
    sign_in_button =(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div)")

    def log_in(self,log_email,password):
        button = WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div')))
        self.chrome.find_element(*self.log_email).send_keys(log_email)
        self.chrome.find_element(*self.password).send_keys(password)
        self.chrome.find_element(*self.sign_in_button).click()
        time.sleep(2)