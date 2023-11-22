from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Browser():
    chrome = webdriver.Chrome(executable_path = ChromeDriverManager().install())
    chrome.maximize_window()
    chrome.get('https://twitter.com/')
    chrome.implicitly_wait(4)

    def close(self):
        self.chrome.close()