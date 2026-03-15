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


def m_7_4_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/7/7.4.1/index.html"
        driver.get(url)
        element = driver.find_element(By.CLASS_NAME, "long-page")
        ActionChains(driver).move_to_element(element).scroll_by_amount(
            0, 1200
        ).perform()
        sleep(3)
        data = (
            driver.find_element(By.CLASS_NAME, "step-wrapper")
            .find_element(By.CLASS_NAME, "countdown")
            .text
        )
        ActionChains(driver).move_to_element(element).scroll_by_amount(
            0, 1200
        ).perform()
        div = driver.find_elements(By.CLASS_NAME, "step-wrapper")[-1]
        div.find_element(By.TAG_NAME, "input").send_keys(data.split()[-1])
        div.find_element(By.TAG_NAME, "button").click()
        sleep(3)
        res = driver.find_element(By.ID, "final-key").text
    print(res.split()[-1])  # S9ECRET-K9EY-9999


def m_7_5_1():
    with get_driver() as driver:
        url = "http://parsinger.ru/scroll/2/index.html"
        driver.get(url)
        res = 0
        elements = driver.find_elements(By.CLASS_NAME, "item")
        for e in elements:
            e.find_element(By.TAG_NAME, "input").click()
            num = e.find_element(By.TAG_NAME, "span").text
            if num.isdigit():
                res += int(num)
    print(res)  # 13310


def m_7_5_2():
    with get_driver() as driver:
        url = "http://parsinger.ru/infiniti_scroll_1/"
        driver.get(url)
        div = driver.find_element(By.CLASS_NAME, "scroll-container")
        spans = []
        res = 0
        while len(spans) < 100:
            sleep(1)
            data = div.find_elements(By.TAG_NAME, "span")
            for span in data:
                id = span.get_attribute("id")
                if id not in spans:
                    num = span.text
                    if num.isdigit():
                        res += int(num)
                    spans.append(id)
            div.send_keys(Keys.PAGE_DOWN)
    print(res)  # 86049950


def m_7_5_3():
    with get_driver() as driver:
        url = "http://parsinger.ru/infiniti_scroll_2/"
        driver.get(url)
        div = driver.find_element(By.CLASS_NAME, "scroll-container")
        elements = []
        res = 0
        while len(elements) < 100:
            sleep(1)
            data = div.find_elements(By.TAG_NAME, "p")
            ActionChains(driver).send_keys(Keys.END).perform()
            for p in data:
                id = p.get_attribute("id")
                if id not in elements:
                    num = p.text
                    if num.isdigit():
                        res += int(num)
                    elements.append(id)
            ActionChains(driver).move_to_element(div).click().scroll_by_amount(
                0, 100
            ).perform()
    print(res)  # 499917600


def m_7_5_4():
    def summ(div):
        elements = []
        res = 0
        while len(elements) < 100:
            data = div.find_elements(By.TAG_NAME, "span")
            for span in data:
                id = span.get_attribute("id")
                if id not in elements:
                    num = span.text
                    if num.isdigit():
                        res += int(num)
                    elements.append(id)
            ActionChains(driver).move_to_element(div).click().send_keys(
                Keys.PAGE_DOWN
            ).perform()
        return res

    with get_driver() as driver:
        url = "http://parsinger.ru/infiniti_scroll_3/"
        driver.get(url)
        divs = driver.find_element(By.CLASS_NAME, "main").find_elements(
            By.XPATH, "./div"
        )
        result = 0
        for div in divs:
            result += summ(div)
        print(result)  # 159858750


def m_7_5_5():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.7/1/index.html"
        driver.get(url)
        div = driver.find_element(By.ID, "floating-container")
        buttons = div.find_elements(By.CLASS_NAME, "clickMe")
        for b in buttons:
            driver.execute_script("return arguments[0].scrollIntoView(true);", b)
            b.click()
        res = driver.switch_to.alert.text
    print(res)  # JKf9-034D-DE02-PB2G-QB8Z-81VN-30GK-IO90-UT89


def m_7_5_6():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.7/5/index.html"
        driver.get(url)
        buttons = driver.find_element(By.ID, "main_container").find_elements(
            By.CLASS_NAME, "timer_button"
        )
        for b in buttons:
            timer = round(float(b.get_attribute("value")) + 1)
            (ActionChains(driver).click_and_hold(b).pause(timer).release().perform())
        res = driver.switch_to.alert.text
    print(res)  # GFL4-ED40-F32F-HJ24-0BXS-235N-PIRE-123VD-123F


def m_7_5_7():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/5.7/4/index.html"
        driver.get(url)
        main_container = driver.find_element(By.ID, "main_container")
        cheked = []
        while len(cheked) < 100:
            divs = main_container.find_elements(By.CLASS_NAME, "child_container")
            for line in divs:
                if line not in cheked:
                    inboxes = line.find_elements(By.TAG_NAME, "input")
                    for i in inboxes:
                        value = i.get_attribute("value")
                        if int(value) % 2 == 0:
                            i.click()
                    cheked.append(line)
            main_container.send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.CLASS_NAME, "alert_button").click()
        res = driver.switch_to.alert.text
    print(res)  # 5402f04236450f263540jk406504l506


def m_7_5_8():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/7/7.5/index.html"
        driver.get(url)
        div = driver.find_element(By.ID, "container")
        data = []
        data_len = -1
        res = 0
        while len(data) != data_len:
            data_len = len(data)
            divs = div.find_elements(By.CLASS_NAME, "card")
            for d in divs:
                if d not in data:
                    like = d.find_element(By.CLASS_NAME, "like-btn")
                    like.click()
                    num = d.find_element(By.CLASS_NAME, "big-number").text
                    res += int(num)
                    data.append(d)
            div.send_keys(Keys.PAGE_DOWN)
            sleep(1)
        input()
    print(res)  # 500000


# m_7_1_1()
# m_7_2_1()
# m_7_3_1()
# m_7_3_2()
# m_7_3_3()
# m_7_3_4()
# m_7_3_5()
# m_7_4_1()
# m_7_5_1()
# m_7_5_2()
# m_7_5_3()
# m_7_5_4()
# m_7_5_5()
# m_7_5_6()
# m_7_5_7()
# m_7_5_8()
