import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import CodeForces
PATH="C:\\chromedriver.exe"
driver=webdriver.Chrome(PATH)
#CodeForces.Scrap(1486)
driver.get("https://codeforces.com/contests")
cl=driver.find_element_by_class_name("contests-table")
l=cl.find_elements_by_tag_name("tr")
for i in range(1,int(sys.argv[1])+1):
	k=l[i].get_attribute("data-contestid")
	CodeForces.Scrap(int(k))

	
