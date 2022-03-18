from src.grab import webDriver
import os

def get_data():
    site_list = '/site_files/infile.txt'
    path = os.getcwd() + site_list
    
    driver = webDriver()  # init driver

    site_list = driver.get_sites(path)
    
    for site in site_list:
        print(site)
        site_data = driver.get_data(site)
        print(site_data)



if __name__ == "__main__":
    get_data()

