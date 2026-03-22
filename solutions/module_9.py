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


# m_9_1_1()
# m_9_2_1()
