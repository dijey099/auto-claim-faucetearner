import os
import time
from termcolor import colored
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


load_dotenv(dotenv_path=".env")

USER = os.getenv("USER")
MAIL = os.getenv("MAIL")
PASSWORD = os.getenv("PASSWORD")
URL = "https://faucetearner.org/login.php"
print("*** Auto Claim for FaucetEarner websites ***")
print("Auto claiming on " + colored("https://faucetearner.org", 'magenta'))
print(colored("Buy this script from the author only!", 'white', 'on_red', attrs=['bold']) + "\n")
print("Author: " + colored("Dijey", 'green'))
print("Maintainer: " + colored("Dijey", 'green'))
print("Facebook: " + colored("https://fb.me/d1j3y", 'cyan'))
print("Mobile: " + colored("+261 32 61 968 23\n\n", 'yellow'))

opts = Options()
opts.add_argument("--width=240")
opts.add_argument("--height=800")
opts.add_argument("--headless")
opts.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36")
browser = webdriver.Firefox(options=opts)


def print_as_log(log):
	_time = time.time()
	m_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_time))
	print(f"[{m_time}] {log}")


print_as_log("Login...")
browser.get(URL)
login_btn = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//button[@type="button"]')))
mail_field = browser.find_element(By.NAME, "email")
pass_field = browser.find_element(By.NAME, "password")

mail_field.send_keys(MAIL)
pass_field.send_keys(PASSWORD)
time.sleep(1)
login_btn.click()

try:
	checked = WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{USER}')]")))
except:
	print_as_log("Login failed!")
	exit()

if checked:
	print_as_log(colored("Logged in!", 'green'))
	try:
		alert_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@id="basic-addon1"]')))
		alert_btn.click()
	except:
		pass
	print_as_log("Preparing for new claim...")

	browser.get("https://faucetearner.org/faucet.php")
	while True:
		while int(browser.find_element(By.ID, "second").text) != 55: pass
		claim_btn = WebDriverWait(browser, 100).until(EC.presence_of_element_located((
			By.XPATH,
			'//button[@class="m-auto mt-2 reqbtn btn solid_btn text-white d-flex align-items-center" and @type="button" and @onclick="apireq()"]'
		)))
		browser.execute_script("arguments[0].scrollIntoView();", claim_btn)
		claim_btn.click()
		time.sleep(2)

		reward_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-info.fs-2")))
		print_as_log(colored("= New claim triggered =", 'white', 'on_green'))
		print_as_log(colored(f"You got {reward_field.text}", 'cyan', attrs=['bold']))

		ok_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'alert_ok')))
		ok_btn.click()
		time.sleep(1)

		print_as_log("Preparing for new claim...")