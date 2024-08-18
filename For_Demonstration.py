from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup,Doctype
import requests
import csv
import pprint

#Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to a webpage
searching="Hillary Clinton" #-->User input 
driver.get("https://www.wikipedia.org/")
time.sleep(2)
input_element =driver.find_element(By.ID,"searchInput") #acess the search bar 
input_element.send_keys(searching+Keys.ENTER) #type into the text area 
# Parse the HTML content
page_source=driver.page_source
time.sleep(3)
soup = BeautifulSoup(page_source,'html.parser') #or use lxml
brief =soup.find_all('p')[1].get_text()
print(brief) #--> breif about the searched person 
driver.quit()
