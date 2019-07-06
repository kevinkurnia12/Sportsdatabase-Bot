import string
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import time
import csv
import unicodedata
import csv

print('import successful')

url = 'https://sportsdatabase.com/mlb/query'
csv_input_file = 'input.csv'
csv_output_file = 'Sportsdatabase_Output.csv'
input_value = []

with open(csv_input_file, encoding='utf8') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')

    for row in csv_reader:
        input_value.append(row[0])

print('Num of input value in CSV: ' + str(len(input_value)))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-infobars')
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)


driver.get(url)

sdql_input = driver.find_element_by_xpath("//input[@name='sdql']")
sdql_input.click()
sdql_input.send_keys(input_value[0])
sdql_button = driver.find_element_by_xpath("//input[@value='  S D Q L !  ']")
sdql_button.click()

results = driver.find_elements_by_xpath("//tr[@role='row']")
print('Num of results: ' + str(len(results)))

for x in reversed(range(len(results))):
    print(results[x].text)








