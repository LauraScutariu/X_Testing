from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Webdriver:
	driver = webdriver.Chrome(
		service=Service(ChromeDriverManager().install())
	)
	driver.maximize_window()
	driver.implicitly_wait(10)

	def quit_driver(self):
		self.driver.quit()