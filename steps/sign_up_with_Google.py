import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTwitterSignUpWithGoogle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
        self.driver.get("https://twitter.com")

    def tearDown(self):
        self.driver.quit()

    def test_sign_up_with_google(self):
        google_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '//span[@class="nsm7Bb-HzV7m-LgbsSe-BPrWId"]'))
        )
        google_button.click()

        google_email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "//input[@type='email']"))
        )
        google_email_input.send_keys("your_google_email")

        next_button = self.driver.find_element_by_css_selector("button[type='button'][jsname='V67aGc']")
        next_button.click()

        google_password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "//input[@type='password']"))
        )
        google_password_input.send_keys("your_google_password")

        next_button = self.driver.find_element_by_css_selector("button[type='button'][jsname='YPqjbf']")
        next_button.click()

        # Verificare către pagina Twitter după autentificarea cu Google
        self.assertTrue("Twitter" in self.driver.title)

if __name__ == "__main__":
    unittest.main()
