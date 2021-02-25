u=input("Enter Your username ")
p=input("Enter Your login password ")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH="C:\\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/")
username=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")
username.clear()
username.send_keys(u)
password.clear()
password.send_keys(p)
Login=driver.find_element_by_id("login")
Text=(Login.text).split("\n")
text=Text[3].split(' ')
g=''
if "first" in text:
	g=text[-4].strip()
elif "second" in text:
	g=text[-2]
elif "add" in text:
	g=str(int(text[-4].strip()) + int(text[-2]))
elif "subtract" in text:
	g=str(int(text[-4].strip()) - int(text[-2]))
Captcha=driver.find_element_by_id("valuepkg3")	
Captcha.clear()
Captcha.send_keys(g)
Captcha.send_keys(Keys.RETURN)
