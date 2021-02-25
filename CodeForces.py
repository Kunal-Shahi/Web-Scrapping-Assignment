import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
PATH="C:\\chromedriver.exe"
driver=webdriver.Chrome(PATH)
def main(number):

	for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		try:
			os.makedirs('./'+str(number)+'/'+i)
			
		except OSError:
			pass
		try:
			driver.get("https://codeforces.com/problemset/problem/"+str(number)+"/"+i)
			driver.implicitly_wait(10)
			if(driver.current_url[-1]!=i):
				os.rmdir('./'+str(number)+'/'+i)
				break
				
			driver.save_screenshot(str(number)+'/'+i+'/'+i+'.png')
			Input=driver.find_elements_by_class_name("input")
			Output=driver.find_elements_by_class_name("output")
			k=0
			for j in Input:
				k+=1
				fileI=open('./'+str(number)+'/'+i+'/input'+str(k)+'.txt','w')
				fileI.write(j.find_element_by_tag_name("pre").text)
				fileI.close()
			t=0   
			for j in Output:
				t+=1
				fileO=open('./'+str(number)+'/'+i+'/output'+str(t)+'.txt','w')
				fileO.write(j.find_element_by_tag_name("pre").text)
				fileO.close()
			

		except Exception:
			break
			pass
			
if __name__ == '__main__':
	main(sys.argv[1])
