from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-extensions")

driver = webdriver.Firefox(options=firefox_options)
driver.get('https://avi.im/stuff/js-or-no-js.html')
p_element = driver.find_element_by_id(id_='intro-text')
print(p_element.text)