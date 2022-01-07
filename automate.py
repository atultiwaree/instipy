from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://instagram.com/')

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']") #target input userid
password_input = browser.find_element_by_css_selector("input[name='password']") #target iput type password
username_input.send_keys("atul.tiwariii")  #yaha par apni insta id dalo
password_input.send_keys("########") #yaha par apna password of insta dalo

btn = browser.find_element_by_xpath("//button[@type='submit']")  #for clicking loggin button
btn.click()

sleep(10)

users = ["subham_yadav834", "ashish.kesharwanii", "pradeep"]

for i in range(0, 3):
   prf = browser.find_element_by_xpath("//div[2]/input")
   sleep(1)
   prf.send_keys(users[i])
   sleep(3)
   cl_t_prf = browser.find_element_by_xpath("//div[2]/div/div/a/div")
   cl_t_prf.click()
   sleep(3)
   cl_t_msg = browser.find_element_by_xpath("//button[contains(.,'Message')]")
   cl_t_msg.click()
   sleep(3)

   
   try:
   	  not_now = browser.find_element_by_xpath("//button[contains(.,'Not Now')]")
   	  not_now.click()
   	  cl_t_s_msg = browser.find_element_by_xpath("//textarea")
   	  cl_t_s_msg.click()
   	  cl_t_s_msg.send_keys("Bye Bye! "+users[i])
   	  sleep(1)
   	  send_msg = browser.find_element_by_xpath("//button[contains(.,'Send')]")
   	  send_msg.click()
   except NoSuchElementException as exception:
   	  cl_t_s_msg = browser.find_element_by_xpath("//textarea")
   	  cl_t_s_msg.click()
   	  cl_t_s_msg.send_keys("Hello! "+users[i])
   	  sleep(1)
   	  send_msg = browser.find_element_by_xpath("//button[contains(.,'Send')]")
   	  send_msg.click()
   	  print("no such yyyyyyyyyyyyyyyyyyyy")
   else:
   	print("No Exception Found")
   finally:
   	print("All Set!!")
    	
    

   
   



    





# prf = browser.find_element_by_xpath("//div[6]/span/img") #for clickng right  corner image of your profile
# prf.click()

# sleep(3)

# vew = browser.find_element_by_xpath("//div[2]/div[2]/a/div") #to click view profile
# vew.click()

# sleep(8)

# prf = browser.find_element_by_xpath("//span/img")  #to click on profile image for logging out
# prf.click()

# sleep(3)

# lgt = browser.find_element_by_xpath("//div[2]/div[2]/div[2]/div[2]/div") #click to logout
# lgt.click()

# sleep(5)
# browser.close()  #ye browser driver close kar dega
