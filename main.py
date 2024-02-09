import chromedriver_autoinstaller

from selenium import webdriver
import os
from src import jira_extractor as fun
from src import jql_queries as jql
from src.config import CREDENTIAL_MANAGER_TARGET_NAME, DOWNLOAD_PATH, ARCHIVE_PATH


if __name__ == "__main__":

    chrome_options = fun.options()
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=chrome_options)

    # Login
    username, password = fun.get_credentials(CREDENTIAL_MANAGER_TARGET_NAME)
    fun.login_test(driver, username, password)
    fun.random_sleep()

    # Search and Extraction
    fun.show_search_page(driver,jql.QUERIES[0])
    fun.extract_issues_to_csv_test(driver)

    # Manage Files
    latest_tmp_file = fun.find_latest_tmp_file(DOWNLOAD_PATH)
    csv_file_path = fun.create_csv_from_tmp(latest_tmp_file, DOWNLOAD_PATH, prefix="state")
    fun.copy_csv_to_archive(csv_file_path, ARCHIVE_PATH)
    fun.delete_files_except_latest(DOWNLOAD_PATH, os.path.basename(csv_file_path))

    #fun.display(driver)
