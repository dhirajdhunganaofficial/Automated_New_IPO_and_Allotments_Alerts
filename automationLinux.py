from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def runAutomation(username, password):
    # Chrome options for headless Linux
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Remove Windows-specific PATH
    service = Service(executable_path='/usr/local/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Add user agent and anti-detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    newIPOissueMessage = ""
    totalNewIPOissue = 0
    totalIPOapplied = 0

    driver.get("https://meroshare.cdsc.com.np/")
    wait = WebDriverWait(driver, 40)

    # Step 1: Wait for and click the DP dropdown
    dp_dropdown = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".select2-selection"))
    )
    dp_dropdown.click()

    # Step 2: Wait for DP options to appear, then pick one by visible text
    # Replace 'NABIL INVESTMENT BANK LTD.' with your actual DP name

    print("--------------------")
    print(dp)
    print("--------------------")

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

    driver.save_screenshot("/tmp/debug.png")

    myASBA = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".msi-asba"))
    )
    myASBA.click()

    # Wait until ASBA page loads
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "app-asba ul li")))

    applyForIssue = driver.find_element(By.CSS_SELECTOR, "app-asba ul li:nth-child(1)")
    applyForIssue.click()

    # before
    # ipo_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "company-list")))

    # after
    # ipo_items = wait.until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table tbody tr"))
    # )

    try:
        ipo_items = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "company-list"))
        )
    except TimeoutException:
        ipo_items = []

    print("-------------------------")
    print(ipo_items)

    totalNewIPOissue = len(ipo_items)

    print(len(ipo_items))

    for item in ipo_items:
        print(type(item.text))
        print(len(item.text))
        print(item.text)

    if ipo_items:
        newIPOissueMessage = "☺ "+str(totalNewIPOissue)+" New IPO "+"listings available" if totalNewIPOissue > 1 else "☺ "+str(totalNewIPOissue)+" New IPO "+"listing available"
    else:
        newIPOissueMessage = "😞 No IPO listings available"

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

    sleep(3)
    driver.close()
    driver.quit()

    return newIPOissueMessage, totalNewIPOissue, totalIPOapplied

