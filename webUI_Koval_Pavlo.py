from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
from behave import *

class functions_selenium:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

    def click_button(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def enter_info(self, xpath, text):
        self.driver.find_element(By.XPATH, xpath).send_keys(text)


    def enter(self):
        #Log in
        self.enter_info('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input', 'Admin')
        self.enter_info('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input', 'admin123')
        self.click_button('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input')

    def add_new_record(self):
        #opening the Job-Work Shifts
        self.click_button('/html/body/div[1]/div[2]/ul/li[1]/a')
        self.click_button('/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a')
        self.click_button('/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[5]/a')
        #add workShits
        self.click_button('/html/body/div[1]/div[3]/div[2]/div/div[2]/form/div[1]/input[1]')
        self.enter_info('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/input', 'RandomName')
        self.click_button('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select[1]/option[26]')
        self.click_button('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select[2]/option[74]')
        self.click_button('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/table/tbody/tr[2]/td[1]/select/option[1]')
        self.click_button('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/table/tbody/tr[2]/td[2]/a[1]')
        self.click_button('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/p/input[1]')

    def check(self, changes):
        page = self.driver.find_element(By.XPATH, changes)
        assert page != None

def main():
    test = functions_selenium()
    test.enter()
    test.add_new_record()

    check_record = "//*[contains(text(), 'RandomName')]"
    test.check(check_record)

if __name__=='__main__':
    main()

