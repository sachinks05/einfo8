from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from time import sleep
driver=Chrome(r"C:\Users\SACHIN\Desktop\training\chromedriver.exe")
#url="https://www.flipkart.com/offers-store"
url="file:///C:/Users/SACHIN/Desktop/demo.html"
driver.get(url)
box=driver.find_element_by_id("standard_cars")
list=Select(box)
x=list.options
for i in x[-1:]:
    list.select_by_visible_text(i.text)
    sleep(1)

driver = webdriver
driver.123
a ="sachin"
b= "sachinks"
c = "sachinsachu"
