#EVENT = 'https://indico.neic.no/event/178/manage/'
EVENT_REG = 'https://indico.neic.no/event/178/manage/registration/85/registrations/'

import os
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://indico.neic.no')

# Login
driver.get('https://indico.neic.no/login/')
driver.find_element_by_name('identifier').send_keys('rkdarst')
pwd = open(os.path.expanduser('~/mnt/encrypted/coderefinery')).readlines()[2].strip()
driver.find_element_by_name('password').send_keys(pwd)
driver.find_element_by_name('password').send_keys(Keys.RETURN)


driver.get(EVENT_REG)
table = driver.find_elements_by_css_selector('table.i-table tbody tr')

# Find #209 as a test
user_map = { }
for row in table:
    #if row.text.startswith('#209'):
    #    print(row)
    id = re.match(r'#(\d+) ', row.text).group(1)
    print(id)
    user_map[int(id)] = int(row.get_attribute('id').split('-')[-1])

assert len(user_map) == len(table)


def confirm_users(users):
    driver.get(EVENT_REG)
    for user in users:
        driver.find_element_by_xpath(f'//table[contains(@class, "i-table")]//tr/td[normalize-space(.)="#{user}"]/..//input[@class="select-row"]').click()

def update_person(id_, type=None):

    driver.get(EVENT_REG + '%s/edit'%user_map[209])

    # Turn off mail
    email_status = driver.find_element_by_xpath('//input[@id="send-notification"]').get_attribute('value')
    if email_status == 'y':
        driver.find_element_by_xpath('//input[@id="send-notification"]/..').click()


    #labels = driver.find_elements_by_css_selector('label')
    label_map = {l.text: l for l in labels}

    # Set learner status
    if type:
        new_type = "Exe"
        driver.find_element_by_xpath('//label[contains(., "Type")]/../../following::td//select').send_keys(new_type)

    # Submit
    driver.find_element_by_xpath('//input[@type="submit"]').submit()

data = pd.read_excel('~/Downloads/registrations.xlsx')

#driver.quit()
