import os
import time

import speech_recognition as sr
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv()


chrome_driver_path = "C:\development\chromedriver.exe"
chr_options = webdriver.ChromeOptions()
chr_options.add_experimental_option("detach", True)


r = sr.Recognizer()
mic = sr.Microphone()


def listen():
    with mic as source:
        audio = r.listen(source)
        try:
            data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("try again")
            listen()
        else:
            return data


phrase = listen()
print(phrase)

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chr_options)
driver.get("https://www.youtube.com/watch?v=DqUd72pK15Y")

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Omah Lay godly")
search_box.send_keys(Keys.ENTER)
