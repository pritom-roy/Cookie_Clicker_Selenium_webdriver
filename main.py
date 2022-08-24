from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = Service('D:\Python\chromeDriver\chromedriver.exe')

driver = webdriver.Chrome(service=url)

product_url = "https://www.python.org/"

driver.get(url=product_url)

price = driver.find_elements(by="class name", value='event-widget time')
event = driver.find_elements(by="class name", value='event-widget li a')

# date = driver.find_element(by="xpath", value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time/text()')

for day in price:
    print(day.text)
# print(event)
for ev in event:
    print(ev.text)

d = {}
for n in range (len(event)):
    d[n] = {
        "time" : price[n].text,
        "event": event[n].text
    }

print(d)

driver.quit()
