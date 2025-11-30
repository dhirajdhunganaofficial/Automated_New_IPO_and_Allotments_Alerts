from flask import Flask, render_template, request

import automation
import sendEmail

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='IPO Allotment Alerts')

@app.route('/automationReport', methods=['POST'])
def automationStarted():
    email = request.form['email']
    dp = request.form['Depository Participants']
    username = request.form['Username']
    password = request.form['password']
    report = automation.runAutomation(dp, username, password)
    sendEmail.sendEmail(email, report)
    print("Report: ", report)
    print(report)
    return render_template('automationReport.html', title='Automation Report', email=email, dp=dp, username=username, password=password, report=report)


@app.route('/home')
def home():
    return render_template('home.html', title='My Automated App')

@app.route('/result', methods = ['POST'])
def result():
    name = request.form['username']
    return render_template('result.html', user=name)

if __name__ == '__main__':
    app.run(debug=True)