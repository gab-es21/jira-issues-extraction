import functions as fun
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

PROJECT_NAMES = ["GLOBALAR"]
QUERIES = ["\"Begin Date\" < startOfYear() "]

if __name__ == "__main__":
    chrome_options = fun.options()
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=chrome_options)

    # Login Page
    username = "your_username"
    password = "your_password"
    #fun.login(driver, username, password)
    #fun.display(driver)

    # Filter All Issues
    #fun.show_all_issues_page(driver)
    #fun.display(driver)

    fun.show_search_page(driver,QUERIES[0])
    fun.display(driver)
    #fun.export_as_csv(driver)
    #fun.display(driver)