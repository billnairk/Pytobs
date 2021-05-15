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
    sf = sf
  )

@app.route("/<abc>")
def job_search(abc):
  return "haha"

@app.route("/qwdwd")
def tt():
  return render_template(
    "tt.html",
)

app.run(host="0.0.0.0")