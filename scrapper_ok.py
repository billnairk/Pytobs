import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_jobs(OK_URL):
  jobs = []
  total =0
  result = requests.get(OK_URL, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  trs = soup.find("table", {"id": "jobsboard"}).find_all("tr", class_="job")
  for val, tr in enumerate(trs):
    jobs.append(extract_job(tr))
  total += val
  return jobs, (total+1)

def extract_job(html):
  td = html.find("td", class_="company_and_position")
  title = td.find("h2").get_text()
  company = td.find("h3").get_text()
  location = td.find("div", class_="location")
  if location == None:
    location = None
  else:
    location = td.find("div", class_="location").get_text()
  link = td.find("a")["href"]
  return {
    "title": title,
    "company": company,
    "location": location,
    "site": "RemoteOK",
    "link": f"https://remoteok.io{link}"
  }

def remote_ok(search):
  OK_URL = f"https://remoteok.io/remote-{search}-jobs"
  return extract_jobs(OK_URL)