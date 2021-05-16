import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "site", "link"])
  # print(jobs)
  for job in jobs:
    # print(job)
    writer.writerow(list(job.values()))
  return