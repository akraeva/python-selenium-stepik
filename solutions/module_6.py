from time import sleep
from selenium.webdriver.common.by import By
from main import get_driver


def m_6_1_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.2/index.html"
        driver.get(url)
        elem = driver.find_element(By.TAG_NAME, "a")
        elem.click()
        elem = driver.find_element(By.TAG_NAME, "a")
        elem.click()
        driver.back()
        driver.back()
        button = driver.find_element(By.ID, "getPasswordBtn")
        button.click()
        alert = driver.switch_to.alert
        res = alert.text
    print(res.split(":")[-1].strip())  # B@ck 1n Bl@ck


def m_6_1_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.2.1/index.html"
        driver.get(url)
        elem = driver.find_element(By.ID, "this_pic")
        elem.screenshot("res_6_1_2.png")  # 2323


def m_6_3_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.3.1/index.html"
        driver.get(url)
        token = driver.get_cookie("token_22")
        res = token["value"]
    print(res)  # V78lmnOPQ123rstUVW456xyzABC


def m_6_3_2():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.3/index.html"
        driver.get(url)
        data = driver.get_cookies()
        song = next(d["name"] for d in data if "name" in d.keys())
        driver.find_element(By.ID, "phraseInput").send_keys(song)
        driver.find_element(By.ID, "checkButton").click()
        res = driver.find_element(By.ID, "result").text
    print(res)  # Th3r3-1s-N0-W0rd-M1ss-1n-Pudg35-D1ct10n@ry


def m_6_3_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.3.2/index.html"
        driver.get(url)
        driver.delete_all_cookies()
        sleep(3)
        res = driver.find_element(By.ID, "password").text
    print(res.split()[-1])  # Рыба-Меч


def m_6_4_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.3.3/index.html"
        driver.get(url)
        driver.add_cookie({"name": "secretKey", "value": "selenium123"})
        driver.refresh()
        res = driver.find_element(By.ID, "password").text
    print(res.split()[-1])  # J4m3s-B0nd-007


def m_6_5_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/6/6.5/index.html"
        driver.get(url)
        element = driver.find_element(By.ID, "target")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        res = driver.find_element(By.ID, "secret-key").text
    print(res.split()[-1])  # S1E2L3ENIUM-S1E2C3RET


def m_6_6_1():
    with get_driver() as driver:
        url = "https://parsinger.ru/methods/1/index.html"
        driver.get(url)
        res = ""
        while not res.isdigit():
            element = driver.find_element(By.ID, "result")
            res = element.text
            driver.refresh()
    print(res)  # 4168138981270992


def m_6_6_2():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/5.5/1/1.html"
        driver.get(url)
        text_fields = driver.find_elements(By.CLASS_NAME, "text-field")

        for text_field in text_fields:
            text_field.clear()
        driver.find_element(By.ID, "checkButton").click()
        alert = driver.switch_to.alert
        res = alert.text
    print(res)  # 6540634355436603541756586467083


def m_6_6_3():
    with get_driver() as driver:
        url = "https://parsinger.ru/methods/3/index.html"
        driver.get(url)
        cookies = driver.get_cookies()
        res = 0
        for c in cookies:
            num = int(c["name"].split("_")[-1])
            if num % 2 == 0:
                res += int(c["value"])
    print(res)  # 1962101


def m_6_6_4():
    with get_driver(False) as driver:
        url = "https://parsinger.ru/selenium/5.5/2/1.html"
        driver.get(url)
        text_fields = driver.find_elements(By.CLASS_NAME, "text-field")
        for tf in text_fields:
            if tf.is_enabled():
                tf.clear()
        driver.find_element(By.ID, "checkButton").click()
        res = driver.switch_to.alert.text
    print(res)  # 534645033455443650615463625441067356407


def m_6_6_5():
    with get_driver() as driver:
        url = "https://parsinger.ru/methods/5/index.html"
        driver.get(url)
        links = driver.find_elements(By.TAG_NAME, "a")
        hrefs = [link.get_attribute("href") for link in links]
        # max_exp = 0
        # res_url = ''
        data = {}
        for url in hrefs:
            driver.get(url)
            cookie = driver.get_cookies()[0]["expiry"]
            data[url] = cookie
        res_url = max(data, key=lambda x: data[x])
        driver.get(res_url)
        res = driver.find_element(By.ID, "result").text
    print(res)  # 563244506345412334251234560541


def m_6_6_6():
    with get_driver() as driver:
        url = "http://parsinger.ru/scroll/4/index.html"
        driver.get(url)
        elements = driver.find_elements(By.CLASS_NAME, "btn")
        res = 0
        for btn in elements:
            driver.execute_script("return arguments[0].scrollIntoView(true);", btn)
            btn.click()
            num = driver.find_element(By.ID, "result")
            res += int(num.text)
    print(res)  # 4479945576993


def m_6_6_7():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.5/3/1.html"
        driver.get(url)
        elements = driver.find_elements(By.CLASS_NAME, "parent")
        res = 0
        for e in elements:
            cb = e.find_element(By.CLASS_NAME, "checkbox")
            if cb.is_selected():
                num = e.find_element(By.TAG_NAME, "textarea")
                res += int(num.get_attribute("value"))
    print(res)  # 25903


def m_6_6_8():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.5/4/1.html"
        driver.get(url)
        elements = driver.find_elements(By.CLASS_NAME, "parent")
        for e in elements:
            gray = e.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]')
            blue = e.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]')
            button = e.find_element(By.TAG_NAME, "button")
            blue.send_keys(gray.get_attribute("value"))
            gray.clear()
            button.click()
        driver.find_element(By.ID, "checkAll").click()
        res = driver.find_element(By.ID, "congrats").text
    print(res)  # FGFF-D546-DF31-34SQ-4346-93PF


def m_6_6_9():
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.5/5/1.html"
        # url = "https://parsinger.ru/selenium/5.5/5/test/test.html"
        driver.get(url)
        elements = driver.find_element(By.ID, "main-container").find_elements(
            By.XPATH, "./div"
        )
        for e in elements:
            # Коды Цветов: Получите цвет в формате HEX из каждого элемента <span>.
            color = e.find_element(By.TAG_NAME, "span").text
            # Выбор в Списке: В выпадающем списке в каждом контейнере найдите и выберите тот же HEX цвет что и у родительского контейнера.
            e.find_element(By.CSS_SELECTOR, f'option[value="{color}"]').click()
            # Кнопочная Магия: Найдите и нажмите на кнопку, у которой атрибут data-hex совпадает с HEX цветом родительского контейнера.
            e.find_element(By.CSS_SELECTOR, f'button[data-hex="{color}"]').click()
            # Чек-Бокс Челлендж: Поставьте галочку в чек-боксе на странице.
            e.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
            # Текстовое Поле: Вставьте в текстовое поле тот же HEX-цвет, который имеет фон родительского контейнера.
            e.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(color)
            # Подтверждение: Нажмите на кнопку "Проверить": если вставлен корректный HEX, то на кнопке появится "ОК".
            e.find_element(By.XPATH, ".//button[text()='Проверить']").click()
        driver.find_element(
            By.XPATH, "//button[text()='Проверить все элементы']"
        ).click()
        res = driver.switch_to.alert.text
    print(res)  # 532344023354423035345134503454510


def m_6_6_10():
    with get_driver() as driver:
        url = "https://parsinger.ru/methods/3/index.html"
        driver.get(url)
        res = 0
        cookies = driver.get_cookies()
        for c in cookies:
            if c["name"].startswith("secret_cookie_"):
                res += int(c["value"])
    print(res)  # 4901217


def m_6_6_11():
    data = [
        {"name": "KXIYO4xMrWh", "value": "ibyAZPfXAsPqptPaNyL"},
        {"name": "0OIJ4G4ZLzK", "value": "kJcPzQu5Jr8ELK"},
        {"name": "O1C4sd3RK5udnZ6P", "value": "4mYYxbfgnIvuip2ry58EQ"},
        {"name": "AUZgaLJ4Y", "value": "FLSZvYrkf1E57YMUkdD"},
        {"name": "9PWJc0VXVtnXNcS5Tf", "value": "YQ2G4RayBoXSEqEgA3oXRN3FAvAMT"},
        {"name": "pN2x6MDb", "value": "htbtD59XD3vCemHRCe9iUxV1smvXAIk5XOwuHnnmMB0"},
        {"name": "AsqpQd", "value": "uNFFRiqeRrj25MwJajG4AxeKvCxKbHUSbbvzb3C"},
        {"name": "73PVEdwTk0txDp4L", "value": "DTniz3Fwj110H24dfZfd5JqqfEtN"},
        {"name": "jZ1MwGy5z0L8ZW00U", "value": "sspfahNvfeo3zHWAIW0jdp2A9LyDbIm0"},
        {"name": "aLRosjpBhYrZ0J69a", "value": "zcoXWv5L9Pz5kwGeyP5jlAQ"},
        {
            "name": "9LPCTyKTNmvBcnZ",
            "value": "GWBjw1Gosk4IKxuh5J2eu0ikgowOaZwP8FOm1ekKeQIxJDIXBy",
        },
        {"name": "psH0h", "value": "wNAUmVlQwG6VK5TvDfryipzWeLXX46WDbXUd8yGrhrA3Hnc"},
        {"name": "BULl3P", "value": "wefA0ljyA82kYpV1OoOixtAIp6xjmiQlS9SLeN"},
        {"name": "3bIJVJCylqgshRC9r1dH", "value": "6Y6EZE5dttgx7rKzP881nAhRPE"},
        {"name": "dBDhCzi6VO0", "value": "LKMcpZ6bEJy5IY352OMViznSP5OMqS9IgZB0YMv"},
        {"name": "6SGnnuoZ7v", "value": "6asdYiIPBsMEdO0mQ9Jlq0mSMbJjfg"},
        {"name": "4dfAVZ1qZwijwYMUj", "value": "3TOxOPelSdN6cK273"},
        {
            "name": "RMOPZQILwFr3o637M",
            "value": "RZoaTFTdytqxB6sZhO4ebrhWlxjhMoQn8ZiObpdcGgH",
        },
        {
            "name": "08cQ7E3qHOOMk4uy1fLz",
            "value": "YfYkz9boRjDHLTahMuZcAJPzbjwTlRt1iNZzGl",
        },
        {
            "name": "YT1NKf55egy",
            "value": "3MSmfnklFY5TzvM8np4guMsJYtmdHmbyHiz3Vp6Rtk7r4GWhC",
        },
        {"name": "cTKnm0a3H2euL46Ibi", "value": "HCZ0KYkidXfFowGinPuWG19cT79gEJC"},
        {"name": "mvAz0P7Igjs2JY", "value": "8O67zvSDHJx"},
        {
            "name": "TzWXbWMvDBcKTo",
            "value": "dzwNYZCg4jpxKtpCeumwq0DO2KtGWLIHpQLOrzmGbXMC8G",
        },
        {
            "name": "1BMgyMHkzUemIEr",
            "value": "08Sd1v8kQi6eB1FTs9qfjDkJ9UfKCLOFGtDgbOlu9v9iiuu",
        },
        {"name": "Jig5voy", "value": "Pi4OA6hY21TeHlHyPMaMFHgY0BZRcQ9V0nXg"},
        {
            "name": "10wa7lhCoJXIzEYW5kQ",
            "value": "BFp4YeKWKVKXHTOesJLleaAelwYwPz51C95IYzd",
        },
        {"name": "BqXt5D", "value": "n99ZSFFhseCs7aVjU31pYSJxqMgFYGfreFZl9ixb2NNHRBp"},
        {
            "name": "GJunU5e1BEvfd",
            "value": "y5YFJ3hF9hG45G86MD9W9nRk61JMsh8rsmbFFrDoeJVUfyBvZ",
        },
        {"name": "itFJBn79wksvZ15lc2", "value": "nXpdqpt0Po84uOuSU"},
        {"name": "O5Q70eOB5ivJt5DZ", "value": "AZRr2ATREeF9HQR2opgF"},
        {"name": "6jBEUxI0a7x790m", "value": "comi8Mx5ig95NAiSO8"},
        {"name": "KpVF7aIkav32LuqIDI", "value": "ik4furgLieyUawgJpttvHxWoXm2zO19"},
        {"name": "OTRFyN", "value": "vlzV7Z97sWcJStZgDJiRjzIf"},
        {
            "name": "hKLzMbgdIlUTAMYSEo",
            "value": "Tq2l0QJ3ekwxY3uaC8n2ln1nDMWhltFQm2TNaBefAAzk",
        },
        {"name": "GJKNrAvRn", "value": "dByJXuSsAIz3Rnqa9BvU11okpnSydEZnkaqMQu9RoE"},
        {"name": "AowB8Q3t74JHmXTGc1", "value": "02JklRAtbsNNe"},
        {
            "name": "xPpvKmo03bGBYrmqw",
            "value": "7bf4FgaLKoj6YvGq4huLT5r9eCflo70QhI9gAPkMIuj4Bg",
        },
        {"name": "8UqFFBP3Dm0s6XM", "value": "kSZJPw6oTBwqG94q"},
        {"name": "WeeXL7bKNWIZZkgX", "value": "ap3DPbBYqlfEOZ6"},
        {"name": "fhdSevpxKUzledgGtbL4", "value": "v5I4A3PFOlN9zWPDkedlC2eLbMZ5cn3cf8"},
        {"name": "3H6lO", "value": "jxc9994fPQBKpnyr8aZBDZlMAolnxXh"},
        {"name": "QVen8QnA1648g4Dm9p", "value": "RXNYpaUTJlD4xVIOm"},
        {"name": "3PxMnD9w", "value": "JC74xNLEc5ujZge7OmXj5EWk3hwdm4OH8FgF60D6pFl"},
        {
            "name": "o8yY57CZSN",
            "value": "afO10rX663gaVttfSxeE70Gd22JKxwJAli7EhEdzkxxME",
        },
        {"name": "UpAdf46rvxXW", "value": "Ft2FEQV71gLnG"},
        {"name": "WRrpVIAkMKiZVxHt299", "value": "FC53hjqCGooNgV"},
        {"name": "XHViH149aRl5", "value": "YbozZeoGCt3gO1kRMoLExcfCotBz"},
        {"name": "yjNLzeR4k", "value": "Chd2mmuK7nxuVTi"},
        {"name": "5M4RGm", "value": "tj3HWN5mVpz9zgIie2ac2KHKIeABaou"},
        {"name": "CcxIZZYgojDZpHnO9zJl", "value": "xLiql8yXUxULBG9w2snaMLI4FjSyX"},
        {"name": "NScrEjcTmwo639PQqki", "value": "eOSFemtdjyphiPubTAzTICUhgw92By"},
        {"name": "9b5OpL5NrCpmtsE", "value": "VKdEIeX5ZNTghD6sq3qyjBHJaUuXfpQ7YnYb"},
        {"name": "uyBoiSTHTtxV8Wszttb", "value": "SHEEfVcj1jNv3V1oqeT2wfEbWKZ0uJ2ljwv"},
        {"name": "qR6AeEoEbQb1GYRj", "value": "mA66a177y8e6Nm7BlKBvpcUrM3fm6y4K"},
        {"name": "l0Y9gn8MNtC", "value": "M1L2OUmAisn1c6DNB9mJfTHRM9V3HuXUAEGG8Zx"},
        {
            "name": "L8m4GeWyECR",
            "value": "QuFfnWXebyrwwqXfVvAN2dbSisST8IgGyLggrVzTjaCeQ",
        },
        {
            "name": "GxJSMQh9aZjFdhgjaAj",
            "value": "phOonlKiMt0xLDtvoB52TbATS1Ggm4Pv5lztk5vTNkXVqp",
        },
        {"name": "GRE1eZ8D1bb", "value": "llpIP76V4S978YmQcfW"},
        {"name": "dooT1cyS41bIWEB9c", "value": "ORu004k9aFl9FdS77Iz"},
        {
            "name": "csjauyxnCpBySvkXTDzS",
            "value": "SJKqcIqWDbUJbxnHfD8jNJzYKb3Yp3TPIRDIpxCNB",
        },
        {
            "name": "Y6CgAqWN8",
            "value": "qu0g6xEm0iJeTKM8NfOZUxP0XQaCtUfiTWHtQJ5soU5cpZ",
        },
        {"name": "xxtL44KLbN60b5q", "value": "RSNFhhicL7pWpo3gvE3tJbHaIjU"},
        {
            "name": "KcvqC30",
            "value": "58IlGI646RMaGMYtL5XYqxFq8UaMwjPDNFNApAuDpUI9tMoM4t",
        },
        {
            "name": "y761v6wZDo3V7O",
            "value": "3i9iZjnZXdHlJxDz7ZrkPthYdI3PowS5yRomV0v8fR9WVco4",
        },
        {"name": "Ixr7AetyC", "value": "lYRaNZAnoNHc9UZIoXI9E"},
        {
            "name": "QIvvsr04T0JGVJE",
            "value": "tr6fE8moJI897w967QTmKojC730GdkKTUonevQbYsHQ71mi",
        },
        {"name": "CBTq9zQjJx", "value": "z7BuIeFufYeZysVnrglrDJk8KW8UBWYt62"},
        {
            "name": "2ALhFQM7svECfgsSaiTa",
            "value": "VGMsulQVoobUe4m6w8dZGej8jFzSES3hzl9OG2csqpl",
        },
        {"name": "7VQixJTzu2H", "value": "jPnLpldHTFNgPCH1RUlmRQx7N58P7CQHajLYvGxho"},
        {
            "name": "KdmUSh1SJH6M9",
            "value": "HPKIgmOBqq6Ln6QSPKedXuFpOoWhrOUzCxRMlcoJ2Gd0S7Hd",
        },
        {
            "name": "t6B9gl6QeGEDl1LW",
            "value": "kGs0hk4Pmeb83dBbuHTSzIVNcY0G4iucq73lkCMwt6Akv4w",
        },
        {
            "name": "gcjmy3",
            "value": "QtB6duKOGc7eNc9MFwiOOaikXCYQg6dO4m66sJJxkRebKIKiR",
        },
        {"name": "2oBZU9j", "value": "2U80qbFDpRElKTshedtaZ42OzYG48OQckEt2Zy9D7T"},
        {"name": "g2tyy8erqS4E5pdSynCB", "value": "VN5zSYJpNHQC14FVl"},
        {"name": "lLhLcbED3XAgAPaMp", "value": "tBUVWsfSNg0Iv4TLPAmBRm2m2nrWh"},
        {"name": "iUfgKa7OX", "value": "GtyGoiA00RNiTgqvbXs78khbzQ7d0rh5xTk1aZK"},
        {"name": "WQGGXKzZXvRXLC0", "value": "itGXA2mVtchzcqstP39BvfBvwh"},
        {"name": "p37sYwX5mgtwXJl3yFBL", "value": "h20iY8XooVE"},
        {"name": "tubsOLf", "value": "YGlaF0EEJrT1c5Z2HBAWnc1Q3an3Ob"},
        {
            "name": "mg1Pr2NJJEnw2UkGFg",
            "value": "L48wovkYz32wa16iiswcgbA6JmyVoysUqjfm4i7",
        },
        {
            "name": "V55E3ui8KHXybSDSSnoc",
            "value": "7rhA8PSMZFy1aC8CQXbitOxY0qdUkDOUWijijIvlHhtB0q1",
        },
        {"name": "AcWBQQy", "value": "zl1GXRHA3neBLCN8"},
        {"name": "PtvgV4eJ21CrPE3xeH9", "value": "1tU9KvLdq2uRNRKtA"},
        {"name": "XjuSocgLwoMvFo8a", "value": "pvmx5A97Sad0U6d6i"},
        {
            "name": "mMpdmPLcZEAZDzNyA8a2",
            "value": "WG6CrZ3zXfxN84hJXUKJq0ZroYditsADYplxwhkgXkUcZ",
        },
        {
            "name": "tojhHp0ZlGrZ8Y3",
            "value": "fqpJvGkfQRT7ytNTU5KPum150MmcVR1nja0QIQRVEOPiNvT7Pg",
        },
        {
            "name": "LDHgCR5PNoqYdffU5",
            "value": "7a0tCBgGzylPTGUStOuNXORrRWwy03Upm2CvJX",
        },
        {"name": "F4xcvPzuYYAvDrvDi", "value": "zQEpxlKpKprtwFbJyx0XYxFrlc8XP2RhRG"},
        {"name": "fmnoi", "value": "yB9333KC4bP4SHUF90Kj7OC9QXz22WAZ3xtZxLi9"},
        {
            "name": "TbGdmTkjcC52T7q",
            "value": "2HCejTOfB98e30JMj3Pz9Ok9xLz5Y9lkaJaHoRF2vA5xq0i",
        },
        {"name": "tg3vMrNIZHs", "value": "2XRV99ShR8yc0bCe0QOuC9xd0A"},
        {"name": "8FaJo5TVO7TmoOI", "value": "bGYulAOS3ARzN3Rsyx9JJzu"},
        {"name": "YLBwBAUCJ05p5fx2", "value": "Z8lGSb7AnZKVwlIqKgRIafpIfTVufj"},
        {"name": "fpZCwfH", "value": "cqo4KOj8LSagd6VUhBrq6RJtUquwK7mJaDQsQb"},
        {"name": "zjUiv081bH", "value": "LSJtgc56ylEJGMd1AhE9QcXudC8g"},
        {"name": "yiWR1RtAnWH71I1", "value": "ruskXwdCQOfbfIgtKcetVb"},
        {"name": "KMKvYURaBlIEmtyX", "value": "NFIzhI600J5QYN"},
        {"name": "hbFS4sDwQh", "value": "s4zWhushscPPDDFqT5tzPJqix0HMjjG"},
        {"name": "b9wAAVSyw4V2LQ", "value": "SDkldbPnf6NjLZSxWZV7CpCW"},
        {
            "name": "jFhFn0wPFRG",
            "value": "RYqOrD21ZN7aUeBXqISZ2afocnvvwd6hw3BXUj1wEm0mUO",
        },
    ]
    with get_driver() as driver:
        url = "https://parsinger.ru/selenium/5.6/1/index.html"
        driver.get(url)
        res = None
        res_age = 1000
        res_skills = 0
        for cookie in data:
            driver.delete_all_cookies()
            driver.add_cookie(cookie)
            driver.refresh()
            age_info = driver.find_element(By.ID, "age").text.split()
            if age_info:
                age = int(age_info[-1])
            else:
                continue
            skills = len(
                driver.find_element(By.ID, "skillsList").find_elements(
                    By.TAG_NAME, "li"
                )
            )
            if age < res_age and skills > res_skills:
                res_age, res_skills, res = age, skills, cookie["value"]
        print(res)  # ibyAZPfXAsPqptPaNyL


# m_6_1_1()
# m_6_1_2()
# m_6_3_1()
# m_6_3_2()
# m_6_3_3()
# m_6_4_1()
# m_6_5_1()
# m_6_6_1()
# m_6_6_2()
# m_6_6_3()
# m_6_6_4()
# m_6_6_5()
# m_6_6_6()
# m_6_6_7()
# m_6_6_8()
# m_6_6_9()
# m_6_6_10()
# m_6_6_11()
