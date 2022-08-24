from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = Service('D:\Python\chromeDriver\chromedriver.exe')

driver = webdriver.Chrome(service=driver_path)

page_url = "http://secure-retreat-92358.herokuapp.com/"

driver.get(url=page_url)

article = driver.find_element(by="name", value="fName")
article.send_keys("Jimmy")
article = driver.find_element(by="name", value="lName")
article.send_keys("Cugan")
article = driver.find_element(by="name", value="email")
article.send_keys("hello@gmail.com")
article = driver.find_element(by="tag name", value="button")
article.click()

# driver.quit()