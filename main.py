import requests
from flask import Flask, render_template, request
from scrapper_sf import stack_over_flow as sf

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
  return render_template(
    "search.html",
    search = search,
    sf = sf(search)
)


app.run(host="0.0.0.0")