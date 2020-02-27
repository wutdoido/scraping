from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib3

URL = "https://ca.indeed.com/jobs?q=&l=Windsor%2C+ON&fromage=last&sort=date"


page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find("td", id="resultsCol")
results.prettify()


job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')
prospective_jobs = []

for job in job_elems:
    job_loc = job.find('span', class_="location")
    job_title = job.find('div', class_="title").text.replace('\n', '')
    job_href = job.find("a")["href"]
    if (job_loc != None and job_loc != None and "Windsor" in job_loc.text):
        job_string = "Title: " + job_title + "      Link: https://ca.indeed.com" + job_href
        prospective_jobs.append(job_string)
        print(job_string)

print(len(prospective_jobs))
