import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_driver ():
    test_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    test_driver.get('https://www.amazon.com/')
    test_driver.maximize_window()
    time.sleep(3)
    test_driver.find_element_by_name('field-keywords').send_keys('iphone')
    test_driver.find_element_by_id('nav-search-submit-button').click()
    print(test_driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/span').text)

print("OK")
time.sleep(2)
