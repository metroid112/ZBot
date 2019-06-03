from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import logging
import time


def find_chat(chat_title):
    x_arg = f'//span[contains(@title,"{chat_title}")]'
    print('Searching for chat title with XPATH:', x_arg)
    return wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))


def find_last_text(text_counter):
    text_xpath = f'//*[@id="main"]/div[3]/div/div/div[3]/div[{text_counter}]/div/div/div[1]/div/span/text()'

    return wait.until(EC.presence_of_element_located((By.XPATH, text_xpath)))


logging.basicConfig(filename='chat.log', level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
try:
    target_chat = input('Enter chat name:')
    chat = find_chat(target_chat)
    print('Found chat name: ', chat)
    chat.click()
    print('Inside chat')
    execution = input('Option: Log chat [L] | Type [T] ')
    # TODO: Ejecucion T
    if execution == 'T':
        inp_xpath = '//div[contains(@class,"copyable-text selectable-text")][@dir="ltr"][@data-tab="1"]'
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
        print('encontrado!, send', inp_xpath)
        # for i in range(100):
        #    input_box.send_keys(string + Keys.ENTER)
        #    time.sleep(1)
    if execution == 'L':
        logging.info('Starting a new log')
        last_id = 2
        while True:
            chat_texts = driver.find_elements_by_xpath(f'//span[contains(@class,"selectable-text invisible-space copyable-text")]')
            for text_element in chat_texts:
                text_id = int(text_element.id[text_element.id.index('-') + 1:])
                print('ID:', text_element.id[text_element.id.index('-') + 1:])
                print('Posicion ID:', text_element.id.index('-') + 1)
                print('ID Extraida:', text_id)
                if text_id > last_id:
                    last_id = text_id
                    print('Ultima ID:', last_id)
                    print('Grabo texto', text_element.text)
                    logging.warning(text_element.text)
            time.sleep(10)

except TimeoutException:
    print('Could not find chat name')
