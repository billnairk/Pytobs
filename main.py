import requests
from flask import Flask, render_template, request
from scrapper_sf import stack_over_flow
from scrapper_wwr import we_work_remotely
from scrapper_ok import remote_ok

app = Flask("Pytobs")
fake_db = {}

def save_fake_db(search):
  sf = stack_over_flow(search)
  wwr = we_work_remotely(search)
  ok = remote_ok(search)
  webs = sf[0] + wwr[0] + ok[0]
  total = sf[1] + wwr[1] + ok[1]
  fake_db[search] = webs
  fake_db[search+"total"] = total
  fake_db[search+"count"] = [sf[1], wwr[1], ok[1]]
  return fake_db[search], fake_db[search+"total"], fake_db[search+"count"]

@app.route("/")
def home():
  return render_template(
    "index.html",
  )

@app.route("/jobs")
def job_search():
  search = request.args.get('search')
  search = search.lower()
  db_result = fake_db.get(search)
  db_total = fake_db.get(search+"total")
  db_count = fake_db.get(search+"count")
  if not db_result or not db_total or not db_count:
    save = save_fake_db(search)
    db_result = save[0]
    db_total = save[1]
    db_count = save[2]
  return render_template(
    "search.html",
    search = search,
    db_result = db_result,
    db_total = db_total,
    db_count = db_count
)

app.run(host="0.0.0.0")