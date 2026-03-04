import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    wait = WebDriverWait(browser, 20, poll_frequency=0.1)
    price_locator = (By.ID, "price")
    wait.until(
        lambda d: EC.text_to_be_present_in_element(price_locator, "100")(d)
        and int("".join(ch for ch in d.find_element(*price_locator).text if ch.isdigit())) == 100
    )

    wait.until(EC.element_to_be_clickable((By.ID, "book"))).click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
finally:
    browser.quit()
