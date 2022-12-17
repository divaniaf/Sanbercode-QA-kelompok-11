import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class test_Performance_Aufar(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
    #Muncul error bisa jadi karna:
    # 1. Koneksi 2. Web/server ada problem 3. Data (hiring manager,dll) ada yang dihapus
    # Solusi biasanya nunggu server web di "refresh??", baru code di run lagi

    def test_HRM_10_Performance_1(self):
        #Add Performance Indicator

        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)

        #Performance
        web.find_element(By.XPATH,"//span[normalize-space()='Performance']").click()
        time.sleep(2)

        #Configure
        web.find_element(By.XPATH,"//span[normalize-space()='Configure']").click()

        #KPIs(Key_performance)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a").click()
        time.sleep(3)
        
        #Tambah_indikator_job_performance
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/button[@type='button']").click()
        time.sleep(2)

        #Key_Performance_Indicator
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[1]/div/div[1]/div//input").send_keys("About Testing")
        #Job_title(Support Specialist)
        web.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[24]").click()
        #Minimum_Rating
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div//input").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div//input").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div//input").send_keys("10")
        #Maximum_Rating
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[2]/div//input").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[2]/div//input").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[2]/div//input").send_keys("50")
        #Make_Default(Radio Button)
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[2]/div/div[3]//div[@class='oxd-switch-wrapper']//span").click()
        time.sleep(3)
        #Save
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()

        #Validasi
        assert web.find_element(By.XPATH,"//*[@id='oxd-toaster_1']")
    
    def test_HRM_10_Performance_2(self):
        #Search Performance Indicator
        
        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.XPATH,"//span[normalize-space()='Performance']").click()
        time.sleep(2)
        web.find_element(By.XPATH,"//span[normalize-space()='Configure']").click()
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a").click()
        time.sleep(3)

        #Search
        web.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[24]").click()
        time.sleep(2)
        web.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)

        #Validasi
        assert web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]")

    def test_HRM_10_Performance_3(self):
        #Edit Performance Indicator
        
        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.XPATH,"//span[normalize-space()='Performance']").click()
        time.sleep(2)
        web.find_element(By.XPATH,"//span[normalize-space()='Configure']").click()
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a").click()
        time.sleep(3)

        #Search
        web.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[24]").click()
        time.sleep(2)
        web.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)

        #Edit
        web.find_element(By.XPATH,"//i[@class='oxd-icon bi-pencil-fill']").click()
        time.sleep(2)
       
        #Minimum_Rating
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div//input").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div//input").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div//input").send_keys("70")
        #Maximum_Rating
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[2]/div//input").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[2]/div//input").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[2]/div//input").send_keys("100")
        #Submit
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(2)

        #Validasi
        assert web.find_element(By.XPATH,"//*[@id='oxd-toaster_1']")

    def test_HRM_10_Performance_4(self):
        #Delete Performance Indicator

        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.XPATH,"//span[normalize-space()='Performance']").click()
        time.sleep(2)
        web.find_element(By.XPATH,"//span[normalize-space()='Configure']").click()
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a").click()
        time.sleep(3)

        #Search
        web.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[24]").click()
        time.sleep(2)
        web.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(4)

        #Delete_Performance_Indicator
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[7]/div/button[2]/i").click()
        time.sleep(2)
        web.find_element(By.XPATH,"//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]").click()
        time.sleep(2)

        #Validasi
        assert web.find_element(By.XPATH,"//*[@id='oxd-toaster_1']")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
