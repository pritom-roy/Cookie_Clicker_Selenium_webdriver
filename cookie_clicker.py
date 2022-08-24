from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver_path = Service('D:\Python\chromeDriver\chromedriver.exe')

driver = webdriver.Chrome(service=driver_path)

page_url = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(url=page_url)

cookie_click = driver.find_element(by="xpath", value='//*[@id="cookie"]')
play = True
play_time = time.time() + 60
buy_time = time.time() + 5

while play:

    if time.time() > buy_time:

        upgrade = driver.find_elements(by="css selector", value='#store div')
        upgrade_item_list = []
        for up in upgrade:
            if up.get_attribute("class") != "grayed":
                upgrade_item_list.append(up)

        upgrade_item_list.reverse()
        upgrade_item_list[0].click()
        buy_time = time.time() + 5

    else:
        cookie_click.click()

    if time.time() > play_time:
        break
