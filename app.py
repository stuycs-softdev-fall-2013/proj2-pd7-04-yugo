from flask import Flask
from flask import render_template, session, request, redirect, url_for
import api

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    location = request.form['location']
    search = request.form['search']
    business = api.getNameAddress(search, location, 20)
    return render_template('results.html', search = search, location=location, business = business)


@app.route('/results/<location>/<name>', methods= ['GET','POST'])
def results():
    return render_template('pagetemplate.html', name=name, location=location)

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=7004)
