from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ops = Options()
ops.headless = True  # make it headless to avoid clutter

driver_path = '/geckodriver.exe'  # path to driver's executable
ffdriver = webdriver.Firefox(executable_path=driver_path, option=ops)  # initialize firefox driver with the prior exe, use established options

# clean up to exit driver after content is retrieved
ffdriver.quit()
