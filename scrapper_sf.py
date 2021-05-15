import requests
from bs4 import BeautifulSoup

def get_last_page(SF_URL):
  result = requests.get(SF_URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", class_="s-pagination").find_all("span")
  last_page = pagination[-2].get_text()
  return int(last_page)

def extract_jobs(last_page, SF_URL):
  jobs = []
  for page in range(last_page+1):
    print(f"Scrapping... {page} of {last_page}")
    result = requests.get(f"{SF_URL}&pg={page}")
    soup = BeautifulSoup(result.text, "html.parser")
    list_results = soup.find_all("div", class_="-job")
    for result in list_results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def extract_job(html):
  title = html.find("h2").find("a").get_text()
  company_row = html.find("h3").find_all("span")
  company = company_row[0].get_text(strip=True)
  location = company_row[1].get_text(strip=True)
  id = html["data-jobid"]
  link = f"https://stackoverflow.com/jobs/{id}"
  # print(f"title: {title}\ncompany: {company}\nlocation: {location}\nlink: {link}")
  return {
    "title": title,
    "company": company,
    "location": location,
    "link": link
  }
def stack_over_flow(search):
  SF_URL = f"https://stackoverflow.com/jobs?&q={search}"
  lp = get_last_page(SF_URL)
  return extract_jobs(lp, SF_URL)
