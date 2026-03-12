from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


def m_7_2_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/7/7.2/index.html"
        driver.get(url)
        element = driver.find_element(By.CLASS_NAME, "input-wrapper").find_element(
            By.TAG_NAME, "input"
        )
        for i in range(100):
            element.send_keys(i)
            element.send_keys(Keys.ENTER)
            element.send_keys(Keys.ARROW_DOWN)
            element = driver.switch_to.active_element
        res = driver.find_element(By.ID, "hidden-password").text
    print(res.split()[-1])  # Wasteland-Survivor-2077


# m_7_1_1()
# m_7_2_1()
