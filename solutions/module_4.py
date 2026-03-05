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


def m_4_4_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/3/3.3.3/index.html"
        driver.get(url)
        links = driver.find_elements(By.TAG_NAME, "a")
        total = 0
        for link in links:
            num = link.get_attribute("stormtrooper")
            try:
                total += int(num)
            except:
                continue
        driver.find_element(By.ID, "inputNumber").send_keys(str(total))
        driver.find_element(By.ID, "checkBtn").click()
        res = driver.find_element(By.ID, "feedbackMessage").text
    print(res.split()[-1])  # 7H3-D4RK-S1D3-4LW4YS-W1NS


def m_4_4_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/3/3.3.1/index.html"
        driver.get(url)
        parent = driver.find_element(By.ID, "parent_id")
        child = parent.find_element(By.CLASS_NAME, "child_class")
        child.click()
        res = child.get_attribute("password")
    print(res)  # GET-TH1S-C0D3


def m_4_4_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/3/3.3.2/index.html"
        driver.get(url)
        blocks = driver.find_elements(By.CLASS_NAME, "block")
        for block in blocks:
            block.find_element(By.TAG_NAME, "button").click()
        res = driver.find_element(By.TAG_NAME, "password").text
    print(res)  # H1DD3N-P4SS-W0RD


def m_4_5_1():
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/1/1.html"
        driver.get(url)
        inputs = driver.find_elements(By.CLASS_NAME, "form")
        for inpt in inputs:
            inpt.send_keys("Text")
        driver.find_element(By.CLASS_NAME, "btn").click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # 1123581321345589144233377610987


def m_4_5_2():
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/2/2.html"
        driver.get(url)
        driver.find_element(By.LINK_TEXT, "16243162441624").click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # 324165465463156465


def m_4_5_3():
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/3/3.html"
        driver.get(url)
        data = driver.find_elements(By.TAG_NAME, "p")
        res = 0
        for p in data:
            try:
                res += int(p.text)
            except:
                continue
    print(res)  # 450384194300


def m_4_5_4():
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/3/3.html"
        driver.get(url)
        data = driver.find_elements(By.XPATH, "//div[@class='text']/p[2]")
        res = 0
        for p in data:
            try:
                res += int(p.text)
            except:
                continue
    print(res)  # 149494128600


def m_4_5_5():
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/4/4.html"
        driver.get(url)
        chekc_box = driver.find_elements(By.CLASS_NAME, "check")
        for cb in chekc_box:
            cb.click()
        driver.find_element(By.CLASS_NAME, "btn").click()
        sleep(3)
        res = driver.find_element(By.ID, "result").text
    print(res)  # 3,1415926535897932384626433832795028841971


def m_4_5_6():
    # fmt: off
    numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38, 
        39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73, 
        74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118, 
        119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153, 
        154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
        187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207, 
        208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233, 
        234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255, 
        256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
        292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314, 
        318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349, 
        353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412, 
        419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451, 
        452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479, 
        480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]
    # fmt: on
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/5/5.html"
        driver.get(url)
        chekc_box = driver.find_elements(By.CLASS_NAME, "check")
        for cb in chekc_box:
            if int(cb.get_property("value")) in numbers:
                cb.click()
        driver.find_element(By.CLASS_NAME, "btn").click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # 932169874631968746874987464354


def m_4_5_7():
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/7/7.html"
        driver.get(url)
        data = driver.find_elements(By.TAG_NAME, "option")
        data_sum = 0
        for d in data:
            data_sum += int(d.text)
        driver.find_element(By.ID, "input_result").send_keys(data_sum)
        driver.find_element(By.CLASS_NAME, "btn").click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # 321687416587463168743416874641687


def m_4_5_8():
    with get_driver() as driver:
        url = "http://parsinger.ru/selenium/6/6.html"
        driver.get(url)
        num = ((12434107696 * 3) * 2) + 1
        data = driver.find_elements(By.TAG_NAME, "option")
        for d in data:
            if d.text == str(num):
                d.click()
                break
        driver.find_element(By.CLASS_NAME, "btn").click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # 98763216843164361841357461685743168461


# your_ip()
# m_4_3_1()
# m_4_3_2()
# m_4_3_3()
# m_4_3_4()
# m_4_4_1()
# m_4_4_2()
# m_4_4_3()
# m_4_5_1()
# m_4_5_2()
# m_4_5_3()
# m_4_5_4()
# m_4_5_5()
# m_4_5_6()
# m_4_5_7()
# m_4_5_8()
