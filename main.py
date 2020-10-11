from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
log = input("login: ")
pas = input("password: ")
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys(log)
driver.find_element_by_id("pass").send_keys(pas)
driver.find_element_by_css_selector("button[data-cookiebanner='accept_button']").click()
driver.find_element_by_css_selector("button[type='submit']").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "mount_0_0")))
driver.get("https://www.facebook.com/friends")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "mount_0_0")))
ilosc_dodanych=0
while True:
        try:
            driver.find_element_by_css_selector("div[aria-label='Dodaj']").click()
            ilosc_dodanych+=1
            print(f"ilość dodanych osob:{ilosc_dodanych}")
            start = time.time()
            time.sleep(2)
        except:
            driver.find_element_by_css_selector("div[aria-label='Anuluj zaproszenie']").send_keys(Keys.PAGE_DOWN)
            koniec = time.time()
            if koniec-start>10:
                driver.get("https://www.facebook.com/friends")
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "mount_0_0")))
        
