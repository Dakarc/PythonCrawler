from selenium import webdriver
import time

driver_path = r'D:\Anaconda3\me\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

# inputTag = driver.find_element_by_id('kw')
inputTag = driver.find_element_by_class_name('s_ipt')
inputTag.send_keys('python')

ssTag = driver.find_element_by_class_name('bg s_btn_wr')
ssTag.click()

time.sleep(3)

driver.close()