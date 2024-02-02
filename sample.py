from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

# Set the path to your web driver executable
driver_path = "D:\Program Files\chromedriver_win32\chromedriver.exe"  # Update this with the path to your driver

# Start the browser
# driver = webdriver.Chrome(driver_path)
driver = webdriver.Chrome('./chromedriver')
# Navigate to Jira login page
driver.get("https://portail.agir.orange.com/secure/Dashboard.jspa")

# Enter credentials and submit the login form
username = "your_username"
password = "your_password"

driver.find_element_by_id("login-form-username").send_keys(username)
driver.find_element_by_id("login-form-password").send_keys(password)
driver.find_element_by_id("login").click()

# Wait for the login process to complete
time.sleep(2)

# Perform actions on Jira (e.g., navigate to issues, extract data)

# Example: Extracting issue titles and saving to CSV
issues = driver.find_elements_by_css_selector(".issue-link")
with open("jira_issues.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Issue Title"])
    for issue in issues:
        csv_writer.writerow([issue.text])

# Close the browser
driver.quit()
