from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from dotenv import load_dotenv
import os
load_dotenv()

INSTAGRAM_USERNAME = os.getenv("instagram_username")
INSTAGRAM_PASSWORD = os.getenv("instagram_password")
FANPAGE_NAME = os.getenv("fanpage_name")
DRIVER_LOCATION = os.getenv("driver_location")

INSTAGRAM_URL = "https://www.instagram.com/"


class InstaFollower:

    def __init__(self):
        chrome_driver_path = os.getenv("driver_location")
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/button[1]').click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(INSTAGRAM_USERNAME)
        self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(INSTAGRAM_PASSWORD)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(5)

    def find_followers(self, fanpage_name):
        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(fanpage_name)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()
        time.sleep(3)
        followers_body = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[2]')
        for scroll in range(0, 1):
            self.follow()
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', followers_body)
            time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button/div/svg")
        time.sleep(3)

    def follow(self):
        follower_buttons = self.driver.find_elements(by=By.CLASS_NAME, value="y3zKF")
        for button in follower_buttons:
            try:
                button.click()
                time.sleep(2)
            except NoSuchElementException:
                break
            except ElementClickInterceptedException:
                break

