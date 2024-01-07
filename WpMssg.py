# import libraries
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
#  that helps in managing and controlling the ChromeDriver service. 
# By importing Service, you gain access to methods and options that allow you to start, stop, and configure the ChromeDriver service.
# This enables you to customize and manage the interaction between your automation script and the Chrome browser.
from selenium.webdriver.support.ui import WebDriverWait
#  that helps you pause the execution of your code until a certain condition is met
#  This can be useful when you want to wait for elements to appear on a web page, for certain actions to complete,
# or for any other condition to be satisfied before proceeding with further steps in your script.
from selenium.webdriver.support import expected_conditions as EC
# यह कोड लाइन एक तैयार उपयोग करने योग्य स्थितियों का सेट लाती है जिसका उपयोग आप वेब ऑटोमेशन कार्यों के दौरान विशेष घटनाओं या 
# स्थितियों की प्रतीक्षा करने के लिए कर सकते हैं।
# इन स्थितियों को आमतौर पर WebDriverWait क्लास के साथ उपयोग किया जाता है 
from selenium.webdriver.common.keys import Keys
# this line of code brings in a set of ready-to-use keyboard keys and key combinations that you can use to simulate user interactions with the 
# keyboard during your automation scripts. 
# It provides a convenient way to send special keys like Enter, Tab, Arrow keys, Function keys, and modifiers like Shift, Control, and Alt.
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(executable_path=r"C:\Users\Admin\OneDrive\Desktop\Regular\Selenium\chromedriver.exe"))

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)
# WebDriverWait(driver, 600) creates a WebDriverWait object that will wait for a maximum of 600 seconds (10 minutes)
# for a condition to be satisfied
time.sleep(10)

target = '"Debo"'
string = "Python Automation"*5
x_arg = '//span[contains(@title,' + target + ')]'


group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
# Ye wait krega jb tk x-arg mil nhi jata baad me uspe click krega

time.sleep(5)


inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[1]/div[1]/p'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
# input_box.click()
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(20)
# the loop repeats a sequence of actions 100 times.
# It enters the value of the string variable into an input box, simulates pressing the Enter key, 
# and then pauses execution for 20 seconds before repeating the process for the next iteration


