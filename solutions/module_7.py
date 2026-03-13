from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
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


def m_7_3_1():
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/7/7.3.1/index.html"
        driver.get(url)
        griffin = driver.find_element(By.ID, "draggable")
        pool = driver.find_element(By.ID, "target")
        action = ActionChains(driver)
        action.drag_and_drop(griffin, pool)
        action.perform()
        res = driver.find_element(By.ID, "password").text
    print(res)  # 1-@M-THE-GR34T-@ND-T3RR1BL3-P3T3R-GR1FF1N


def m_7_3_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/7/7.3.2/index.html"
        driver.get(url)
        puple_circle = driver.find_element(By.ID, "dblclick-area")
        action = ActionChains(driver)
        action.double_click(puple_circle).perform()
        res = driver.find_element(By.ID, "password").text
    print(res)  # DoubleClick@2025


def m_7_3_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/7/7.3.3/index.html"
        driver.get(url)
        ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(
            Keys.SHIFT
        ).send_keys("T").key_up(Keys.SHIFT).key_up(Keys.ALT).key_up(
            Keys.CONTROL
        ).perform()
        res = driver.find_element(By.CSS_SELECTOR, "[key='access_code']").text
    print(res)  # KeyCombo@2025


def m_7_3_4():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/7/7.3.4/index.html"
        driver.get(url)
        context_area = driver.find_element(By.ID, "context-area")
        ActionChains(driver).context_click(context_area).perform()
        element = driver.find_element(By.CSS_SELECTOR, "[data-action='get_password'")
        element.click()
        res = driver.find_element(By.CSS_SELECTOR, "[key='access_code']").text
    print(res)  # RightClick@2025


def m_7_3_5():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/7/7.3.5/index.html"
        driver.get(url)
        containers = driver.find_elements(By.CLASS_NAME, "scroll-container")
        for c in containers:
            c.click()
            status = c.find_element(By.CLASS_NAME, "status")
            while status.text != "Прокручено!":
                ActionChains(driver).send_keys(Keys.END).perform()
        WebDriverWait(driver, 2).until(
            lambda d: d.find_element(By.CSS_SELECTOR, "[key='access_code']").text != ""
        )
        res = driver.find_element(By.CSS_SELECTOR, "[key='access_code']").text
    print(res)  # UltimateSecret@2025


# m_7_1_1()
# m_7_2_1()
# m_7_3_1()
# m_7_3_2()
# m_7_3_3()
# m_7_3_4()
# m_7_3_5()
