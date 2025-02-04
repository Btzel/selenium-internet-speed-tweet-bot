import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

X_WEBSITE = "https://x.com/"
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
USERNAME = os.environ['USERNAME']
PROMISED_DOWNLOAD_SPEED = 100
PROMISED_UPLOAD_SPEED = 20
SPEED_TEST_WEBSITE = "https://www.speedtest.net/"

class InternetSpeedXBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 120)
        self.current_download_speed = 0.0
        self.current_upload_speed = 0.0


    def login(self):
        self.driver.get(X_WEBSITE)
        login_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,'a[href="/login"]')
        ))
        login_button.click()
        time.sleep(1)
        email_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,'input[name="text"]')
        ))
        email_input.send_keys(EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(1)
        #since we are using bot driven Chrome web browser
        #and x is asking us the username for it
        username_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,'input[name="text"]')
        ))
        username_input.send_keys(USERNAME)
        username_input.send_keys(Keys.ENTER)
        time.sleep(1)
        password_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,'input[name="password"]')
        ))
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_WEBSITE)
        start_speed_test = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,'span[class="start-text"]')
        ))
        start_speed_test.click()
        time.sleep(1)
        result_link = (self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,'div[data-result-id="true"] a')
        )).get_attribute("href"))
        self.driver.get(result_link)
        time.sleep(3)
        self.current_download_speed = float(self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,'div[title="Receiving Time"] span[class*="result-data-value"]')
        )).text)
        self.current_upload_speed = float(self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,'div[title="Sending Time"] span[class*="result-data-value"]')
        )).text)


    def tweet_about_internet_speed(self):
        if self.current_upload_speed < PROMISED_UPLOAD_SPEED or self.current_download_speed < PROMISED_DOWNLOAD_SPEED:

            tweet_textarea = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]')
            ))
            tweet_text = (f"Hey internet provider, why is my internet speed"
                          f" {self.current_download_speed} Mbps/{PROMISED_DOWNLOAD_SPEED} Mbps Download and"
                          f" {self.current_upload_speed} Mbps/{PROMISED_UPLOAD_SPEED} Mbps Upload"
                          f" when i pay for {PROMISED_DOWNLOAD_SPEED} Mbps Download and {PROMISED_UPLOAD_SPEED} Mbps Upload?")
            tweet_textarea.send_keys(tweet_text)
            tweet_button = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"]')
            ))
            time.sleep(2)
            tweet_button.click()
        else:
            tweet_textarea = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]')
            ))
            tweet_text = (f"Hey internet provider, thank you for providing my promised internet speed as"
                          f" {self.current_download_speed} Mbps/{PROMISED_DOWNLOAD_SPEED} Mbps Download and"
                          f" {self.current_upload_speed} Mbps/{PROMISED_UPLOAD_SPEED} Mbps Upload.")
            tweet_textarea.send_keys(tweet_text)
            tweet_button = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"]')
            ))
            time.sleep(2)
            tweet_button.click()






