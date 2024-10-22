import subprocess
from flask import Flask, redirect, render_template, request
import os

LOGO_FOLDER = os.path.join('static', 'logo')

app=Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = LOGO_FOLDER

@app.route('/')
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'IntelliTrafficLogo.jpg')
    return render_template("home.html", bgImage = full_filename)


@app.route('/configureVehicles')
def configureVehicles():
    result = subprocess.run(["python", "vehicle_detection.py"])
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'IntelliTrafficLogo.jpg')
    return render_template("home.html", bgImage = full_filename)

@app.route('/runSimulationScript')
def runSimulationScript():
    result = subprocess.Popen('python simulation.py')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'IntelliTrafficLogo.jpg')
    return render_template("home.html", bgImage = full_filename)

@app.route('/runTrafficTrendScript')
def runTrafficTrendScript():
    result = subprocess.Popen('python forecasting_new.py')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'IntelliTrafficLogo.jpg')
    return render_template("home.html", bgImage = full_filename)

@app.route('/runFaq')
def runFaq():
    return render_template("faq.html")


if __name__ == '__main__':
    app.run()