import random
import time

from PIL import Image
from io import BytesIO
from IPython.display import display
import matplotlib.pyplot as plt
import chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def random_sleep():
    sleep_time = random.uniform(0.5, 1.5)
    print(f"\tSleep: {sleep_time:.2f}s")
    time.sleep(sleep_time)

def options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless') # ensure GUI is off
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--disable-dev-shm-usage')  # set path to chromedriver as per your configuration
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

    return chrome_options

def display(driver):
    print("\n[Current State]")

    random_sleep()

    screenshot = driver.get_screenshot_as_png()

    image = Image.open(BytesIO(screenshot))

    plt.imshow(image)
    plt.axis('off')
    plt.show()

def login(driver, username, password):
    try:
        driver.get("https://portail.agir.orange.com/secure/Dashboard.jspa")

        scroll_script = "window.scrollBy(500, 0);"
        driver.execute_script(scroll_script)

    
        username_field = driver.find_element(By.ID, "login-form-username")
        username_field.send_keys(username)


        password_field = driver.find_element(By.ID, "login-form-password")
        password_field.send_keys(password)

        login_button = driver.find_element(By.ID, "login")
        login_button.click()
    except Exception as e:
        print("\tLogin Error:")
        print(str(e))

def show_all_issues_page(driver):
    driver.get("https://portail.agir.orange.com/browse/?filter=-4")

def show_project_issues_page(driver, project_name):
    driver.get("https://portail.agir.orange.com/projects/"+project_name+"/issues/?filter=allissues")

def show_search_page(driver, jql):
    driver.get("https://portail.agir.orange.com/issues/?jql=")

    textarea = driver.find_element(By.ID, "advanced-search")
    textarea.send_keys(jql)

    search_button = driver.find_element(By.CLASS_NAME, "search-button")
    search_button.click()


def export_as_csv(driver):
    scroll_script = "window.scrollBy(500, 0);"
    driver.execute_script(scroll_script)

    button = driver.find_element(By.ID, "AJS_DROPDOWN__77")
    button.click()

    driver.implicitly_wait(5)

    option = driver.find_element(By.ID, "allCsvFields")
    option.click()

    export_button = driver.find_element(By.ID, "csv-export-dialog-export-button")
    export_button.click()