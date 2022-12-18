import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class leave_test_df(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def test_hrm05_apply_leave(self):
        #Login as pre-condition
        web = self.browser 
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(4)

        #Move to Leave
        web.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click()
        time.sleep(3)
        web.find_element(By.LINK_TEXT, "Apply").click()
        time.sleep(3)

        #Apply leave
        web.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div').click() #Choose leave type
        time.sleep(3)
        web.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys("2022-12-22") #From date
        time.sleep(3)
        web.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input").send_keys("") #To date
        time.sleep(4)
        web.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div").click() #Duration
        time.sleep(4)
        web.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div/div[1]").click() #Choose duration full day
        time.sleep(4)
        web.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div[2]/textarea').send_keys("Request leave bereavement DF") #Optional notes on Comment
        time.sleep(4)
        #Apply
        web.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/button").click()
        time.sleep(3)

        #Validation
        assert web.find_element(By.XPATH, "/html/body/div/div[2]") 

        
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()   




