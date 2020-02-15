from selenium   import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://117.78.21.190/web-visitor-center-vue/#/blackList/index")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[1]/form/button[2]/span').click()


