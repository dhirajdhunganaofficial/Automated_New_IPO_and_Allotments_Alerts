from flask import Flask, render_template, request

from utils.secrets import get_secret

import automation, automationLinux
import sendEmail

app = Flask(__name__)

USERNAME, PASSWORD = get_secret()

@app.route('/')
def index():
    return render_template('index.html', title='IPO Allotment Alerts')

@app.route('/automationReport', methods=['POST'])
def automationStarted():
    email = request.form['email']
    print(email)
    report = automationLinux.runAutomation("02349532", "Deerw@lk25")
    automationReport = sendEmail.sendEmail(email, report)
    print("Report: ", report)
    print("Automation Report: ", automationReport)
    # return render_template('automationReport.html', title='Automation Report', email=email, dp=dp, username=username, password=password, report=report)
    return render_template('automationReport.html', title='Automation Report', email=email, report=automationReport)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)