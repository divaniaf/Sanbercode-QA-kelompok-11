
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class time_test_df(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_hrm07_punch_in(self):
        #Login as pre-condition
        web = self.browser 
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(4)

        #Move to Time
        web.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click()
        time.sleep(3)
        web.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
        time.sleep(4)
        web.find_element(By.XPATH, "//a[normalize-space()='Punch In/Out']").click() #Move to Punch In/Out
        time.sleep(3)

        #Punch In
        #Skip input date and time (auto fill in real time)
        web.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/form/div[2]/div/div/div/div[2]/textarea').send_keys("DF check in outside area") #input notes (optional)
        time.sleep(4)
        web.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/form/div[3]/button').click() #Submit Punch In
        time.sleep(3)

    def test_hrm08_punch_out(self):
        #Punch Out
        #Login and Punch In as pre-condition
        web = self.browser 
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(4)

        #Move to Time
        web.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click()
        time.sleep(3)
        web.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
        time.sleep(4)
        web.find_element(By.XPATH, "//a[normalize-space()='Punch In/Out']").click() #Move to Punch In/Out
        time.sleep(3)

        #Punch Out
        #Skip input date and time (auto fill in real time)
        web.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/form/div[2]/div/div/div/div[2]/textarea').send_keys("DF check out outside area") #input notes (optional)
        time.sleep(4)
        web.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/form/div[3]/button').click() #Submit Punch Out
        time.sleep(10)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()   

