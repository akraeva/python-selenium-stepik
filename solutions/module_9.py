from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from main import get_driver


def m_9_1_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.1.1/index.html"
        driver.get(url)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable(button)).click()
        res = driver.find_element(By.ID, "message").text
    print(res.split()[-1])  # CL1CK-N0W-0R-N3V3R


def m_9_2_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.2.1/index.html"
        driver.get(url)
        driver.find_element(By.ID, "startScan").click()
        WebDriverWait(driver, 30).until(EC.title_is("Access Granted"))
        res = driver.find_element(By.ID, "passwordValue").text
    print(res.split()[-1])  # H4CK3R_42


def m_9_3_1():
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/9/9.3.1/index.html"
        driver.implicitly_wait(7)
        driver.get(url)
        driver.find_element(By.ID, "startButton").click()
        for _ in range(5):
            driver.find_element(By.ID, "dynamicButton").click()
        res = driver.find_element(By.ID, "secretPassword").text
    print(res.split()[-1])  # W41T-4S-L0NG-4S-U-W4NT


def m_9_4_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.4.3/index.html"
        res_url = "https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure"
        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Правильный путь").click()
        WebDriverWait(driver, 10).until(EC.url_to_be(res_url))
        res = driver.find_element(By.ID, "password").text
    print(res)  # SECURE-URL-2025


def m_9_4_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.4.4/index.html"
        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Начать").click()
        current_url = driver.current_url
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))
        res = driver.find_element(By.ID, "password").text
    print(res.split()[-1])  # URL_CHANGED_2025


def m_9_4_3():
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html"
        driver.get(url)
        while True:
            driver.find_element(By.ID, "searchLink").click()
            if "qLChv49" in driver.current_url:
                driver.find_element(By.ID, "checkButton").click()
                res = driver.find_element(By.TAG_NAME, "p").text
                break
    print(res.split()[-1])  # N0-M0R3-HUNGRY-M0NK3Y


def m_9_4_4():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.4.2/index.html"
        driver.get(url)
        driver.find_element(By.ID, "startButton").click()
        url_pattern = r"^https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html$"
        res = 0
        while True:
            WebDriverWait(driver, 5).until(EC.url_changes(url))
            url = driver.current_url
            if EC.url_contains("index_2")(driver):
                break
            if EC.url_matches(url_pattern)(driver):
                num = driver.find_element(By.CLASS_NAME, "number").text
                res += int(num)
        driver.find_element(By.ID, "sumInput").send_keys(res)
        driver.find_element(By.ID, "checkButton").click()
        res = driver.find_element(By.ID, "result").text

    print(res.split()[-1])  # AbcD123XyZ


# m_9_1_1()
# m_9_2_1()
# m_9_3_1()
# m_9_4_1()
# m_9_4_2()
# m_9_4_3()
# m_9_4_4()
