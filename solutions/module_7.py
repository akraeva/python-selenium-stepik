from time import sleep
from selenium.webdriver.common.by import By
from main import get_driver


def m_7_1_1():
    with get_driver() as driver:
        driver.maximize_window()
        url = "https://parsinger.ru/selenium/7/7.1/index.html"
        driver.get(url)
        height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, {height});")
        sleep(2)
        res = driver.find_element(By.ID, "secret-container").text
    print(res.split()[-1])  # E7XX-QILL-PWJ1-SE0D


# m_7_1_1()
