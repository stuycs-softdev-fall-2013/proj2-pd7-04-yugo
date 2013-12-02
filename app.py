from flask import Flask
from flask import render_template, session, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    newLocation = request.form['newLocation']
    return redirect(url_for('main'))

@app.route('/main', methods = ['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    search = request.form['search']
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html')
    
@app.route('/search')
def serach():
    return render_template('search.html')

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
