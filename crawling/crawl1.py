from selenium import webdriver

path = "D:\web-crawling\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get('https://www.youtube.com')