from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from job_listing_extractor.browser_config import create_driver
def perform_automation():
 driver=create_driver()
 driver.get("https://www.rozee.pk/")
 time.sleep(2)
 wait = WebDriverWait(driver, 10)
 search_input = driver.find_element(By.ID, "search")
 search_input.send_keys("Python Developer")  
 time.sleep(2)
 city_dropdown = driver.find_element(By.XPATH, "//button[@data-id='homeSearchCity']")
 driver.execute_script("arguments[0].click();", city_dropdown)
 time.sleep(2)
 try:
   target_city="Karachi" 
   input_city = driver.find_element(By.XPATH, "//*[@id='search_form']/div[2]/div/div/div/input")
   input_city.send_keys(target_city)    
   time.sleep(2)
 except Exception as e:
    print(f"city not found: {e}")
 time.sleep(2)
 salary_dropdown = driver.find_element(By.XPATH, "//*[@id='search_form']/div[3]/div/button")
 driver.execute_script("arguments[0].click();", salary_dropdown)
 time.sleep(2)
 try:
     options = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="search_form"]/div[3]/div/div/ul/li'))
    )
     time.sleep(2)
     desired_salary = '8,000'
     found = False
     for option in options:
        if option.text.strip() == desired_salary:
            driver.execute_script("arguments[0].scrollIntoView(true);", option)
            time.sleep(2)
            driver.execute_script("arguments[0].click();", option)
            found = True
            break
 except Exception as e:
    print(f"salary not found: {e}")
 select_button = driver.find_element(By.XPATH, "//*[@id='search_form']/div[4]/button")
 driver.execute_script("arguments[0].click();", select_button)
 time.sleep(2)
 return driver
#---------------------------------------yhn tk perfect hai-----------------------------------
