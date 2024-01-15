import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.chrome(ChromeDriverManager().install())

from steps.browser import Browser
class create_account(Browser):
    log_name = (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/label/div/div[2]')
    log_email = (By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/label/div/div[2]')
    log_date_of_birth = (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[3]/div/div[1]')
    next_button =(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div")

    def test_log_in(self, log_name, password, log_email, log_date_of_birth, next_button):
        button = WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')))
        self.chrome.find_element(*self.log_name).send_keys(log_name)
        self.chrome.find_element(*self.log_email).send_keys(log_email)
        self.chrome.find_element(*self.log_date_of_birth).send_keys(log_date_of_birth)
        self.chrome.find_element(*self.next_button).click()
        time.sleep(5)