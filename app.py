
from Flask import flask
from Flask import render_template


@app.route('/')
def home:
  return render_template("index.html")
