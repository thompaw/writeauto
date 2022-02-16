from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://avi.im/stuff/js-or-no-js.html')
p_element = driver.find_element(id_='intro-text')
print(p_element.text)