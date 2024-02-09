import random
import time
import keyring
import os
import shutil
import csv

from datetime import datetime
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import LOGIN_URL, SEARCH_URL, DOWNLOAD_PATH, ARCHIVE_PATH

def get_credentials(target_name):
    try:
        cred = keyring.get_credential(target_name,"") 

        return cred.username, cred.password
    except keyring.errors.KeyringError as e:
        print(f"Error retrieving credentials: {e}")

        return None, None

def random_sleep():
    sleep_time = random.uniform(2.5, 5.0)
    time.sleep(sleep_time)

def options():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless') # ensure GUI is off
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_PATH,
        "download.prompt_for_download": False,  # Disable the download prompt
    })
    return chrome_options

def display(driver):
    random_sleep()

    screenshot = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(screenshot))

    plt.imshow(image)
    plt.axis('off')
    plt.show()

def login(driver, username, password):
    try:
        driver.get(LOGIN_URL)

        scroll_script = "window.scrollBy(500, 0);"
        driver.execute_script(scroll_script)
    
        username_field = driver.find_element(By.ID, "login-form-username")
        username_field.send_keys(username)

        password_field = driver.find_element(By.ID, "login-form-password")
        password_field.send_keys(password)

        login_button = driver.find_element(By.ID, "login")
        #login_button.click()

    except Exception as e:
        print("\tLogin Error:")
        print(str(e))

def login_test(driver, username, password):
    try:
        driver.get(LOGIN_URL)

        username_field = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys(username)
        continue_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "login-submit"))
        )
        continue_button.click()
        random_sleep()
        
        password_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)
        continue_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "login-submit"))
        )
        continue_button.click()
        random_sleep()

      
    except Exception as e:
        print("\tLogin Error:")
        print(str(e))
    
def show_search_page(driver, jql_query):
    driver.get(SEARCH_URL)
    
    random_sleep()
    textarea = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "advanced-search")))
    textarea.send_keys(jql_query)

    search_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
    search_button.click()

    random_sleep()

def extract_issues_to_csv(driver):
    random_sleep()
    scroll_script = "window.scrollBy(500, 0);"
    driver.execute_script(scroll_script)

    button = driver.find_element(By.ID, "AJS_DROPDOWN__77")
    button.click()

    driver.implicitly_wait(5)

    option = driver.find_element(By.ID, "allCsvFields")
    option.click()

    export_button = driver.find_element(By.ID, "csv-export-dialog-export-button")
    export_button.click()

    # Wait for Download
    random_sleep()


def extract_issues_to_csv_test(driver):
    random_sleep()
    scroll_script = "window.scrollBy(500, 0);"
    driver.execute_script(scroll_script)

    button = driver.find_element(By.ID, "jira-export-trigger")
    button.click()

    driver.implicitly_wait(5)

    option = driver.find_element(By.ID, "allCsvWithBomFields")
    option.click()

    random_sleep()

def find_latest_tmp_file(directory):
    tmp_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".tmp")]

    if not tmp_files:
        raise FileNotFoundError("No temporary files found.")

    return max(tmp_files, key=os.path.getctime)

def create_csv_from_tmp(tmp_file_path, destination_folder, prefix="state"):
    current_date = datetime.now().strftime("%Y-%m-%d")
    csv_filename = f"{prefix}-{current_date}.csv"
    csv_file_path = os.path.join(destination_folder, csv_filename)

    with open(tmp_file_path, "r", encoding="utf-8") as tmp_file, open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv.reader(tmp_file))

    return csv_file_path

def copy_csv_to_archive(csv_file_path, archive_folder):
    shutil.copy(csv_file_path, os.path.join(archive_folder, os.path.basename(csv_file_path)))

def delete_files_except_latest(directory, keep_filename):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if file != keep_filename:
            os.remove(file_path)
