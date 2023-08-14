import time
# import random
from datetime import datetime, timedelta
# import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

# Generate a random date and time
    # start_date = datetime.now()
    # end_date = start_date + timedelta(days=365)  # Set the maximum range to 1 year from now
    # random_datetime = start_date + (end_date - start_date) * random.random()

#BROWSER selection
driver = webdriver.Chrome(
    executable_path='E:\Software testing\Automation project\PycharmProjects\OdooCCL\drivers\chromedriver')
    
# from login page url
driver.get("http://10.10.14.196:9091/web/login")
time.sleep(2)

# User-name-and-password-input-field
driver.find_element_by_id("login").send_keys("Test_data_migration")
driver.find_element_by_id("password").send_keys("@testdata1234")
submit = driver.find_element_by_tag_name("button").submit()
time.sleep(2)

#Windows maximize
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)

#Plant selection

# Odoo menu select button
# driver.find_element_by_xpath('/html/body/header/nav/div[1]/button').click()
driver.find_element_by_xpath("//button[@title='Home Menu']").click()
time.sleep(2)

# Purchase root menu selection
# PurchaseRootMenu= driver.find_element_by_xpath("/html/body/header/nav/div[1]/div/a[7]").click()
PurchaseRootMenu= driver.find_element_by_xpath("//a[@data-menu-xmlid='purchase.menu_purchase_root']").click()
time.sleep(2)

# Purchase requisition create section
PRCreate =driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button[3]').click()
time.sleep(2)

#Purchase requisition budget selection option
wait = WebDriverWait(driver, 30)
# dropdown_menu = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".o_input ui-autocomplete-input")))
# dropdown_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='o_field_input_96']")))
dropdown_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@name='budget_line_id']")))

dropdown_menu.click()
wait = WebDriverWait(driver, 20)
# dropdown_options = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.dropdown-item ui-menu-item-wrapper')))

dropdown_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@id='ui-id-1']")))


# dropdown_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//uL[@id='ui-id-54']")))
# dropdown_options = driver.find_element(By.CSS_SELECTOR, "#ui-id-54")

# dropdown_options= wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//a[@id='ui-id-84']")))
# dropdown_options.click()
# Find the desired option by its text and click on it
# desired_option_text = 'A. Fixed Plant Overhead - 2.Daily Allowance/Lunch-Plant - 2022-2023 (CPRL) (4118400.0) (4118400.0)'
desired_option_text = 'A. Fixed Plant Overhead - 3.Overtime & Holiday Bill - 2023-2024 (CPBL) (1020000.0) (1020000.0)'
for option in dropdown_options:
    option.text==desired_option_text
    option.click()
    break
#End Budget option selection
# Find the dropdown element

#start priority set oprtin
priority_Option = ['High','Medium','Low']
prioritySet= driver.find_element(By.XPATH,'//select[@name="priority"]')
prioritySet.click()
dropdownPriortyOption = Select(prioritySet)

for priority in priority_Option:
    dropdownPriortyOption.select_by_visible_text(priority)
    break
# dropdown_element = driver.find_element_by_id("dropdown_id")
time.sleep(2)
#End priority set oprtin

# Requisition date selection
current_datetime = datetime.now()

# Format the current date and time
pr_formatted_datetime = current_datetime.strftime("%m/%d/%Y %H:%M:%S")
prdateselection = driver.find_element_by_xpath('//input[@name="requisition_date"]').clear()
prdateselection = driver.find_element_by_xpath('//input[@name="requisition_date"]').send_keys(pr_formatted_datetime)
time.sleep(3)

#Requisition for selecton
requisitionlist_for =['Operation','Project']
requisitionfor_Set= driver.find_element(By.XPATH,'//select[@name="requirement_for"]')
requisitionfor_Set.click()
prdropdownrequisitionforOption = Select(requisitionfor_Set)

for requestfor in requisitionlist_for:
    prdropdownrequisitionforOption.select_by_visible_text(requestfor)
    break
time.sleep(2)
#End Requisition for selecton

#Approvedby  selecton
approveSelection=driver.find_element(By.XPATH,"//*[contains(@name,'assigned_to')]")

# Click on the dropdown to expand it
approveSelection.click()

# Wait for the options to be visible
wait = WebDriverWait(driver, 10)
approveSelectoptions = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@id='ui-id-2']")))

# Loop through the options and select the desired one
desired_option = 'Test_data_migration'  

for approveselect in approveSelectoptions:
    approveselect.text == desired_option
    approveselect.click()
    break
#End Approvedby  selecton

#Start requisition type  selecton
requisitionTypeList=['Site Purchase','Local','Foreign',]
requisitionTypeSelection=driver.find_element(By.XPATH,'//select[@name="requisition_type"]')
requisitionTypeSelection.click()
requisitionTypeOption = Select(requisitionTypeSelection)
for requisitionType in requisitionTypeList:
    requisitionTypeOption.select_by_visible_text(requisitionType)
    break
time.sleep(2)
#End requisition type  selecton

#Start Purchase type  selecton
purchaseTypeList=['New Purchase','Re-Purchase','Site Purchase']
purchaseTypeSelection=driver.find_element(By.XPATH,'//select[@name="purchase_type"]')
purchaseTypeSelection.click()
purchaseTypeOption = Select(purchaseTypeSelection)
for purchaseType in purchaseTypeList:
    purchaseTypeOption.select_by_visible_text(purchaseType)
    break
time.sleep(2)
#End requisition type  selecton


# dropdown_options = driver.find_element(By.XPATH,"//a[(text()='Test_data_migration')]")
AddALine=driver.find_element(By.XPATH,"//*[contains(text(),'Add a line')]").click()
time.sleep(3)

# #Start Line item   selecton
# ProductLineSelection=driver.find_element(By..

time.sleep(2)




# wait = WebDriverWait(driver, 20)
# approvedby_Set = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#o_field_input_1197")))

# approvedby_Set = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#o_field_input_1197")))


# approvedby_Set= driver.find_element(By.XPATH,"//div/input[@id='o_field_input_1197']")

# approvedby_Set.click()
# prapprovedbydropdonoption = Select(approvedby_Set)

# for prapprove in prapprovedby:
#     prapprovedbydropdonoption.select_by_visible_text(prapprove)
#     break
# time.sleep(2)





# Close the WebDriver instance

#End Requisition for selecton