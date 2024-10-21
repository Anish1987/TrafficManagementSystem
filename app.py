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

def redirectToconfigureVehicles():
    print('redirectToconfigureVehicles')
    return redirect("/configureVehicles")

@app.route('/configureVehicles')
def configureVehicles():
    return render_template("configureVehiclesForm.html")

@app.route('/runSimulationScript')
def runSimulationScript():
    # return exec('simulation.py')
    # return subprocess.call("simulation.py", shell=True)
    result = subprocess.run(["python", "simulation.py"])

@app.route('/submit-vehicle-count', methods=['POST'])
def submit_vehicle_count():
    vehicles = request.form['vehicles']

if __name__ == '__main__':
    app.run()