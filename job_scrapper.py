from bs4 import BeautifulSoup
import requests

def scrape_indeed_jobs():
    url = "https://www.indeed.com/jobs?q=python+developer&l="
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "Failed to fetch jobs"

    soup = BeautifulSoup(response.text, "html.parser")
    
    job_listings = []
    for job_card in soup.find_all("div", class_="job_seen_beacon"):
        title = job_card.find("h2").text.strip() if job_card.find("h2") else "No Title"
        company = job_card.find("span", class_="companyName").text.strip() if job_card.find("span", class_="companyName") else "Unknown Company"
        location = job_card.find("div", class_="companyLocation").text.strip() if job_card.find("div", class_="companyLocation") else "Unknown Location"
        
        job_listings.append({"title": title, "company": company, "location": location})

    return job_listings
