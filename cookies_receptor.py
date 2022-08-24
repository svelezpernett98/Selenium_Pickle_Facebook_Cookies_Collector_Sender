from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, base64
import pandas as pd
import pickle


PATH = "C:/Users/santi/OneDrive/Documents/RPA/chromedriver.exe"
picture_options = Options()
picture_options.add_argument("--start-maximized")
init = webdriver.Chrome(PATH, chrome_options=picture_options)

init.get("https://es-la.facebook.com/login/device-based/regular/login/")
cookies = pickle.load(open("C:/Users/santi/OneDrive/Desktop/cookies_receptor/cookies9.pkl", "rb"))
for cookie in cookies:
    init.add_cookie(cookie)
    
init.refresh()