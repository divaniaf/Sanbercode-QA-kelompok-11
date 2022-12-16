import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class testday17(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    #Muncul error bisa jadi karna:
    # 1. Koneksi 2. Web/server ada problem 3. Data (hiring manager,dll) ada yang dihapus
    # Solusi biasanya nunggu server web di "refresh??", baru code di run algi

    def test_HRM_6_Recruitment_1(self):
        #Add/Update Vacancy

        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)

        #Recruitment
        web.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[5]/a[1]/span[1]").click()
        time.sleep(3)
        #Vacancies
        web.find_element(By.LINK_TEXT,"Vacancies").click()
        time.sleep(2)
        #Add
        web.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
        time.sleep(2)
        
        #Vacancy_Name
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input").send_keys("About Testing")
        time.sleep(3)
        #Job_Title
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[1]/div[2]/div//div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").click()
        time.sleep(3)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/span").click()
        time.sleep(2)
        #Hiring_Manager
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[3]/div[1]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("Odis")
        time.sleep(4)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div").click()
        time.sleep(2)
        #Save
        web.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)
        web.find_element(By.LINK_TEXT,"Vacancies").click()
        time.sleep(4)

        #Validasi
        assert web.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div')
    
    def test_HRM_6_Recruitment_2(self):
        #Add Candidate

        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[5]/a[1]/span[1]").click()
        time.sleep(3)

        #Add
        web.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]/i[1]").click()
        time.sleep(3)

        #First_name
        web.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Mr.")

        #Middle_name
        web.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("World")
        
        #Last_name
        web.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Wide")

        #Vacancy
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div[1]").click()
        time.sleep(2)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[2]").click()
        #Email
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input").send_keys("mrwide@gmail.com")
        #Consent
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[7]/div/div/div/div[2]/div/label/span/i").click()
        #Save
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(4)

        #Validasi
        assert web.find_element(By.XPATH,"//*[@id='oxd-toaster_1']")

    def test_HRM_6_Recruitment_3(self):
        #Search Candidate

        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(4)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.LINK_TEXT,"Recruitment").click()
        time.sleep(3)
        
        #Search_Candidate
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[1]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("Mr.")
        time.sleep(4)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div").click()
        #Search_Button
        web.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[4]/button[2]").click()
        time.sleep(3)

        #Validasi
        assert web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div")
    
    
    
    def test_HRM_6_Recruitment_4(self):
        #Delete Candidate
        
        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.LINK_TEXT,"Recruitment").click()
        time.sleep(3)
        
        #Search_Candidate
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[1]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("Mr.")
        time.sleep(4)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div").click()
        #Search_Button
        web.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[4]/button[2]").click()
        time.sleep(3)

        #Delete_Candidate
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[7]/div/button[2]/i").click()
        time.sleep(3)
        web.find_element(By.XPATH,"//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]").click()
        time.sleep(3)

        #Validation
        assert web.find_element(By.XPATH,"//*[@id='oxd-toaster_1']")


    def test_HRM_6_Recruitment_5(self):
        #Search About Testing

        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        time.sleep(3)
        web.find_element(By.LINK_TEXT,"Vacancies").click()
        time.sleep(3)

        #Search_Vacan
        web.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click()
        #Search_Button
        web.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[2]").click()
        time.sleep(3)

        #Validasi
        assert web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[2]/div[.='About Testing']")
    
    def test_HRM_6_Recruitment_6(self):
        #Delete About Testing

        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.LINK_TEXT,"Recruitment").click()
        time.sleep(3)
        web.find_element(By.LINK_TEXT,"Vacancies").click()
        time.sleep(3)

        #Search_Vacan
        web.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click()
        #Search_Button
        web.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[2]").click()
        time.sleep(3)

        #Delete_About_Testing
        web.find_element(By.XPATH,"//div[@role='table']//div[1]//div[1]//div[6]//div[1]//button[1]//i[1]").click()
        time.sleep(3)
        web.find_element(By.XPATH,"//button[normalize-space()='Yes, Delete']").click()
        time.sleep(3)

        #Validation
        assert web.find_element(By.XPATH,"//*[@id='oxd-toaster_1']")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
