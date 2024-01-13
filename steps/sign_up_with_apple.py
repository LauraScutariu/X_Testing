import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTwitterSignUpWithApple(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
        self.driver.get("https://twitter.com")

    def tearDown(self):
        self.driver.quit()

    def test_sign_up_with_apple(self):
        apple_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "//div[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-17w48nw r-1mf7evn r-a9p05 r-eu3ka r-1ipicw7 r-p1pxzi r-2yi16 r-1qi8awa r-ymttw5 r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']"))
        )
        apple_button.click()

        apple_id_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "//input[@id='ac-localnav-menustate']"))
        )
        apple_id_input.send_keys("your_apple_id")

        password_input = self.driver.find_element_by_css_selector("//input[@type='password']")
        password_input.send_keys("your_apple_password")

        sign_in_button = self.driver.find_element_by_css_selector("//button[@id='sign-in']")
        sign_in_button.click()

        # Verificare către pagina Twitter după autentificarea cu Apple
        self.assertTrue("Twitter" in self.driver.title)

if __name__ == "__main__":
    unittest.main()
