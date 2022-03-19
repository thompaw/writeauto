from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


ops = Options()
ops.add_argument("--window-size=1920,1080")  # set window size to native GUI size
ops.add_argument("start-maximized") # start maximized
ops.add_argument("--headless") # make a headless browser


class webDriver:
    def __init__(self):
        self.options = ops
        # use the webdriver manager to auto-install and implement the necessary web driver
        self.service = Service(executable_path=ChromeDriverManager().install()) 
        # initialize a new webdriver using the previous driver, and the prior options
        self.driver = webdriver.Chrome(service=self.service, options=ops)

    def get_data(self, link):  # function to get raw data
        # function needs to: 
        # 1. recognize which sites are used, in order to determine what kind of scraping should be used
        site_name = link[link.index("//") + 2:link.index(".com")]
        # 2. get raw data from each site and return it in a pretty manner
        if site_name == "hackerone":
            data = self.from_hackerone(link)
        else:
            data = self.driver.get(url=link)
        return data

    def from_hackerone(self, link):
        pass

    def end(self):
        # clean up code, will exit the driver when done
        self.driver.quit()
