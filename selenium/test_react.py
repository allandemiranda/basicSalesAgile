# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestReact():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(3)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    # Test name: login
    # Step # | name | target | value
    # 1 | open | https://localhost:3000/auth/login/ | 
    self.driver.get("https://localhost:3000/auth/login/")
    # 2 | click | name=user_name | 
    self.driver.find_element(By.NAME, "user_name").click()
    # 3 | type | name=user_name | allan_miranda
    self.driver.find_element(By.NAME, "user_name").send_keys("allan_miranda")
    # 4 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 5 | type | name=password | 123456
    self.driver.find_element(By.NAME, "password").send_keys("123456")
    # 6 | click | css=.MuiButton-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-label").click()
    # 7 | click | css=.makeStyles-logoutButton-35 > .MuiButton-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".makeStyles-logoutButton-35 > .MuiButton-label").click()
  
  def test_clickTop1(self):
    # Test name: clickTop1
    # Step # | name | target | value
    # 1 | open | https://localhost:3000/auth/login/ | 
    self.driver.get("https://localhost:3000/auth/login/")
    # 2 | click | name=user_name | 
    self.driver.find_element(By.NAME, "user_name").click()
    # 3 | type | name=user_name | allan_miranda
    self.driver.find_element(By.NAME, "user_name").send_keys("allan_miranda")
    # 4 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 5 | mouseOver | css=.MuiButton-label | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 6 | type | name=password | 123456
    self.driver.find_element(By.NAME, "password").send_keys("123456")
    # 7 | click | css=.MuiButton-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-label").click()
    # 8 | click | css=.MuiTableRow-root:nth-child(1) .makeStyles-details-61 | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(1) .makeStyles-details-61").click()
    # 9 | click | css=.makeStyles-logoutButton-35 > .MuiButton-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".makeStyles-logoutButton-35 > .MuiButton-label").click()
  
  def test_listUsersAndClick(self):
    # Test name: listUsersAndClick
    # Step # | name | target | value
    # 1 | open | https://localhost:3000/auth/login/ | 
    self.driver.get("https://localhost:3000/auth/login/")
    # 2 | click | name=user_name | 
    self.driver.find_element(By.NAME, "user_name").click()
    # 3 | type | name=user_name | allan_miranda
    self.driver.find_element(By.NAME, "user_name").send_keys("allan_miranda")
    # 4 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 5 | mouseOver | css=.MuiButton-label | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 6 | type | name=password | 123456
    self.driver.find_element(By.NAME, "password").send_keys("123456")
    # 7 | click | css=.MuiButton-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-label").click()
    # 8 | click | css=.MuiListItem-root:nth-child(2) .MuiButton-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiListItem-root:nth-child(2) .MuiButton-label").click()
    # 9 | click | css=.MuiTableRow-root:nth-child(1) .makeStyles-subscriptions-84 | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(1) .makeStyles-subscriptions-84").click()
    # 10 | click | css=.makeStyles-logoutButton-35 > .MuiButton-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".makeStyles-logoutButton-35 > .MuiButton-label").click()
  
  
