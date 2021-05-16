import requests
from flask import Flask, render_template, request
from scrapper_sf import stack_over_flow
from scrapper_wwr import we_work_remotely

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

app = Flask("Pytobs")

@app.route("/")
def home():
  return render_template(
    "index.html",
  )

@app.route("/jobs")
def job_search():
  search = request.args.get('search')
  sf = stack_over_flow(search)
  wwr = we_work_remotely(search)
  webs = sf[0] + wwr[0]
  total = sf[1] + wwr[1]
  return render_template(
    "search.html",
    search = search,
    webs = webs,
    total = total,
    total_wwr = wwr[1],
    total_sf = sf[1]
)


app.run(host="0.0.0.0")