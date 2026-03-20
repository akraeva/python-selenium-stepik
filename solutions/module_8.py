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


def m_8_5_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.8/1/index.html"
        driver.get(url)
        buttons = driver.find_element(By.CLASS_NAME, "main").find_elements(
            By.CLASS_NAME, "buttons"
        )
        for button in buttons:
            button.click()
            driver.switch_to.alert.accept()
            res = driver.find_element(By.ID, "result").text
            if res:
                break
    print(res)  # 321968541687435564865796413874


def m_8_5_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.8/2/index.html"
        driver.get(url)
        input_box = driver.find_element(By.CLASS_NAME, "res").find_element(
            By.ID, "input"
        )
        the_button = driver.find_element(By.CLASS_NAME, "res").find_element(
            By.ID, "check"
        )
        buttons = driver.find_element(By.CLASS_NAME, "main").find_elements(
            By.CLASS_NAME, "buttons"
        )
        for button in buttons:
            button.click()
            alert = driver.switch_to.alert
            code = alert.text
            alert.accept()
            input_box.send_keys(code)
            the_button.click()
            res = driver.find_element(By.ID, "result").text
            if res != "Неверный пин-код":
                break
    print(res)  # 867413857416874163897546183542


def m_8_5_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.8/3/index.html"
        driver.get(url)
        button = driver.find_element(By.ID, "check")
        pins = driver.find_element(By.CLASS_NAME, "pins-container").find_elements(
            By.CLASS_NAME, "pin"
        )
        for pin in pins:
            code = pin.text
            button.click()
            alert = driver.switch_to.alert
            alert.send_keys(code)
            alert.accept()
            res = driver.find_element(By.ID, "result").text
            if res != "Неверный пин-код":
                break
    print(res)  # 1261851212132345456274632


def m_8_5_4():
    with get_driver() as driver:
        url = "http://parsinger.ru/window_size/1/"
        driver.get(url)
        window_width, window_height = map(int, driver.get_window_size().values())
        view_width = driver.execute_script("return window.innerWidth")
        view_hight = driver.execute_script("return window.innerHeight")
        set_width = 555 + window_width - view_width
        set_hight = 555 + window_height - view_hight
        driver.set_window_size(set_width, set_hight)
        res = driver.find_element(By.ID, "result").text
    print(res)  # 1684163857416385746374


def m_8_5_5():
    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    with get_driver() as driver:
        url = "http://parsinger.ru/window_size/2/index.html"
        driver.get(url)
        window_width, window_height = map(int, driver.get_window_size().values())
        view_width = driver.execute_script("return window.innerWidth")
        view_hight = driver.execute_script("return window.innerHeight")
        x_correct = window_width - view_width
        y_correct = window_height - view_hight
        for x in window_size_x:
            for y in window_size_y:
                driver.set_window_size(x + x_correct, y + y_correct)
                res = driver.find_element(By.ID, "result").text
                if res:
                    print(res)  # 9874163854135461654
                    return


def m_8_5_6():
    window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    with get_driver() as driver:
        url = "http://parsinger.ru/window_size/2/index.html"
        driver.get(url)
        window_width, window_height = map(int, driver.get_window_size().values())
        view_width = driver.execute_script("return window.innerWidth")
        view_hight = driver.execute_script("return window.innerHeight")
        x_correct = window_width - view_width
        y_correct = window_height - view_hight
        for x in window_size_x:
            for y in window_size_y:
                driver.set_window_size(x + x_correct, y + y_correct)
                res = driver.find_element(By.ID, "result").text
                if res:
                    print(
                        f"{{'width': {x}, 'height': {y}}}"
                    )  # {'width': 955, 'height': 600}
                    return


def m_8_5_7():
    with get_driver() as driver:
        url = "http://parsinger.ru/blank/3/index.html"
        driver.get(url)
        buttons = driver.find_element(By.CLASS_NAME, "main").find_elements(
            By.CLASS_NAME, "buttons"
        )
        res = []
        first_tab = driver.window_handles[0]
        for button in buttons:
            button.click()
            current_tab = driver.window_handles[-1]
            driver.switch_to.window(current_tab)
            title = driver.title
            res.append(int(title))
            driver.switch_to.window(first_tab)
    print(sum(res))  # 77725787998028643152187739088279


def m_8_5_8():
    sites = [
        "http://parsinger.ru/blank/1/1.html",
        "http://parsinger.ru/blank/1/2.html",
        "http://parsinger.ru/blank/1/3.html",
        "http://parsinger.ru/blank/1/4.html",
        "http://parsinger.ru/blank/1/5.html",
        "http://parsinger.ru/blank/1/6.html",
    ]
    res = []
    with get_driver() as driver:
        driver.get("about:blank")
        for url in sites:
            driver.switch_to.new_window("tab")
            driver.get(url)
            driver.find_element(By.CLASS_NAME, "checkbox_class").click()

            num = driver.find_element(By.ID, "result").text
            num = int(num) ** 0.5
            res.append(num)
    print(round(sum(res), 9))  # 334703.720482347


def m_8_5_9():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.8/5/index.html"
        driver.get(url)
        res = ""
        chek_input = driver.find_element(By.ID, "guessInput")
        button = driver.find_element(By.ID, "checkBtn")
        frames = driver.find_element(By.ID, "main_container").find_elements(
            By.TAG_NAME, "iframe"
        )
        for frame in frames:
            driver.switch_to.frame(frame)
            driver.find_element(By.TAG_NAME, "button").click()
            num = driver.find_element(By.ID, "numberDisplay").text
            driver.switch_to.default_content()
            chek_input.send_keys(num)
            button.click()
            try:
                res = driver.switch_to.alert.text
                break
            except:
                chek_input.clear()
                continue
    print(res)  # FD79-32DJ-79XB-124S-P3DX-2456-DFB-DSA9


# m_8_1_1()
# m_8_1_2()
# m_8_2_1()
# m_8_2_2()
# m_8_3_1()
# m_8_4_1()
# m_8_4_2()
# m_8_4_3()
# m_8_5_1()
# m_8_5_2()
# m_8_5_3()
# m_8_5_4()
# m_8_5_5()
# m_8_5_6()
# m_8_5_7()
# m_8_5_8()
# m_8_5_9()
