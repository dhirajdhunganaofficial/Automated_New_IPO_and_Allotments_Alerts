from contextlib import nullcontext

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def runAutomation(email, dp, username, password):
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    service = Service(PATH)

    driver = webdriver.Chrome(service=service)

    newIPOissue = ""
    totalIPOapplied = 0

    driver.get("https://meroshare.cdsc.com.np/")
    wait = WebDriverWait(driver, 20)

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

    usernameField = driver.find_element(By.ID, "username")
    # usernameField.send_keys("02349532")
    usernameField.send_keys(username)

    passwordField = driver.find_element(By.ID, "password")
    # passwordField.send_keys("Deerw@lk25")
    passwordField.send_keys(password)

    login = driver.find_element(By.CLASS_NAME, "sign-in")

    login.click()

    menu = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".mdi-menu"))
    )
    menu.click()

    myASBA = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".msi-asba"))
    )
    myASBA.click()

    # Wait until ASBA page loads
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "app-asba ul li")))

    applyForIssue = driver.find_element(By.CSS_SELECTOR, "app-asba ul li:nth-child(1)")
    applyForIssue.click()

    ipo_items = driver.find_elements(By.CSS_SELECTOR, "app-share-list .card")

    if len(ipo_items) == 0:
        print("No IPO listings available.")
        newIPOissue = "No IPO listings available."
    else:
        print(f"Found {len(ipo_items)} IPO(s).")
        newIPOissue = "Found {len(ipo_items)} IPO(s)."

    sleep(3)

    applicationReport = driver.find_element(By.CSS_SELECTOR, "app-asba ul li:nth-child(3)")
    applicationReport.click()

    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="main"]/div/app-asba/div/div[2]/app-share-list/div/div/div[2]/div[1]')))
    parentDiv = driver.find_element(By.XPATH,
                                    '//*[@id="main"]/div/app-asba/div/div[2]/app-share-list/div/div/div[2]/div[1]')
    childDivs = parentDiv.find_elements(By.XPATH, "./div")

    # Safely get applied shares
    totalIPOapplied = len(childDivs)

    if len(childDivs) == 0:
        print("No applied shares found.")
    else:
        print(f"Found {len(childDivs)} applied shares.")

    sleep(3)
    driver.close()
    driver.quit()

    return newIPOissue, totalIPOapplied

