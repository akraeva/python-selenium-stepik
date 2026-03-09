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


def m_6_3_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.3.1/index.html"
        driver.get(url)
        token = driver.get_cookie("token_22")
        res = token["value"]
    print(res)  # V78lmnOPQ123rstUVW456xyzABC


def m_6_3_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.3/index.html"
        driver.get(url)
        data = driver.get_cookies()
        song = next(d["name"] for d in data if "name" in d.keys())
        driver.find_element(By.ID, "phraseInput").send_keys(song)
        driver.find_element(By.ID, "checkButton").click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # Th3r3-1s-N0-W0rd-M1ss-1n-Pudg35-D1ct10n@ry


def m_6_3_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.3.2/index.html"
        driver.get(url)
        driver.delete_all_cookies()
        sleep(3)
        res = driver.find_element(By.ID, "password").text
    print(res.split()[-1])  # Рыба-Меч


def m_6_4_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.3.3/index.html"
        driver.get(url)
        driver.add_cookie({"name": "secretKey", "value": "selenium123"})
        driver.refresh()
        res = driver.find_element(By.ID, "password").text
    print(res.split()[-1])  # J4m3s-B0nd-007


def m_6_5_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.5/index.html"
        driver.get(url)
        element = driver.find_element(By.ID, "target")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        res = driver.find_element(By.ID, "secret-key").text
    print(res.split()[-1])  # S1E2L3ENIUM-S1E2C3RET


# m_6_1_1()
# m_6_1_2()
# m_6_3_1()
# m_6_3_2()
# m_6_3_3()
# m_6_4_1()
# m_6_5_1()
