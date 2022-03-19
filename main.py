from src.handler import fileToData
from src.grabber import webDriver
import os


def get_data():
    site_list = '/site_files/infile.txt'
    path = os.getcwd() + site_list  # join the current working directory with the path to the infile
    handler = fileToData(path)
    grabber = webDriver()


if __name__ == "__main__":
    get_data()

