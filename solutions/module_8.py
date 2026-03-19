from time import sleep
import re
from selenium.webdriver.common.by import By
from main import get_driver


def m_8_1_1():
    with get_driver() as driver:
        driver.get("about:blank")
        res = 0
        data = (
            {"url": "https://parsinger.ru/selenium/8/8.1/site1/", "to_del": "439"},
            {"url": "https://parsinger.ru/selenium/8/8.1/site2/", "to_del": "780"},
        )

        for d in data:
            driver.switch_to.new_window("tab")
            driver.get(d["url"])
            num = "".join(
                n for n in driver.title if n not in d["to_del"] and n.isdigit()
            )
            res += int(num)
    print(res)  # 4135565044598459771911


def m_8_1_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/8/8.1.2/index.html"
        driver.get(url)
        first_tab = driver.window_handles[0]
        urls = [a.get_attribute("href") for a in driver.find_elements(By.TAG_NAME, "a")]
        res = []
        for url in urls:
            driver.switch_to.new_window("tab")
            driver.get(url)
            sleep(5)
            nums = driver.find_element(By.ID, "codePlaceholder").get_attribute(
                "data-numbers"
            )
            res.append(sum(map(int, nums.split(", "))))
        driver.switch_to.window(first_tab)
        driver.find_element(By.ID, "sumInput").send_keys(sum(res))
        driver.find_element(By.ID, "checkButton").click()
        res = driver.find_element(By.ID, "passwordDisplay").text
    print(res.split(":")[-1].strip())  # TH3-G4T3S-0F-H3LL-4R3-0P3N


def m_8_2_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/8/8.2.1/index.html"
        driver.get(url)
        driver.set_window_size(1200, 720)
        driver.find_element(By.ID, "checkSizeBtn").click()
        res = driver.find_element(By.ID, "secret").text
    print(res)  # K2Z6-N9a7-B3Z8-jJ2Q


def m_8_2_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/8/8.2.2/index.html"
        driver.get(url)
        sizes_sum = sum(driver.get_window_size().values())
        driver.find_element(By.ID, "answer").send_keys(sizes_sum)
        driver.find_element(By.ID, "checkBtn").click()
        res = driver.find_element(By.ID, "resultMessage").text
    print(res.split()[-1])  # W1DTH-GETSIZE2025-HE1GHT


def m_8_3_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/8/8.3.1/index.html"
        driver.get(url)
        driver.find_element(By.ID, "alertButton").click()
        driver.switch_to.alert.accept()
        driver.find_element(By.ID, "promptButton").click()

        alert = driver.switch_to.alert
        alert.send_keys("Alert")
        alert.accept()
        driver.find_element(By.ID, "confirmButton").click()
        driver.switch_to.alert.accept()
        sleep(1)
        res = driver.find_element(By.ID, "secretKey").text

    print(res.split()[-1])  # @L3RT-1T-1S-3ASY


def m_8_4_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/8/8.4.1/"
        driver.get(url)
        frame = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(frame)
        code = driver.page_source
        res = re.findall(r"\*(.*?)\*", code)
    print("".join(res))  # FrameMaster


def m_8_4_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/8/8.4.2/index.html"
        driver.get(url)
        done = []
        res = ""
        while len(done) < 4:
            frames = driver.find_elements(By.TAG_NAME, "iframe")
            for frame in frames:
                if frame not in done:
                    driver.switch_to.frame(frame)
                    if len(done) < 3:
                        driver.find_element(By.TAG_NAME, "button").click()
                    elif len(done) == 3:
                        res = driver.find_element(By.TAG_NAME, "h2").text
                    done.append(frame)
                    driver.switch_to.default_content()
        print(res.split()[-1])  # TH3-M4TR1X-H4S-C0NTR0LL3D-Y0U


def m_8_4_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/8/8.4.3/index.html"
        driver.get(url)
        res = ""
        for _ in range(4):
            frame = driver.find_element(By.TAG_NAME, "iframe")
            driver.switch_to.frame(frame)
            driver.find_element(By.TAG_NAME, "button").click()

        res = driver.find_element(By.CLASS_NAME, "password-container").text
    print(res)  # IM-IFRAME-N1NJ4


# m_8_1_1()
# m_8_1_2()
# m_8_2_1()
# m_8_2_2()
# m_8_3_1()
# m_8_4_1()
# m_8_4_2()
# m_8_4_3()
