import json
import gzip
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
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


def stepik_selenium_python_m10_cdp():
    """
    Скрипт для извлечения JSON-данных с веб-страниц с использованием CDP
    - Автоматически фильтрует только JSON-ответы
    - Декодирует данные и преобразует их в Python-объекты
    - Сохраняет каждый найденный JSON в отдельный файл
    """

    options = Options()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    # Функция для фильтрации JSON-ответов
    def log_filter(log_):
        return (
            log_["method"] == "Network.responseReceived"
            and "json" in log_["params"]["response"]["mimeType"]
        )

    with webdriver.Chrome(options=options) as browser:
        browser.get("http://31.130.149.237/json_extraction")
        sleep(10)

        # Если нужно — можно инициировать события тут, например клик или ввод
        # browser.find_element(...).click()

        # Получаем "сырые" логи производительности (Performance logs)
        logs_raw = browser.get_log("performance")

        # Фильтруем и вытаскиваем полезные JSON-сообщения
        logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

        # Счетчик найденных JSON
        json_count = 0

        print("\n" + "=" * 80)
        print("НАЧАЛО СБОРА JSON-ДАННЫХ")
        print("=" * 80 + "\n")

        # Перебираем отфильтрованные логи (только JSON-ответы)
        for log in filter(log_filter, logs):
            try:
                request_id = log["params"]["requestId"]
                resp_url = log["params"]["response"]["url"]

                json_count += 1
                print("\n" + "=" * 80)
                print(f"JSON #{json_count}")
                print(f"URL: {resp_url}")

                body = browser.execute_cdp_cmd(
                    "Network.getResponseBody", {"requestId": request_id}
                )

                # Попытка сохранить JSON в файл
                try:
                    # После этой строки у вас есть готовый Python-объект json_data, с которым можно выполнять любые операции.
                    json_data = json.loads(body["body"])

                    # Сохраняем JSON напрямую в директории скрипта
                    filename = f"json_{json_count}.json"
                    with open(filename, "w", encoding="utf-8") as f:
                        json.dump(json_data, f, indent=4, ensure_ascii=False)
                    print(f"Сохранено в файл: {filename}")
                except Exception as e:
                    print(f"Ошибка при сохранении JSON: {e}")
                    # Если не удалось обработать как JSON, сохраняем текст как есть
                    fallback_filename = f"raw_response_{json_count}.txt"
                    with open(fallback_filename, "w", encoding="utf-8") as f:
                        f.write(body["body"])
                    print(f"Сохранен необработанный ответ в: {fallback_filename}")

            except WebDriverException:
                print("Нет Body для данного запроса")
                continue


def stepik_selenium_python_m10_wire():
    """
    Скрипт сохраняет найденные JSON-ответы в отдельные файлы (json_1.json, json_2.json, ...).
    Используется selenium-wire для перехвата сетевых запросов, поддерживается обработка gzip.
    """
    URL = "http://31.130.149.237/json_extraction"
    options = webdriver.ChromeOptions()
    # Отключаем автоматическое обновление HTTP до HTTPS т.к. тренажер работает на 80 порту HTTP
    options.add_argument("--disable-features=HttpsUpgrades")

    with webdriver.Chrome(options=options) as browser:
        # Открываем страницу
        browser.get(URL)
        # Ждем загрузки страницы и AJAX-запросов
        sleep(5)

        # Если нужно — можно инициировать события тут, например клик или ввод
        # browser.find_element(...).click()

        json_count = 0  # Счетчик найденных JSON и отсеиваем по длине
        # Перебираем все запросы
        for request in browser.requests:
            # Проверяем, что есть ответ и это JSON с длинной более 50 байтов
            if (
                request.response
                and "application/json"
                in request.response.headers.get("Content-Type", "")
                and len(request.response.body) > 50
            ):
                try:
                    # Получаем тело ответа
                    body = request.response.body  # Получаем сырые данные ответа

                    # Проверяем, является ли ответ сжатым (gzip)
                    if request.response.headers.get("Content-Encoding") == "gzip":
                        body = gzip.decompress(body)  # Распаковываем gzip сжатие

                    # Декодируем ответ в UTF-8
                    decoded_body = body.decode("utf-8", errors="replace")

                    # Парсим JSON
                    # После этой строки у вас есть полноценный Python-объект json_data, с которым вы можете выполнять любые операции
                    json_data = json.loads(
                        decoded_body
                    )  # Преобразуем текст в объект Python

                    # Форматируем JSON для сохранения
                    formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
                    # Увеличиваем счетчик и сохраняем JSON
                    json_count += 1
                    # Выводим информацию о найденном JSON
                    print("\n" + "=" * 80)  # Печатаем разделитель
                    print(f"URL: {request.url}")  # Печатаем URL запроса
                    # Сохраняем JSON в файл
                    with open(
                        f"json_{json_count}.json", "w", encoding="utf-8"
                    ) as f:  # Открываем файл для записи
                        f.write(formatted_json)  # Записываем JSON в файл
                    print(f"Сохранен в json_{json_count}.json")  # Печатаем имя файла
                except Exception as e:  # Обрабатываем возможные ошибки
                    print(
                        f"Ошибка при обработке ответа: {str(e)}"
                    )  # Печатаем сообщение об ошибке

        # Выводим итоговую статистику
        print(
            f"\nВсего найдено и сохранено JSON: {json_count}"
        )  # Печатаем общее количество найденных JSON


def m_10_3_1():
    options = Options()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    def log_filter(log_):
        return (
            log_["method"] == "Network.responseReceived"
            and "json" in log_["params"]["response"]["mimeType"]
        )

    with webdriver.Chrome(options=options) as driver:
        driver.get("http://31.130.149.237/json_extraction")
        button_locator = (By.ID, "contactsButton")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(button_locator))
        driver.find_element(*button_locator).click()
        modal = driver.find_element(By.ID, "contactsModal")
        WebDriverWait(driver, 10).until(EC.visibility_of(modal))
        logs_raw = driver.get_log("performance")
        logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
        res = ""
        for log in filter(log_filter, logs):
            try:
                request_id = log["params"]["requestId"]
                body = driver.execute_cdp_cmd(
                    "Network.getResponseBody", {"requestId": request_id}
                )
                json_data = json.loads(body["body"])
                if "stores" in json_data.keys():
                    for store in json_data["stores"]:
                        if store["id"] == 2:
                            res = store["coordinates"]["lng"]
                            break

            except WebDriverException:
                continue
    print(res)  # 30.332


def m_10_3_2():
    options = Options()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    def log_filter(log_):
        return (
            log_["method"] == "Network.responseReceived"
            and "json" in log_["params"]["response"]["mimeType"]
        )

    with webdriver.Chrome(options=options) as driver:
        driver.get("http://31.130.149.237/json_extraction")
        book_card = (By.CLASS_NAME, "book-card")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(book_card))
        logs_raw = driver.get_log("performance")
        logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
        res = 0
        for log in filter(log_filter, logs):
            try:
                request_id = log["params"]["requestId"]
                body = driver.execute_cdp_cmd(
                    "Network.getResponseBody", {"requestId": request_id}
                )
                json_data = json.loads(body["body"])
                books = json_data["data"]
                for book in books:
                    data = (book["id"], book["year"], book["price"])
                    res += sum(map(int, data))
            except WebDriverException:
                continue
    print(res)  # 16643


def m_10_3_3():
    options = Options()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    def log_filter(log_):
        return (
            log_["method"] == "Network.responseReceived"
            and "json" in log_["params"]["response"]["mimeType"]
        )

    with webdriver.Chrome(options=options) as driver:
        driver.get("http://31.130.149.237/json_extraction")
        book_card = (By.CLASS_NAME, "book-card")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(book_card))
        stop_scroll = driver.find_element(By.ID, "endMessage")
        while not stop_scroll.is_displayed():
            driver.execute_script("window.scrollBy(0, 300);")

        logs_raw = driver.get_log("performance")
        logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
        res = []
        for log in filter(log_filter, logs):
            try:
                request_id = log["params"]["requestId"]
                body = driver.execute_cdp_cmd(
                    "Network.getResponseBody", {"requestId": request_id}
                )
                json_data = json.loads(body["body"])
                books = json_data["data"]
                for book in books:
                    if "password" in book.keys():
                        res.append(book["password"])
            except WebDriverException:
                continue
    print("-".join(res))  # JSON-EXTRACTION-POWER-SUM-BOOKS-PASS


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
# m_10_3_1()
# m_10_3_2()
# m_10_3_3()
