#!/usr/bin/env python
# -*- coding: utf-8 -*-

# I use this scraper to get the CONV_DICT

from selenium import webdriver


driver_path = '/usr/local/bin/chromedriver'
base_url = 'http://www.i18nqa.com/debug/utf8-debug.html'

expected = []
actual = []

driver = webdriver.Chrome(executable_path = driver_path)
driver.get(base_url)

xpath = '//table[@id="dbg"]//td[@class="ch"][1]'
expected.extend([e.text for e in driver.find_elements_by_xpath(xpath)])

xpath = '//table[@id="dbg"]//td[@class="ch"][2]'
actual.extend([e.text for e in driver.find_elements_by_xpath(xpath)])

xpath = '//table[@id="dbg"]//td[@class="ch"][3]'
expected.extend([e.text for e in driver.find_elements_by_xpath(xpath)])

xpath = '//table[@id="dbg"]//td[@class="ch"][4]'
actual.extend([e.text for e in driver.find_elements_by_xpath(xpath)])

conv_list = sorted(filter(lambda x: len(x[0]) > 0 and len(x[1]) > 0
    and actual.count(x[0]) == 1, zip(actual, expected)),
    key=lambda x: len(x[0]), reverse=True)
conv_pattern = '|'.join([x[0] for x in conv_list])

print('{')
for x in conv_list:
    print('\'{}\'\t: \'{}\','.format(x[0], x[1]))
print('}')
print('\'{}\''.format(conv_pattern))

driver.quit()
