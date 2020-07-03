from selenium import webdriver
import chromedriver_binary
import csv

driver = webdriver.Chrome()

def main():
    with open('form.csv','r',encoding="utf-8_sig") as f:
        reader = csv.reader(f)

        for index, row in enumerate(reader):
            driver.get('http://example.selenium.jp/reserveApp/')
            print('continue') if index == 0 else _inputForm(row)

def _inputForm(row):

    driver.find_element_by_id("reserve_year").clear()
    driver.find_element_by_id("reserve_year").send_keys(row[0])
    driver.find_element_by_id("reserve_month").clear()
    driver.find_element_by_id("reserve_month").send_keys(row[1])
    driver.find_element_by_id("reserve_day").clear()
    driver.find_element_by_id("reserve_day").send_keys(row[2])
    driver.find_element_by_id("reserve_term").clear()
    driver.find_element_by_id("reserve_term").send_keys(row[3])
    driver.find_element_by_id("headcount").clear()
    driver.find_element_by_id("headcount").send_keys(row[4])
    driver.find_element_by_id("guestname").send_keys(row[7])

    if row[5] == 'あり':
        driver.find_element_by_id("breakfast_on").click()
    else:
        driver.find_element_by_id("breakfast_off").click()

    if row[6] == 'A':
        driver.find_element_by_id("plan_a").click()
    else:
        driver.find_element_by_id("plan_b").click()

    driver.find_element_by_id("goto_next").click()
    driver.find_element_by_id("commit").click()
    
main()
