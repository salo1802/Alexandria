from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.timeout = 30
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome('ChromeDriver\chromedriver.exe')
        self.driver.set_page_load_timeout(1000)

    def get_image_url(self):
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, '_aagv'))
            WebDriverWait(self.driver, self.timeout).until(element_present)
        except TimeoutException:
            print ("Timed out waiting for page to load")

        div = self.driver.find_element(By.CLASS_NAME, '_aagv')
        img = div.find_element(By.TAG_NAME, "img")
        src = img.get_attribute("src")
        self.driver.quit()
        return src

