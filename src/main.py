"""
1. create linux command that accept argument(name of the repo)
2.create a folder with the argument
3.enter in the folder
4.create README.md

"""
import os
import sys
import time


from selenium import webdriver

repoName = sys.argv[1]


PATH = '/home/mercy/chrome driver/chromedriver'
driver = webdriver.Chrome(PATH)#ouvrir le navigateur

driver.get("https://www.github.com/login")

mailInput = driver.find_elements_by_xpath("//*[@id='login_field']")[0]
mailInput.send_keys("kirangimercyplaisir@gmail.com")

pswdInput = driver.find_elements_by_xpath("//*[@id='password']")[0]
pswdInput.send_keys(os.getenv('MYPASSWORD'))



submitButton =driver.find_elements_by_xpath("//*[@id='login']/div[4]/form/div/input[12]")

if isinstance(submitButton,list):
	submitButton[0].submit()
else:
	submitButton.submit()

driver.get("https://github.com/new")


repoInputName = driver.find_elements_by_xpath("//*[@id='repository_name']")
repoInputName[0].send_keys(repoName)

createRepoButton = driver.find_elements_by_xpath("//*[@id='new_repository']/div[4]/button")

time.sleep(3)

if isinstance(createRepoButton,list):

	createRepoButton[0].click()
else:
	createRepoButton.click()

print("REPO CREATED SUCCEFFULLY")

time.sleep(5)
driver.quit()
















