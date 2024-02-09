# Jira Issues Extraction

## Introduction

This project facilitates the extraction of Jira issues and their details into a CSV file. Leveraging Python and the Selenium library for web automation, the script interacts with the Jira platform, automating tasks such as login, issue retrieval, and CSV file creation.


## Features

- **Login Automation:** The script automates the login process to your Jira account, removing the need for manual intervention.
  
- **Issue Extraction:** Retrieve Jira issues based on specified criteria, such as project, time range, or issue type.

- **CSV Output:** Export the retrieved issues and their details to a CSV file for easy analysis and reporting.

## Getting Started

1. **Setup Python Environment:**
   - Create a virtual environment using `python -m venv venv`.
   - Activate the virtual environment: 
     - On Windows: `venv\Scripts\activate`

2. **Install Dependencies:**
   Run `pip install -r requirements.txt` to install the necessary Python packages.

3. **Configure Credentials:**
   Add your Jira credentials to the Windows Credential Manager, follow instructions [here](#setting-up-credentials).

4. **Run the Script:**
   Execute `python main.py` to initiate the Jira issues extraction process.


## Setting Up Credentials

To interact with Jira, you need to store credentials securely. This project uses the Windows Credential Manager to manage credentials.

### Adding a Generic Credential

Follow these steps to add a generic credential to the Windows Credential Manager:

1. Press `Win + S` to open the Windows search bar.

2. Type "Credential Manager" and select it from the search results.

3. In Credential Manager, click on "Windows Credentials."

4. Under "Generic Credentials," click "Add a generic credential."

5. Enter the following information:

   - **Internet or network address:** Provide the target service or system's address.
   - **User name:** Your username for the service or system.
   - **Password:** Your password for the service or system.

6. Click "OK" to save the credentials.
