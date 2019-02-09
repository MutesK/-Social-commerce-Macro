from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class DriverAwaiter(object):
	def __init__ (self, driver_Src, debug_option) :
		if debug_option == True :
			self.driver = webdriver.Chrome(driver_Src)
		else :
			chrome_option = Options()
			chrome_option.add_argument("--headless")
			chrome_option.add_argument("--window-size=%s" % "800,600")
			chrome_option.binary_location = driver_Src

			self.driver = webdriver.Chrome(executable_path=driver_Src,
								  chrome_options=chrome_option)

	def get_driver(self) :
		return self.driver

	def get(self, httpsrc) :
		return self.driver.get(httpsrc)

	def await_pageload_by_xpath(self, xpath) :
		wait = WebDriverWait(self.driver, 8)
		wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
		return True;

	def await_pageload_by_id(self, id) :
		wait = WebDriverWait(self.driver, 8)
		wait.until(EC.presence_of_element_located((By.ID, id)))

	def await_pageload_by_class(self, class_) :
		wait = WebDriverWait(self.driver, 8)
		wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_)))
		
	def await_find_element_by(self, id) :
		self.await_pageload_by_id(id)
		return self.driver.find_element_by_id(id)

	def await_find_element_by_class_name(self, class_) :
		self.await_pageload_by_class(class_)
		return self.driver.find_element_by_class_name(class_)

	def await_find_element_by_xpath(self, xpath) :
		self.await_pageload_by_xpath(xpath)
		return self.driver.find_element_by_xpath(xpath)
		
	def find_element_by_id(self, id) :
		return self.driver.find_element_by_id(id)

	def find_element_by_class_name(self, class_) :
		return self.driver.find_element_by_class_name(class_)

	def find_element_by_xpath(self, xpath) :
		return self.driver.find_element_by_xpath(xpath)

	def clickable_wait_by_xpath(self, xpath) :
		wait = WebDriverWait(self.driver, 8)
		wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
		return self.find_element_by_xpath(xpath)

