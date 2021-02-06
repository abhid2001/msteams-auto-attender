import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import os
import platform
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


def clearscreen():
    plt = platform.system()
    if plt == "Windows":
        os.system("cls")
    else:
        os.system("clear")


class bot:
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        # chrome_driver_binary = "C:\\Program Files (x86)\\chromedriver.exe"
        # self.driver = webdriver.Chrome(chrome_driver_binary, options=options)
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://teams.microsoft.com/')
        sleep(2)

        loginuser = self.driver.find_element_by_id("i0116")
        loginuser.send_keys(
            "shipramathur.191it147@nitk.edu.in" + Keys.RETURN)
        sleep(2)

        loginpass = self.driver.find_element_by_id("i0118")
        loginpass.send_keys("surya@333" + Keys.RETURN)
        sleep(2)
        self.driver.find_element_by_id("idSIButton9").click()
        sleep(2)
        # self.driver.find_element_by_xpath(
        #     '/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]').click()

    def checkchannel(self):
        sleep(15)
        self.driver.get(
            'https://teams.microsoft.com/_#/school/conversations/General?threadId=19:2b925891dfca4837b4fb9a45498b2b4a@thread.tacv2&ctx=channel')
        sleep(5)
        count_of_channels = len(
            self.driver.find_elements_by_css_selector("div.name-channel-type"))
        self.driver.find_element_by_css_selector('a.channel-anchor').click()

    def waitformeeting(self):
        while True:
            try:
                joinbtn = self.driver.find_element_by_xpath(
                    '//*[@title="Join call with video"]')
                joinbtn.click()
                print("Meeting is available, joining now...")
                sleep(5)
                break
            except:
                sleep(60)
                print("Waiting for meeting to start...")

    def showparticipants(self):
        while True:
            try:
                participantsbtn = self.driver.find_element_by_xpath(
                    '//*[@id="roster-button"]')
                participantsbtn.click()
            except:
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.TAB)
                actions.perform()
            else:
                break

    def checkparticipants(self):

        self.showparticipants()
        sleep(2)
        nbr = 0
        inmeeting = self.driver.find_element_by_xpath(
            '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[1]/button')
        if "Currently in this meeting" in inmeeting.get_attribute('aria-label'):
            nbr = nbr + \
                int(inmeeting.get_attribute(
                    'aria-label').split("Currently in this meeting ")[1])
            return nbr
        else:
            nbr = nbr + \
                int(inmeeting.get_attribute(
                    'aria-label').split("Attendees ")[1])
            presenters = self.driver.find_element_by_xpath(
                '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[1]/div/calling-roster-section/div/div[1]/button')
            nbr = nbr + \
                int(presenters.get_attribute(
                    'aria-label').split("Presenters ")[1])
            return nbr

    def joinmeeting(self):
        while True:
            try:
                mic = self.driver.find_element_by_xpath(
                    '//*[@id="preJoinAudioButton"]/div/button/span[1]')
                if 'Mute microphone' in mic.get_attribute('outerHTML'):
                    mic.click()
                    print("I muted your microphone")

                cam = self.driver.find_element_by_xpath(
                    '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
                if 'Turn camera off' in cam.get_attribute('outerHTML'):
                    cam.click()
                    print("I turned off your Camera")

                sleep(2)
                # joinbtn2
                self.driver.find_element_by_xpath(
                    '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button').click()
                break
            except:
                print('Team Still Loading...')
                sleep(2)
        students = self.checkparticipants()
        print("Joined meeting,number of participants: "+str(students))
        sleep(5)

    def endcall(self):
        while True:
            try:
                                
                print("Leaving the meet now!")
                end = self.driver.find_element_by_xpath('//*[@id="hangup-button"]')                
                print(end)
                end.click()
                print("Meet ended")
            except:
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.TAB)
                actions.perform()
            else:
                break
            


def main(teamname):
    clearscreen()
    print("Running the script for team '"+teamname+"'")
    b = bot()
    b.login()
    b.checkchannel()
    b.waitformeeting()
    b.joinmeeting()
    b.endcall()


main("test")
