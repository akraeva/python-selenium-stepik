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


def m_9_5_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.5.1/index.html"
        driver.get(url)
        locator = By.ID, "order-number"
        element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(locator)
        )
        res = element.text
    print(res)  # TR07NGM19XTR07NGM19X


def m_9_5_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.5.2/index.html"
        driver.get(url)
        locator = By.ID, "ghost-button"
        button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        button.click()
        res = driver.find_element(By.ID, "password-display").text
    print(res.split()[-1])  # 1234


def m_9_5_3():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/9/9.5.3/index.html"
        driver.get(url)
        driver.find_element(By.ID, "showProducts").click()
        locator = (By.CLASS_NAME, "product")
        elements = WebDriverWait(driver, 30).until(
            EC.visibility_of_all_elements_located(locator)
        )
        summ = 0
        for e in elements:
            price = e.find_element(By.CLASS_NAME, "price").text
            summ += int(price.strip("$"))
        driver.find_element(By.ID, "sumInput").send_keys(str(summ))
        driver.find_element(By.ID, "checkSum").click()
        key_locator = (By.ID, "secretMessage")
        res = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(key_locator))
            .text
        )
    print(res)  # S56P-8B0D-D3B4-PR1V


def m_9_6_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.6.1/index.html"
        driver.get(url)
        rate = "75.50"
        element = (By.ID, "usd-rate")
        WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element(element, rate))
        res_element = (By.ID, "secret-code")
        res = (
            WebDriverWait(driver, 30)
            .until(EC.visibility_of_element_located(res_element))
            .text
        )
    print(res)  # FOREX_HUNTER_2025


def m_9_6_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.6.2/index.html"
        driver.get(url)
        driver.find_element(By.ID, "ask-jaskier").click()
        text = "Селениумий"
        input_box = By.ID, "recipe_field"
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element_value(input_box, text)
        )
        res_element = (By.ID, "password")
        res = (
            WebDriverWait(driver, 30)
            .until(EC.visibility_of_element_located(res_element))
            .text
        )
    print(res)  # КаэрМорхен1258


def m_9_6_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.6.3/index.html"
        driver.get(url)
        atr, value = "src", "success"
        element = By.ID, "main-image"
        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element_attribute(element, atr, value)
        )
        driver.find_element(By.ID, "main-image").click()
        res_element = (By.ID, "password")
        res = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(res_element))
            .text
        )
    print(res)  # ARC-R34CT0R-P0W3R


def m_9_6_4():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.6.4/index.html"
        driver.get(url)
        atr = "confirmed"
        element = (By.ID, "booking-number")
        WebDriverWait(driver, 15).until(EC.element_attribute_to_include(element, atr))
        num = driver.find_element(By.ID, "booking-number").text
        driver.find_element(By.ID, "booking-input").send_keys(num)
        driver.find_element(By.ID, "check-button").click()
        res_element = (By.CLASS_NAME, "password-value")
        res = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(res_element))
            .text
        )
    print(res)  # SELENIUM_WAIT_MASTER


# m_9_1_1()
# m_9_2_1()
# m_9_3_1()
# m_9_4_1()
# m_9_4_2()
# m_9_4_3()
# m_9_4_4()
# m_9_5_1()
# m_9_5_2()
# m_9_5_3()
# m_9_6_1()
# m_9_6_2()
# m_9_6_3()
# m_9_6_4()
