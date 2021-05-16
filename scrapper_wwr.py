import requests
from bs4 import BeautifulSoup

def extract_jobs(WWR_URL):
  jobs = []
  total = 0
  result = requests.get(WWR_URL)
  soup = BeautifulSoup(result.text, "html.parser")
  sections = soup.find("div", class_="jobs-container").find_all("section", class_="jobs")
  for section in sections:
    section_title = section.find("h2").find("a").get_text()
    print(f"Scrapping in WeWorkRemotely.. [{section_title}]")
    li = section.find("ul").find_all("li")
    for val, job in enumerate(li[:-1]):
      jobs.append(extract_job(job))
    total += val
  return jobs, (total+1)

def extract_job(html):
  title = html.find("span", class_="title").get_text()
  company =html.find("span", class_="company").get_text()
  location = html.find("span", class_="region company")
  if location == None:
    location = None
  else:
    location = html.find("span", class_="region company").get_text()
  links = html.find_all("a")
  link = links[1]['href']
  return {
    "title": title,
    "company": company,
    "location": location,
    "site": "WeWorkReomtely",
    "link": f"https://weworkremotely.com{link}"
  }

def we_work_remotely(search):
  WWR_URL = f"https://weworkremotely.com/remote-jobs/search?term={search}"
  return extract_jobs(WWR_URL)