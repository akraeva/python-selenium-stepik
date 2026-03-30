from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from main import get_driver


def m_10_1_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/draganddrop/1/index.html"
        driver.get(url)
        element = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "field2")
        ActionChains(driver).drag_and_drop(element, target).perform()
        res = driver.find_element(By.ID, "result").text
    print(res)  # ODYzNDQ1MzM0NTE0MzQ2OTAwMA==


def m_10_1_2():
    res = ""
    with get_driver(False) as driver:
        url = "https://parsinger.ru/draganddrop/3/index.html"
        driver.get(url)
        control_points = driver.find_elements(By.CLASS_NAME, "controlPoint")
        block = driver.find_element(By.ID, "block1")
        for point in control_points:
            ActionChains(driver).drag_and_drop(block, point).perform()
        code = driver.find_element(By.ID, "message")
        WebDriverWait(driver, 60).until(EC.visibility_of(code))
        res = code.text
    print(res)  # Ni44NTc4MTk2NzY4NTQ0NTZlKzIz


def m_10_1_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.10/2/index.html"
        driver.get(url)
        green_squares = driver.find_elements(By.CLASS_NAME, "draganddrop")
        grey_zone = driver.find_element(By.CLASS_NAME, "draganddrop_end")
        for square in green_squares:
            ActionChains(driver).drag_and_drop(square, grey_zone).perform()
        code = driver.find_element(By.ID, "message")
        res = code.text
    print(res)  # 39FG-3490-34F0-944S-34FV-80VX-F3GJ-349B


def m_10_1_4():
    with get_driver() as driver:
        url = "https://parsinger.ru/draganddrop/2/index.html"
        driver.get(url)
        orange_circle = driver.find_element(By.ID, "draggable")
        boxes = driver.find_elements(By.CLASS_NAME, "box")
        for b in boxes:
            ActionChains(driver).drag_and_drop(orange_circle, b).perform()
        code = driver.find_element(By.ID, "message")
        res = code.text
    print(res)  # NS4zNDUzMzU0NTQ2MzU0NDVlKzIx


def m_10_1_5():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/5.10/3/index.html"
        driver.get(url)
        driver.maximize_window()
        code = driver.find_element(By.ID, "message")
        elements, targets = {}, {}
        container = driver.find_element(By.ID, "main_container")
        blocks = container.find_elements(By.TAG_NAME, "div")
        for block in blocks:
            if block.get_attribute("class") == "draganddrop_end":
                dic = targets
                color = block.value_of_css_property("border-color").strip("rgb()")
            else:
                color = block.value_of_css_property("background-color").strip("rgba()")
                color = color.rsplit(", ", 1)[0]
                dic = elements
            dic[color] = block
        while not (res := code.text):
            for color in elements.keys():
                ActionChains(driver).drag_and_drop(
                    elements[color], targets[color]
                ).perform()

    print(res)  # F934-3902-2FH4-DV02-3454-9HCX-4F53-12FS


def m_10_1_6():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/5.10/4/index.html"
        driver.get(url)
        driver.maximize_window()
        code = driver.find_element(By.CLASS_NAME, "message")
        basket_with_toys = driver.find_element(By.CLASS_NAME, "basket_with_toys")
        balls = basket_with_toys.find_elements(By.TAG_NAME, "div")
        baskets = driver.find_elements(By.CSS_SELECTOR, ".basket_color")
        basket_color = {
            basket.value_of_css_property("background-color"): basket
            for basket in baskets
        }
        for ball in balls:
            color = ball.value_of_css_property("background-color")
            ActionChains(driver).drag_and_drop(ball, basket_color[color]).perform()
        res = code.text
    print(res)  # ER96-SVN0-34HX-ER3W-WHJ5-WHG4-SNJ1-12LO


def m_10_1_7():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/5.10/8/index.html"
        driver.get(url)
        code = driver.find_element(By.ID, "message")
        balls = driver.find_element(By.ID, "pieces_container").find_elements(
            By.TAG_NAME, "div"
        )
        for ball in balls:
            x = ball.get_attribute("id").split("_")[-1]
            ActionChains(driver).drag_and_drop_by_offset(ball, int(x) + 24, 0).perform()
        res = WebDriverWait(driver, 30).until(lambda d: code.text)
    print(res)  # GD60-34JX-354F-3HJC-NXC0-54KO-W3B1-2DFH-23JG


def m_10_1_8():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/5.10/6/index.html"
        driver.get(url)
        sliders = driver.find_elements(By.CLASS_NAME, "slider-row")
        for slider in sliders:
            s = slider.find_element(By.CLASS_NAME, "volume-slider")
            target = int(slider.find_element(By.CLASS_NAME, "target-value").text)
            current = int(s.get_attribute("value"))
            direction = Keys.ARROW_RIGHT if target > current else Keys.ARROW_LEFT
            while target != current:
                s.send_keys(direction)
                current = int(s.get_attribute("value"))
        code = driver.find_element(By.ID, "message")
        res = WebDriverWait(driver, 20).until(EC.visibility_of(code)).text
    print(res)  # 3F9D-DVB0-EH46-96VB-JHJ5-34UK-2SSF-JKG0


def m_10_1_9():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/draganddrop/4/index.html"
        driver.get(url)
        word = driver.find_element(By.ID, "target-word").text
        slots = driver.find_element(By.ID, "letter-slots").find_elements(
            By.CLASS_NAME, "letter-slot"
        )

        for i, letter in enumerate(word):
            target = slots[i]
            element = driver.find_element(By.XPATH, f"//div[text()='{letter}']")
            ActionChains(driver).drag_and_drop(element, target).perform()
        res = driver.find_element(By.ID, "password").text
    print(res)  # 0000-MAGIC-WORD-0000


def m_10_2_1():
    url = "https://parsinger.ru/selenium/stealth/1/index.html"
    with get_driver() as driver:
        driver.get(url)
        code = driver.find_element(By.ID, "verification-code").text

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=options)
    with browser as driver:
        driver.get(url)
        driver.find_element(By.ID, "verification-input").send_keys(code)
        driver.find_element(By.ID, "check-button").click()
        res_element = driver.find_element(By.ID, "secret")
        res = WebDriverWait(driver, 20).until(EC.visibility_of(res_element)).text
    print(res.split()[-1])  # Web1-Driver-Masked-0000


# m_10_1_1()
# m_10_1_2()
# m_10_1_3()
# m_10_1_4()
# m_10_1_5()
# m_10_1_6()
# m_10_1_7()
# m_10_1_8()
# m_10_1_9()
# m_10_2_1()
