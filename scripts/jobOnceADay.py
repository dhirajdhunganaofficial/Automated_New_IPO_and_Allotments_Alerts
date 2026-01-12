from flask import Flask
from configLinux import Config
from models import Subscriber
from extensions import db
import automationLinux, sendEmail


from utils.secrets import get_secret
USERNAME, PASSWORD = get_secret()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def runJob():
    with app.app_context():
        subscribers = Subscriber.query.all()

        emailList = []

        print(subscribers)

        for subscriber in subscribers:
            if subscriber.frequency == "once":
                print(subscriber.email)
                emailList.append(subscriber.email)

        report = automationLinux.runAutomation(USERNAME, PASSWORD)
        sendEmail.sendEmail(emailList, report)

if __name__ == '__main__':
    runJob()

import sqlite3

conn = sqlite3.connect("automation.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM subscribers;")
rows = cursor.fetchall()

for row in rows:
    print(row)