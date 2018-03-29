# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 09:54:06 2018

@author: yni

Scraping Type, Title, Due
"""
import selenium.webdriver as webdriver
from pandas import DataFrame
import os

def login(email,password):
    #Set browser to be Chrome, please change it to your own file directory
    chromedriver_path = os.path.dirname(__file__) + "/chromedriver.exe"
    browser = webdriver.Chrome(chromedriver_path)
    browser.get('http://ems.itu.edu/users/sign_in')
    inputbox1 = browser.find_element_by_id('user_email')
    inputbox1.send_keys(email)
    inputbox2 = browser.find_element_by_id('user_password')
    inputbox2.send_keys(password)
    loginbutton = browser.find_element_by_name('commit')
    loginbutton.click()
    data = []
    #Go to SWE500 Quiz page
    browser.get('https://ems.itu.edu/student/sections/5661/quizzes')
    tables = browser.find_elements_by_xpath("//table[@class='table table-bordered table-hover']")
    table = tables[0]
    for tr in table.find_elements_by_tag_name('tr'):
        tds = tr.find_elements_by_tag_name('td')
        tds = tds[0:3]
        if tds:
            data.append([td.text for td in tds])
    df = DataFrame.from_records(data, columns = ['Title','Points','Due'])  
    browser.close()
    browser.quit()
    return df

def write_to_file(data_frame, path=None):
    if path is None:
        path = os.path.dirname(__file__)
    data_frame.to_json(path_or_buf='{}/data.json'.format(path), orient='index')

if __name__ == "__main__":
    # Type in email, password
    # print __file__
    result = login('','')
    print result
    write_to_file(result)
