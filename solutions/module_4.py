from selenium.webdriver.common.by import By
from main import get_driver
from time import sleep


def your_ip():
    url = "https://2ip.ru/"
    with get_driver() as driver:
        driver.get(url)
        sleep(5)
        clip_button = driver.find_element(By.ID, "d_clip_button")
        res = clip_button.find_element(By.TAG_NAME, "span").text
    print(res)


def m_4_3_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/3/3.2.1/index.html"
        driver.get(url)
        button = driver.find_element(By.ID, "clickButton")
        button.click()
        code = driver.find_element(By.ID, "codeOutput").text
    print(code)  # Шаи-Хулуд


def m_4_3_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/3/3.2.2/index.html"
        driver.get(url)
        input_field = driver.find_element(By.ID, "codeInput")
        input_field.send_keys("Дрогон")
        sleep(1)
        button = driver.find_element(By.ID, "clickButton")
        button.click()
        sleep(1)
        res = driver.find_element(By.ID, "codeOutput").text
    print(res)  # DR4G0N-F1R3


def m_4_3_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/3/3.2.3/index.html"
        driver.get(url)
        driver.find_element(By.ID, "showTextBtn").click()
        result = driver.find_element(By.ID, "text1").text
        driver.find_element(By.ID, "userInput").send_keys(result)
        driver.find_element(By.ID, "checkBtn").click()
        res = driver.find_element(By.ID, "text2").text
    print(res)  # G00D-J0B-T0M-P0W3R


def m_4_3_4():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/3/3.2.4/index.html"
        driver.get(url)
        button = driver.find_element(By.ID, "secret-key-button")
        button.click()
        res = button.get_attribute("data")
    print(res)  # TH3-S3CR3T-K3Y-IS-Y0URS


# your_ip()
# m_4_3_1()
# m_4_3_2()
# m_4_3_3()
# m_4_3_4()
