import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from model import LocalStorage

EXTENSION_PATH = 'phantom.crx'
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(options=opt)
driver.switch_to.window(driver.window_handles[1])

actions = ActionChains(driver)


def click_button(by, class_name: str, index: int = 0) -> None:
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((by, class_name)))
    elem = driver.find_elements(by, class_name)
    driver.execute_script("arguments[0].scrollIntoView(true);", elem[index])
    elem[index].click()
    time.sleep(1)


def write_input(by, class_name: str, value: str, index: int = 0) -> None:
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((by, class_name)))
    elem = driver.find_elements(by, class_name)
    driver.execute_script("arguments[0].scrollIntoView(true);", elem[index])
    elem[index].send_keys(value)


def load_phantom(private_key: str) -> None:
    click_button(By.CLASS_NAME, 'dPiuzj')
    click_button(By.CLASS_NAME, 'iAHaiv', 1)
    write_input(By.CLASS_NAME, 'bffMtp', 'first')
    write_input(By.CLASS_NAME, 'fNRzXp', private_key)
    click_button(By.CLASS_NAME, 'jhviRH')
    write_input(By.CLASS_NAME, 'bffMtp', 'verystrongpassword123')
    write_input(By.CLASS_NAME, 'bffMtp', 'verystrongpassword123', 1)

    button = driver.find_element(By.CLASS_NAME, "btCro")
    driver.execute_script('arguments[0].removeAttribute("disabled");', button)
    button.click()

    click_button(By.CLASS_NAME, 'jhviRH')

    driver.switch_to.window(driver.window_handles[0])


def create_market(base_coin: str, quote_token: str) -> None:
    driver.get('https://v2.raydium.io/create-market/')
    storage = LocalStorage(driver)
    storage["USER_AGREE_DISCLAIMER"] = 'true'
    driver.refresh()

    click_button(By.XPATH, '//div[text()="Connect Wallet"]')

    click_button(By.XPATH, '//div[text()="Phantom"]')
    driver.switch_to.window(driver.window_handles[1])

    click_button(By.CLASS_NAME, 'bbORoo')

    driver.switch_to.window(driver.window_handles[0])

    click_button(By.CLASS_NAME, 'text-base', 0)

    # WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, 'input')))
    # elem1 = driver.find_elements(By.TAG_NAME, 'input')
    # elem1[3].send_keys('So11111111111111111111111111111111111111112')  # mint address for base coin
    write_input(By.TAG_NAME, 'input', base_coin, 3)

    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(4)

    # quote token:
    click_button(By.CLASS_NAME, 'text-base', 0)

    write_input(By.TAG_NAME, 'input', quote_token, 3)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(100)

    click_button(By.CLASS_NAME, 'Button', -1)
