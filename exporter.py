import csv

def save_to_file(jobs, search):
  with open(f"{search}.csv", "w", newline='' ,encoding="UTF-8") as file:
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "site", "link"])
    for job in jobs:
      writer.writerow(list(job.values()))
  return