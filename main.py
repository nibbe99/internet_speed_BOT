from selenium import webdriver
from selenium.webdriver.common.by import By
import time


PROMISED_DOWNLOAD_SPEED = 250
class InternetSpeedBot():
    def __init__(self):
        self.up =""
        self.down =""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get("https://www.speedtest.net/sv")
        self.driver.implicitly_wait(10)
        acceptButton =  self.driver.find_element(By.XPATH,value='//*[@id="onetrust-accept-btn-handler"]')
        acceptButton.click()


        self.get_internet_speed()

    def get_internet_speed(self):
        buttonStart = self.driver.find_element(By.CLASS_NAME,value="start-text")
        buttonStart.click()
        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed")
        print("testing..... might take a while")
        time.sleep(30)  #change to higher IF needs more time


        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed")
        print("Almost done!!")
        time.sleep(20)
        print("download speed: " , self.down.text)
        print("uppload speed: ", self.up.text)

        if float(self.down.text) > PROMISED_DOWNLOAD_SPEED:
            print("Your download speed is higher than what you are paying for")
        else:
            print("Your download speed is lower than what you are paying for")

myBot = InternetSpeedBot()



