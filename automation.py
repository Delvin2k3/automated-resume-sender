from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def apply_on_indeed(resume_path):
    driver = webdriver.Chrome()
    driver.get("https://www.indeed.com/")
    time.sleep(5)

    search_box = driver.find_element(By.ID, "text-input-what")
    search_box.send_keys("Software Developer")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    jobs = driver.find_elements(By.CLASS_NAME, "tapItem")
    if jobs:
        jobs[0].click()
        time.sleep(3)

        apply_button = driver.find_element(By.CLASS_NAME, "ia-IndeedApply-button")
        apply_button.click()

        upload = driver.find_element(By.NAME, "resume")
        upload.send_keys(resume_path)

        time.sleep(5)

    driver.quit()

def apply_on_linkedin(resume_path):
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(5)

    search_box = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
    search_box.send_keys("Python Developer")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")
    if jobs:
        jobs[0].click()
        time.sleep(3)

        apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        apply_button.click()

        upload = driver.find_element(By.NAME, "resume")
        upload.send_keys(resume_path)

        time.sleep(5)

    driver.quit()

def apply_on_naukri(resume_path):
    driver = webdriver.Chrome()
    driver.get("https://www.naukri.com/")
    time.sleep(5)

    upload = driver.find_element(By.ID, "resumeUpload")
    upload.send_keys(resume_path)

    time.sleep(5)
    driver.quit()
