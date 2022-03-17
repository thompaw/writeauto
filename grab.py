from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-extensions")
driver = webdriver.Firefox(executable_path = "./geckodriver.exe", options=firefox_options)

def fetch_page(url): 
    driver.get(url)
    maindiv = driver.find_element_by_class_name('content-wrapper da-scroll-area card-drop-shadow')
    return(maindiv)

# test code below
print(fetch_page('https://hackerone.com/reports/1309435'))
# resource: https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72 