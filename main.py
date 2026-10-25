from flask import Flask, render_template
import gallery
import request
import admin
import User

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/request/')
def request():
    return render_template('request.html')

@app.route("/consultation/")
def consultation():
    return render_template('consultation.html')

@app.route("/paint/")
def paint():
    return render_template('paint.html')

@app.route("/Works/")
def Works():
    return render_template('Works.html')

def main():
    app.run(debug=True)



main()

