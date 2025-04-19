from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд цену
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button_book = browser.find_element(By.ID, "book")
button_book.click()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
x = x_element.text
y = calc(x)
 
input1 = browser.find_element(By.ID, "answer") 
input1.send_keys(y)

time.sleep(2)        
# Отправляем заполненную форму
button_submit = browser.find_element(By.ID, "solve")
button_submit.click()
time.sleep(3) 
