import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class Espera(unittest.TestCase):
	def setUp(self):
		global driver
		driver = webdriver.Chrome()
		driver.implicitly_wait(15)
		driver.get("http://localhost:8081")
		
	#test1(self):
	
		#diomaEspanol = driver.find_element_by_xpath("button button-primary button-large")
		#f IdiomaEspañol is not None:
	#	IdiomaEspañol.click()
#		time.sleep(3)
		
		IdiomaEspanolbox = driver.find_element_by_class_name("button button-primary button-large")
		if IdiomaEspañolbox is not None:
			IdiomaEspañolbox.click()
			time.sleep(10)
    	
		SiteTitle = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/th/label")
		print("*******************************************************")
		print("MARCA: " +  SiteTitle.text)
		print("*******************************************************")
		print(" ")
		
		SiteTitlebox = driver.find_element_by_name('weblog_title')
		if SiteTitlebox is not None:
			SiteTitlebox.send_keys("Wordpress-ApiGolang")
			time.sleep(3)
			
		UserName = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/th/label")
		print("*******************************************************")
		print("MARCA: " +  UserName.text)
		print("*******************************************************")
		print(" ")
		
		UserNamebox = driver.find_element_by_name('user_name')
		if UserNamebox is not None:
			UserNamebox.send_keys("admin")
			time.sleep(3)

		Password = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/th/label")
		print("*******************************************************")
		print("MARCA: " +  Password.text)
		print("*******************************************************")
		print(" ")

		Passwordbox = driver.find_element_by_name('pass1-text')
		if Passwordbox is not None:
			Passwordbox.clear();
			Passwordbox.send_keys("admin")
			time.sleep(3)

		ConfirmPassword = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[5]/th")
		print("*******************************************************")
		print("MARCA: " +  ConfirmPassword.text)
		print("*******************************************************")
		print(" ")

		ConfirmPasswordbox = driver.find_element_by_name('pw_weak')
		if ConfirmPasswordbox.is_selected() is not None: 
			ConfirmPasswordbox.click() 
			time.sleep(3)

		YourEmail = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[6]/th/label")
		print("*******************************************************")
		print("MARCA: " +  YourEmail.text)
		print("*******************************************************")
		print(" ")

		YourEmailbox = driver.find_element_by_name('admin_email')
		if YourEmailbox is not None: 
			YourEmailbox.send_keys("angulo.franklin@gmail.com")
			time.sleep(3)

		Submitbox = driver.find_element_by_name('Submit')
		if Submitbox is not None: 
			Submitbox.click()
			time.sleep(10)

	def test1(self):
		print("*******************************************************")
		print("Estado de la Instalación: Completada")
		print("*******************************************************")
		print(" ")

	def tearDown(self):
		driver.quit()

if __name__ == "__main__":
	unittest.main()
