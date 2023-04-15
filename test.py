from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver with the specified driver executable
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to a web page
driver.get('http://saucedemo.com/')

# Find an element by its ID and interact with it (e.g. type text, click)
username = driver.find_element_by_css_selector('#user-name')
username.send_keys('shanka')
password = driver.find_element_by_css_selector('#password')
password.send_keys('automation')
login_button = driver.find_element_by_css_selector('#login-button')
login_button.click()

# Close the WebDriver
driver.close()