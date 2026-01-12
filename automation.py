from contextlib import nullcontext

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from time import sleep

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def runAutomation(username, password):
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    service = Service(PATH)

    driver = webdriver.Chrome(service=service)

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
    usernameField.send_keys(username)

    passwordField = driver.find_element(By.ID, "password")
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

    currentIssue = driver.find_element(By.CSS_SELECTOR, "app-asba ul li:nth-child(2)")
    currentIssue.click()

    # test1 = ['Citizens Santulit Yojana.', '-', 'For General Public (CSTY)', 'IPO', 'Close Ended Mutual Fund']
    # test3 = ['Citizens Santulit Yojana.', '-', 'For General Public (CSTY)', 'IPO', 'Close Ended Mutual Fund']
    # test2 = ['VIJAYA LAGHUBITTA BITTIYA SANSTHA LIMITED', '-', 'For General Public (VLBS)', 'FPO', 'Ordinary Shares']
    # test4 = ['VIJAYA LAGHUBITTA BITTIYA SANSTHA LIMITED', '-', 'For General Public (VLBS)', 'FPO', 'Ordinary Shares']

    try:
        sharesToApply = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "company-list"))
        )
    except TimeoutException:
        sharesToApply = []

    listingDetails = []

    for share in sharesToApply:
        spanTexts = []
        spans = share.find_elements(By.TAG_NAME, "span")
        for i in range (len(spans)):
            spanTexts.append(spans[i].text)
        listingDetails.append(spanTexts)

    # listingDetails = []
    # listingDetails.append(test1)
    # listingDetails.append(test2)
    # listingDetails.append(test3)
    # listingDetails.append(test4)


    driver.close()
    driver.quit()

    return len(listingDetails), listingDetails