import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
import platform
from time import sleep


def clearscreen():
    plt = platform.system()
    if plt == "Windows":
        os.system("cls")
    else:
        os.system("clear")


class bot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        chrome_driver_binary = "C:\\Program Files (x86)\\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver_binary, options=options)

    def login(self):
        self.driver.get('https://teams.microsoft.com/')
        sleep(2)

        loginuser = self.driver.find_element_by_id("i0116")
        loginuser.send_keys(
            "anandkumarsingh.191ec104@nitk.edu.in" + Keys.RETURN)
        sleep(2)

        loginpass = self.driver.find_element_by_id("i0118")
        loginpass.send_keys("smks2807" + Keys.RETURN)
        sleep(2)
        self.driver.find_element_by_id("idSIButton9").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]').click()


def main(teamname):
    clearscreen()
    print("Running the script for team '"+teamname+"'")
    b = bot()
    b.login()
# driver.quit()


main("DSA")
