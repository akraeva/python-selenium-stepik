from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from main import get_driver
import random


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


def m_9_7_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.7.1/index.html"
        driver.get(url)
        driver.find_element(By.ID, "address").send_keys("Сергиев Посад")
        payment = Select(driver.find_element(By.ID, "payment"))
        payment.select_by_index(random.randint(1, 2))
        driver.find_element(By.ID, "submit-order").click()
        spinner = (By.ID, "spinner")
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(spinner))
        confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "confirm-address"))
        )
        confirm.click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element(confirm))
        driver.find_element(By.ID, "get-code").click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # 5TR4NG3R-D3M0G0N-001


def m_9_7_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.7.2/index.html"
        driver.get(url)
        driver.find_element(By.CLASS_NAME, "search-box").send_keys("Lorem Ipsum")
        driver.find_element(By.ID, "search-button").click()
        old_locator = (By.ID, "old-result")
        old_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(old_locator)
        )
        WebDriverWait(driver, 10).until(EC.staleness_of(old_element))
        driver.find_element(By.ID, "secret-button").click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # S34RCH-K3Y


def m_9_7_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/9/9.7.3/index.html"
        driver.get(url)
        driver.find_element(By.ID, "summonBtn").click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(5))
        driver.find_element(By.ID, "passwordBtn").click()
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        res = alert.text
        alert.accept()
    print(res.split()[-1])  # X1Y0-A2B3-Z4XC


def m_9_8_1():
    with get_driver() as driver:
        url = "http://parsinger.ru/expectations/3/index.html"
        driver.get(url)
        button_locator = (By.ID, "btn")
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()
        WebDriverWait(driver, 30).until(EC.title_is("345FDG3245SFD"))
        res = driver.find_element(By.ID, "result").text
    print(res)  # 82934401788.40141


def m_9_8_2():
    with get_driver() as driver:
        url = "http://parsinger.ru/expectations/4/index.html"
        driver.get(url)
        button_locator = (By.ID, "btn")
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()
        WebDriverWait(driver, 30).until(EC.title_contains("JK8HQ"))
        res = driver.title
    print(res)  # 33GBK-98C3X-K8PKB-JK8HQ-DMXMQ


def m_9_8_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/expectations/6/index.html"
        driver.get(url)
        button_locator = (By.ID, "btn")
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()
        element_locator = (By.CLASS_NAME, "BMH21YY")
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(element_locator)
        )
        res = element.text
    print(res)  # 688596737976


def m_9_8_4():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.9/2/index.html"
        driver.get(url)
        element_locator = (By.ID, "qQm9y1rk")
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(element_locator)
        )
        element.click()
        res = driver.switch_to.alert.text
    print(res)  # tlprcp6S-kDbhujKo-uh7Rv9f9-irv26iU9-Zt2XZcIm


def m_9_8_5():
    ids_to_find = [
        "xhkVEkgm",
        "QCg2vOX7",
        "8KvuO5ja",
        "CFoCZ3Ze",
        "8CiPCnNB",
        "XuEMunrz",
        "vmlzQ3gH",
        "axhUiw2I",
        "jolHZqD1",
        "ZM6Ms3tw",
        "25a2X14r",
        "aOSMX9tb",
        "YySk7Ze3",
        "QQK13iyY",
        "j7kD7uIR",
    ]
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/5.9/3/index.html"
        driver.get(url)
        for element_id in ids_to_find:
            element = driver.find_element(By.ID, element_id)
            WebDriverWait(driver, 15).until(EC.visibility_of(element))
            element.click()
        res = driver.switch_to.alert.text
    print(res)  # CFoCZ3Ze-8CiPCnNB-XuEMunrz-vmlzQ3gH-axhUiw2I-QQK13iyY-j7kD7uIR


def m_9_8_6():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/5.9/4/index.html"
        driver.get(url)
        element = driver.find_element(By.ID, "closeBtn")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element))
        element.click()
        WebDriverWait(driver, 60).until(EC.invisibility_of_element(element))
        driver.find_element(By.TAG_NAME, "button").click()
        res = driver.find_element(By.ID, "message").text
    print(res)  # FS03-R9R3-SVV9-3P05-DSS1-01VI


def m_9_8_7():
    res = []
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/5.9/5/index.html"
        driver.get(url)

        buttons = driver.find_element(By.ID, "main_container").find_elements(
            By.CLASS_NAME, "box_button"
        )
        for button in buttons:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button))
            button.click()
            banner = driver.find_element(By.ID, "ad_window")
            close_btn = banner.find_element(By.ID, "close_ad")
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(close_btn)
            ).click()
            WebDriverWait(driver, 20).until(EC.invisibility_of_element(banner))
            WebDriverWait(driver, 30).until(lambda d: button.text)
            res.append(button.text)
    print("-".join(res))  # F34S-FFS3-56FGH-LKJ0-2E9D-440D-4Q0D-230S-D120


def m_9_8_8():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.9/6/index.html"
        driver.get(url)
        check_box = driver.find_element(By.ID, "myCheckbox")
        WebDriverWait(driver, 30).until(EC.element_to_be_selected(check_box))
        driver.find_element(By.TAG_NAME, "button").click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # 34D0-3SCV-SCM0-654R-DVM9-42IU


def m_9_8_9():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.9/7/index.html"
        driver.get(url)
        containers = driver.find_elements(By.CLASS_NAME, "container")
        for container in containers:
            check_box = container.find_element(By.TAG_NAME, "input")
            button = container.find_element(By.TAG_NAME, "button")
            WebDriverWait(driver, 30).until(EC.element_to_be_selected(check_box))
            button.click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # GFD9-3SV0-3280-WEZC-23UN-Q921-3G5D


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
# m_9_7_1()
# m_9_7_2()
# m_9_7_3()
# m_9_8_1()
# m_9_8_2()
# m_9_8_3()
# m_9_8_4()
# m_9_8_5()
# m_9_8_6()
# m_9_8_7()
# m_9_8_8()
# m_9_8_9()
