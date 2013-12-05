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

@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')
	
@app.route('/compile/<saddress>/<eaddress>', methods= ['GET'])
def compile(saddress=None, eaddress=None):
    if request.method == 'GET':
        return render_template('compile.html', saddress=saddress, eaddress=eaddress)
	
	
@app.route('/results/<location>/<name>', methods= ['GET','POST'])
def results():
	if request.method == 'GET':
		return render_template('results.html')
	location = request.form['location']
	search = request.form['search']
	return render_template('go.html', search=search, location=location)
	

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=7004)
