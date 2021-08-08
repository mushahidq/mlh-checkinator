import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

info_file = open('info.json')
info = json.load(info_file)

devpost_login = 'https://secure.devpost.com/users/login?ref=top-nav-login'
devpost_mlh_open = 'https://devpost.com/hackathons?organization=Major%20League%20Hacking&status[]=ope'

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1200")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")    
# chrome_options.add_argument("--headless")

# Loggin into devpost
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(devpost_login)

time.sleep(10)
devpost_email = driver.find_element_by_xpath('//*[@id="user_email"]')
devpost_email.send_keys(info['devpost']['user'])

devpost_pass = driver.find_element_by_xpath('//*[@id="user_password"]')
devpost_pass.send_keys(info['devpost']['password'])

devpost_submit = driver.find_element_by_xpath('//*[@id="submit-form"]')
devpost_submit.click()

# Go to the open MLH hackathons page
time.sleep(5)
driver.get(devpost_mlh_open)

time.sleep(2)
mlh_open = driver.find_element_by_xpath('//*[@id="results-and-filters"]/div[2]/div[2]/div/a')
mlh_open.click()

time.sleep(5)
mlh__open_register = driver.find_element_by_xpath('//*[@id="primary"]/a')
mlh__open_register.click()

time.sleep(5)   
team_solo = driver.find_element_by_xpath('//*[@id="registration-form"]/div[1]/span[1]')
team_solo.click()
ref_mlh = driver.find_element_by_xpath('//*[@id="registration-form"]/div[3]/span[2]')
ref_mlh.click()
eligibility_agree = driver.find_element_by_xpath('//*[@id="registration-form"]/div[9]')
eligibility_agree.click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
rules_agree = driver.find_element_by_xpath('//*[@id="registration-form"]/div[11]')
rules_agree.click()

register = driver.find_element_by_xpath('//*[@id="registration-form"]/div[12]/input')
register.click()

time.sleep(5)
mlh_link = driver.find_element_by_xpath('//*[@id="active-items"]/div[1]/div[1]/p[1]/a').get_attribute('href')
mlh_check_in = driver.find_element_by_xpath('//*[@id="active-items"]/div[3]/div[1]/p[1]/a').get_attribute('href')

mlh_link = 'https://organize.mlh.io/participants/events/7157-slam-dunk-hacks'
driver.get(mlh_link)
driver.get('https://my.mlh.io/users/login')
time.sleep(2)
login_email = driver.find_element_by_xpath('//*[@id="user_email"]')
login_email.send_keys(info['mlh']['user'])
login_password = driver.find_element_by_xpath('//*[@id="user_password"]')
login_password.send_keys(info['mlh']['password'])
login = driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/button')
login.click()   
driver.get(mlh_link)
reg = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]')
reg.click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
# driver.find_element_by_xpath('//*[@id="edit_participation_316880"]/div/a').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="edit_participation_316880"]/fieldset[1]/div/label').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="edit_participation_316880"]/fieldset[2]/div/label').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="participation_event_questions_form_which_of_these_regio_015f"]/option[4]').click()
# time.sleep(1)
driver.find_element_by_xpath('//*[@id="edit_participation_316880"]/div[2]/input').click()

# mlh_check_in = 'https://hackp.ac/RoboHacksCheckIn'
# Check In Form
driver.get(mlh_check_in)
time.sleep(10)
actions = ActionChains(driver)
actions.send_keys(Keys.RETURN)
actions.pause(2)
actions.send_keys(Keys.RETURN)
actions.pause(2)

actions.send_keys(info['mlh']['fname'])
actions.pause(2)
actions.key_down(Keys.RETURN).key_up(Keys.RETURN)
actions.pause(2)
actions.send_keys(info['mlh']['lname'])
actions.pause(2)
actions.key_down(Keys.RETURN).key_up(Keys.RETURN)
actions.pause(2)

actions.send_keys(info['mlh']['mob'])
actions.key_down(Keys.RETURN).key_up(Keys.RETURN) 
actions.pause(2)

actions.send_keys(info['mlh']['user'])
actions.key_down(Keys.RETURN).key_up(Keys.RETURN)
actions.pause(2)

actions.send_keys(Keys.TAB)
actions.send_keys(info['mlh']['discord-username'])
actions.key_down(Keys.RETURN).key_up(Keys.RETURN)
actions.pause(2)

actions.key_down(Keys.RETURN).key_up(Keys.RETURN)
actions.pause(2)

actions.key_down('c').key_up('c')
actions.pause(2)

actions.pause(2)
actions.send_keys(info['mlh']['country'])
actions.pause(2)
actions.send_keys(Keys.DOWN)
actions.pause(2)
actions.send_keys(Keys.DOWN)
actions.pause(2)
actions.send_keys(Keys.RETURN)
actions.pause(2)
actions.send_keys(Keys.RETURN)
actions.pause(2)
actions.send_keys('y')
actions.pause(2)
actions.send_keys('y')
actions.pause(2)
actions.send_keys('y')
actions.pause(2)
actions.send_keys('y')
actions.pause(2)
actions.send_keys('y')
actions.pause(2)
actions.send_keys('y')
actions.pause(2)
actions.send_keys('y')
actions.pause(2)

actions.send_keys(info['mlh']['linkedin'])
actions.pause(2)
actions.send_keys(Keys.RETURN)
actions.pause(2)

actions.send_keys(info['mlh']['grad-year'])
actions.pause(2)
actions.send_keys(Keys.RETURN)
actions.pause(2)

actions.send_keys(Keys.RETURN)
actions.pause(2)
actions.send_keys('h')
actions.pause(2)
actions.send_keys('y')
actions.pause(2)

actions.send_keys(Keys.TAB)
actions.pause(2)
actions.send_keys(Keys.TAB)
actions.pause(2)
actions.send_keys(Keys.TAB)
actions.pause(2)


actions.send_keys(Keys.RETURN)
actions.pause(2)
actions.perform()

# driver.quit()