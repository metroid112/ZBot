from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

target = '"Ricos, Mocosos y Currrvos"'
string = "Esto es un bot aprovado por Bantotal, entreguenme su salario"

x_arg = '//span[contains(@title,' + target + ')]'
print('buscando titulo')
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
print('encontrado, click', group_title)
group_title.click()
print('clickeado, buscando input')
inp_xpath = '//div[contains(@class,\'copyable-text selectable-text\')][@dir="ltr"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
print('encontrado!, send', inp_xpath)
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
