import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

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