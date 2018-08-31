from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

try:
    driver.get('https://www.naver.com/')

    elem = driver.find_element_by_id('query')
    elem.clear()
    elem.send_keys('Serch')
    elem.send_keys(Keys.RETURN)
    
    hotclick = driver.find_element_by_class_name('same_people')
    hotclick_list = hotclick.find_elements_by_tag_name('li')
    ex = Workbook()
    es = ex.active

    for item in hotclick_list:
        item_list = item.find_element_by_class_name('same_list2_content list4 over')
        print(item_list.text)
        es.append([item_list.text])
    ex.save('Test.xlsx')

except Exception as e:
    print(e)

finally:
    driver.close()
