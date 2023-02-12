from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import numpy as np
import random
import cv2
import pyautogui
import re
import requests

class Bot:
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        #with statement
        with webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options) as driver:
            #wait statement
            wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
            driver.get("https://1000randomnames.com/")
            driver.maximize_window()
            self.name_elems = driver.find_elements(By.TAG_NAME, 'li') #list of all the web elements. The name is inside the text prop i.e: name = self.name_elems[0].text
            try: 
                with open('randomNames.txt','x') as names_file:
                    for name_elem in self.name_elems:
                        names_file.write(f'{name_elem.text} \n')
            except:
                pass

    def Tiktok(self)-> None:
        #initialize options
        options = webdriver.ChromeOptions()
        #with statement
        with webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options) as driver:
            #wait statement
            wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
            driver.get("https://www.tiktok.com/signup/phone-or-email/phone")
            driver.maximize_window()
            sign_email = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Sign up with email")))
            sign_email.click()
            month_selec_elem = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[1]')
            month_selec_elem.click()
            month_list_elem = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[1]/div[2]')
            months_elems = month_list_elem.find_elements(By.CLASS_NAME, 'tiktok-x376y3-DivOption')
            month_elem = random.choice(months_elems)
            time.sleep(random.randint(0,15))
            month_elem.click()

            day_selec_elem = driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[2]/div[2]/div[1]')
            time.sleep(random.randint(0,15))
            day_selec_elem.click()
            day_list_elem = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[2]/div[2]')
            days_elems = day_list_elem.find_elements(By.CLASS_NAME, 'tiktok-x376y3-DivOption')
            day_elem = random.choice(days_elems)
            time.sleep(random.randint(0,15))
            day_elem.click()

            year_selec_elem = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[3]/div[1]')
            time.sleep(random.randint(0,15))
            year_selec_elem.click()
            year_list_elem = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[3]/div[2]')
            years_elems = year_list_elem.find_elements(By.CLASS_NAME, 'tiktok-x376y3-DivOption')
            year_elem = random.choice(years_elems)
            time.sleep(random.randint(0,15))
            year_elem.click()
            
            time.sleep(30)
            
    def generate_gmail(ID: str):
        #accessing the API
        #url = 
        pass
if __name__ == "__main__":
    bot = Bot()
    bot.Tiktok()