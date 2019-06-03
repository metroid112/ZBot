import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


def find_chat(chat_title):
    x_arg = f'//span[contains(@title,"{chat_title}")]'
    print('Searching for chat title with XPATH:', x_arg)
    return wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

try:
    target_chat = input('Enter chat name:')
    chat = find_chat(target_chat)
    print('Found chat name:', chat)
    chat.click()
    print('Inside chat')
    inp_xpath = '//div[contains(@class,"copyable-text selectable-text")][@dir="ltr"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    print('encontrado!, send', inp_xpath)
    # for i in range(100):
    #    input_box.send_keys(string + Keys.ENTER)
    #    time.sleep(1)
except TimeoutException:
    print('Could not find chat name')

