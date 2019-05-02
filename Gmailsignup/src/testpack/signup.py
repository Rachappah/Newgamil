'''
Created on 30-Apr-2019

@author: racha
'''
from selenium import webdriver
import time
from lib2to3.tests.support import driver

driver=webdriver.Firefox()
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='firstName']").send_keys("rachappa")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='lastName']").send_keys("halinge")
time.sleep(5)
driver.find_element_by_xpath("//input[@id='username']").send_keys("rachappa22")
time.sleep(5)
driver.find_element_by_xpath("//input[@name='Passwd']").send_keys("rachu2222")
time.sleep(5)
driver.find_element_by_xpath("//input[@name='ConfirmPasswd']").send_keys("rachu2222")
time.sleep(5)
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='phoneNumberId']").send_keys(7353249488)
time.sleep(5)
driver.find_element_by_xpath("//div[@class='IMH1vc lUHSR Hj2jlf']").click()
time.sleep(3)
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@name='Passwd']").send_keys("rachu2222")
time.sleep(5)
driver.find_element_by_xpath("//input[@name='ConfirmPasswd']").send_keys("rachu2222")
time.sleep(3)
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(5)
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
driver.find_element_by_xpath("//*[@id='phoneNumberId']").send_keys(7353249488)
time.sleep(3)
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
#time.sleep(2)
#driver.find_element_by_xpath("//*[@id='code']").send_keys(923079)
#driver.find_element_by_xpath("//input[@class='RveJvd snByac']").click()
