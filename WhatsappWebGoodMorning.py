#Import necessary modules
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import random

#Open Chrome
driver = webdriver.Chrome()

#Load up Web Whatsapp
driver.get("https://web.whatsapp.com/")

#Provide time to scan whatsapp QR code
wait = WebDriverWait(driver, 600)

good_morning_messages=["What's up? :D","Good Morning! :)","Rise and Shine. :3","I'm up!"]

done=0
wish_morning=0

#Keep the bot running
while True:
    
    #Identify time
    cur_time=datetime.datetime.now() 
    time=cur_time.time()
    cur_hour=time.hour
    cur_min=time.minute
    
    #Wish "Good Morning" at 06:00 am
    if wish_morning==0 and cur_hour==6 and cur_min==0:

        #Specify contacts to send message to
        Target = ["Mom","Dad"]

        #Iterate over selected contacts
        for target in Target:

                #Select random greeting
        	string = good_morning_messages[random.randrange(0,100)%4]

        	#Identify correct text input panel (search bar)
        	x_arg = '//span[contains(@title,' + target + ')]'
        	group_title = wait.until(EC.presence_of_element_located((
                    By.XPATH, x_arg)))
        	group_title.click()

        	#Identify correct text input panel (chat box)
        	inp_xpath = '//div[@class="input"][@data-tab="1"][@dir="auto"]'
        	input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath)))

        	#Send message, and set flag to indicate done for day
        	input_box.send_keys("Hi " + target + ", " + string + Keys.ENTER)
        	wish_morning=1

    #Reset flag
    if cur_hour!=6 or cur_min!=0:
        wishmorning=0
