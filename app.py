from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle
import os

app = Flask(__name__)

# Path to ChromeDriver
CHROMEDRIVER_PATH = "chromedriver.exe"

# Path to Chrome Profile (Change this based on your system)
CHROME_PROFILE_PATH = "C:\Program Files\Google\Chrome\Application"

# Function to set up Selenium WebDriver
def get_driver():
    service = Service(CHROMEDRIVER_PATH)
    options = Options()

    # ✅ Use real Chrome profile
    options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
    options.add_argument("--profile-directory=Default")

    # ✅ Anti-bot settings
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=service, options=options)
    
    # ✅ Load cookies if available
    cookies_file = "cookies.pkl"
    if os.path.exists(cookies_file):
        driver.get("https://www.indeed.com")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
    
    return driver

# Function to automate job application on Indeed
def apply_on_indeed(job_title, location):
    driver = get_driver()
    driver.get("https://www.indeed.com/")

    time.sleep(2)  # Wait for page to load

    # Find job search fields and enter job title & location
    job_search_box = driver.find_element(By.ID, "text-input-what")
    location_box = driver.find_element(By.ID, "text-input-where")

    job_search_box.send_keys(job_title)
    location_box.send_keys(location)
    job_search_box.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for search results to load

    # Click on first job listing
    jobs = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")
    if jobs:
        jobs[0].click()
        time.sleep(3)

        # Automate clicking the apply button (if available)
        try:
            apply_button = driver.find_element(By.CLASS_NAME, "ia-IndeedApplyButton")
            apply_button.click()
            time.sleep(3)
        except:
            print("Apply button not found")

    driver.quit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    job_site = request.form.get('job_site')
    job_title = "Software Engineer"
    location = "Remote"

    if job_site == "indeed":
        apply_on_indeed(job_title, location)
        return "Applied on Indeed!"

    return "Invalid job site selected."

@app.route('/save_cookies')
def save_cookies():
    driver = get_driver()
    driver.get("https://www.indeed.com")

    input("Login manually and press Enter...")  # Wait for user to log in

    # Save cookies after login
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    driver.quit()
    return "Cookies saved!"

if __name__ == '__main__':
    app.run(debug=True)
