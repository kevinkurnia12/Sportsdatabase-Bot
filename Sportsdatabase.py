import string
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime
import time
import csv
import unicodedata
import csv

print('import successful')

# Define variables
url = 'https://sportsdatabase.com/mlb/query'
csv_input_file = 'input.csv'
csv_output_file = 'SportsDatabase Output.csv'
input_value = []

# Main function
def main():
    with open(csv_input_file, encoding='utf8') as input_file:
        csv_reader = csv.reader(input_file, delimiter=',')

        for row in csv_reader:
            input_value.append(row[0])

    print('Num of input value in CSV: ' + str(len(input_value)))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-infobars')
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    today_date = datetime.today().strftime('%b %d, %Y')
    print('Today\'s date: ' + today_date)

    # Loop through each input
    for q in range(len(input_value)):
        cnt = 0
        driver.get(url)
        time.sleep(1)

        print('------------------')
        print('Run query: ' + str(input_value[q]))
        sdql_input = driver.find_element_by_xpath("//input[@name='sdql']")
        sdql_input.click()
        sdql_input.send_keys(input_value[q])
        sdql_button = driver.find_element_by_xpath("//input[@value='  S D Q L !  ']")
        sdql_button.click()
        time.sleep(3)
        results = driver.find_elements_by_xpath("//tr[@role='row']")

        for x in reversed(range(len(results))):
            # print(results[x].text)
            date_checker = results[x].find_elements_by_tag_name('td')[0].text
            
            if date_checker == today_date:
                cnt = cnt + 1
                date = results[x].find_elements_by_tag_name('td')[0].text
                link = results[x].find_elements_by_tag_name('td')[1].text
                day = results[x].find_elements_by_tag_name('td')[2].text
                site = results[x].find_elements_by_tag_name('td')[3].text
                team = results[x].find_elements_by_tag_name('td')[4].text
                starter = results[x].find_elements_by_tag_name('td')[5].text
                opp = results[x].find_elements_by_tag_name('td')[6].text
                starter2 = results[x].find_elements_by_tag_name('td')[7].text
                final = results[x].find_elements_by_tag_name('td')[8].text
                sum_value = results[x].find_elements_by_tag_name('td')[9].text
                win_lose = results[x].find_elements_by_tag_name('td')[10].text
                oum = results[x].find_elements_by_tag_name('td')[11].text
                o_u = results[x].find_elements_by_tag_name('td')[12].text
                hits = results[x].find_elements_by_tag_name('td')[13].text
                errors = results[x].find_elements_by_tag_name('td')[14].text
                b_l = results[x].find_elements_by_tag_name('td')[15].text
                line = results[x].find_elements_by_tag_name('td')[16].text
                total = results[x].find_elements_by_tag_name('td')[17].text
                innings = results[x].find_elements_by_tag_name('td')[18].text

                data = {
                    'Date': date,
                    'Link': link,
                    'Day': day,
                    'Site': site,
                    'Team': team,
                    'Starter': starter,
                    'Opp': opp,
                    'Starter2': starter2,
                    'Final': final,
                    'SUm': sum_value,
                    'W/L': win_lose,
                    'OUm': oum,
                    'O/U': o_u,
                    'Hits': hits,
                    'Errors': errors,
                    'BL': b_l,
                    'Line': line,
                    'Total': total,
                    'Innings': innings
                }

                time.sleep(0.5)
                writer.writerow(data)
            else:
                print('Num of results(today\'s date) - input query ' + str(q+1) + ': ' + str(cnt))
                break
            
            print('Date checked ' + date_checker)

##########################################
## START HERE

fieldnames = [
    'Date',
    'Link',
    'Day',
    'Site',
    'Team',
    'Starter',
    'Opp',
    'Starter2',
    'Final',
    'SUm',
    'W/L',
    'OUm',
    'O/U',
    'Hits',
    'Errors',
    'BL',
    'Line',
    'Total',
    'Innings'
]

with open(csv_output_file, 'w', newline = '') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    main()

########################################################
########################################################
## CREATED BY KEVIN SANTOSA

##############    #          #     #           #
      #           #          #       #       #
      #           #          #         #   #
      #           ############           #
      #           #          #         #   #
      #           #          #       #       #
      #           #          #     #           #

### HOPE TO WORK WITH YOU AGAIN IN THE FUTURE :) !!
### CONNECT WITH ME ON LINKEDIN: https://www.linkedin.com/in/kevin-kurnia-santosa-543937128/


