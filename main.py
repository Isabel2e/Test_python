from selenium import webdriver
from credentials import USERNAME, PASSWORD
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import time

class Scraper(webdriver.Chrome):

    def __init__(self, driver_path ='C:\129chromedriver.exe', teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Scraper, self).__init__()


    def open_odoo(self):
 
        self.get("https://www.odoo.sh/")
        time.sleep(1)
    
    def login (self, USERNAME, PASSWORD):
        sign_inlabel = self.find_element(By.XPATH,"//*[@id='top_menu']/form/a")
        sign_inlabel.click()
        time.sleep(1)
        
        username = self.find_element(By.XPATH,"//*[@id='login_field']")
        username.send_keys(USERNAME)
        time.sleep(1)

        password = self.find_element(By.XPATH,"//*[@id='password']")
        password.send_keys(PASSWORD)
        time.sleep(1)

        sign_in_button = self.find_element(By.XPATH, "//*[@id='login']/div[3]/form/div/input[13]")
        sign_in_button.click()
        time.sleep(1)

        #authorized = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/main/div/div[2]/div[1]/div[2]/div[1]/form/div/button[2]")
        #authorized.click()
        #time.sleep(3)
    def open(self):
    
        open = self.find_element(By.XPATH,"//*[@id='wrapwrap']/main/div[2]/div[2]/div[2]/div/div[2]/div[4]/a")
        open.click()
        time.sleep(5)

def main():
    with Scraper() as bot:
        bot.open_odoo()  # Abrir Odoo
        bot.login(USERNAME, PASSWORD)  # Iniciar sesión
        bot.open()  # Abrir la página que contiene el registro de backups
    

if __name__ == '__main__':
    main()