from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# Replace below path with the absolute path
# to chromedriver in your computer
class WhatsappMessage:
	"""
	class for sending message via Whatsappweb
	"""
	def __init__(self, friends_lists, message):
		self.friends_lists = friends_lists
		self.message = message

	def send_message(self):
		"""
		Method to send messages
		"""
		# friends_lists = ['Save']

		# driver = webdriver.Chrome('../chromedriver')
		driver = webdriver.Chrome(executable_path='C:\whatsapp-automate\src\chromedriver.exe')

		url = driver.command_executor._url
		session_id = driver.session_id


		try:
			with open("url_session_id.txt", "r") as f:
				url, session_id = f.read().split()
				driver = webdriver.Remote(command_executor=url,desired_capabilities={})
				driver.session_id = session_id

		except FileNotFoundError:
			with open("url_session_id.txt", "w") as f:
				f.write(f"{url}\n{session_id}")

		driver.get("https://web.whatsapp.com/")
		wait = WebDriverWait(driver, 600)

		group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.RLfQR")))
		search = driver.find_elements_by_xpath('//*[@id="side"]/div/div/label/input')[0]
		print (search)
		for friend in self.friends_lists:
			search.clear()
			search.send_keys(friend)
			wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button._3Burg")))
			time.sleep(3)
			persons = driver.find_elements_by_class_name('_2wP_Y')
			print(len(persons))
			for person in persons:
				try:
					person_title = person.find_element_by_class_name('_1wjpf')
					print(person_title.get_attribute("title"))
					if person_title.get_attribute("title") == friend:
						person_contact = person.find_element_by_class_name('_2EXPL')
						person_contact.click()
						message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
						message.send_keys("Automated Hello message")

						sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
						sendbutton.click()
						break
				except:
					print("*")
					continue

		driver.close()


obj_whatsapp = WhatsappMessage(["Save"], "Thanks")
obj_whatsapp.send_message()
