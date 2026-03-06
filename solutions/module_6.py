from time import sleep
from selenium.webdriver.common.by import By
from main import get_driver


def m_6_1_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.2/index.html"
        driver.get(url)
        elem = driver.find_element(By.TAG_NAME, "a")
        elem.click()
        elem = driver.find_element(By.TAG_NAME, "a")
        elem.click()
        driver.back()
        driver.back()
        button = driver.find_element(By.ID, "getPasswordBtn")
        button.click()
        alert = driver.switch_to.alert
        res = alert.text
    print(res.split(":")[-1].strip())  # B@ck 1n Bl@ck


def m_6_1_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.2.1/index.html"
        driver.get(url)
        elem = driver.find_element(By.ID, "this_pic")
        elem.screenshot("res_6_1_2.png")  # 2323


# m_6_1_1()
# m_6_1_2()
