
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = r"C:\Program Files (x86)\chromedriver.exe"
service = Service(PATH)

driver = webdriver.Chrome(service=service)

driver.get("https://meroshare.cdsc.com.np/")
wait = WebDriverWait(driver, 20)
print(driver.title)

# Step 1: Wait for and click the DP dropdown
dp_dropdown = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".select2-selection"))
)
dp_dropdown.click()

# Step 2: Wait for DP options to appear, then pick one by visible text
# Replace 'NABIL INVESTMENT BANK LTD.' with your actual DP name
dp_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'NIMB ACE CAPITAL LIMITED (10600)')]"))
)
dp_option.click()

username = driver.find_element(By.ID, "username")
username.send_keys("02349532")

password = driver.find_element(By.ID, "password")
password.send_keys("Deerw@lk25")

login = driver.find_element(By.CLASS_NAME, "sign-in")
login.click()

sleep(15)