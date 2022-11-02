from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, "input_value").text)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)
  
    res = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", res)

    res.send_keys(y)

    CH = browser.find_element(By.ID, "robotCheckbox")
    CH.click()

    RB = browser.find_element(By.ID, "robotsRule")
    RB.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type = 'Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()