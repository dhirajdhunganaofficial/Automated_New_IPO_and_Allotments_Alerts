from flask import Flask, render_template, request, jsonify
# from config import Config
from configLinux import Config
from extensions import db

from utils.secrets import get_secret

from models import Subscriber
import automation, automationLinux
import sendEmail

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

USERNAME, PASSWORD = get_secret()

@app.route('/')
def index():
    return render_template('index.html', title='IPO Allotment Alerts')

@app.route('/automationReport', methods=['POST'])
def automationStarted():
    email = request.form['email']
    report = automationLinux.runAutomation(USERNAME, PASSWORD)
    automationReport = sendEmail.sendEmail(email, report)
    return render_template('automationReport.html', title='Automation Report', email=email, report=automationReport)


@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.json

    print(data)

    subscriber = Subscriber(
        email=data["email"],
        frequency=data["frequency"],
        timezone=data.get("timezone", "UTC"),
        still_subscribe=True
    )

    try:
        db.session.add(subscriber)
        db.session.commit()

        return jsonify({"status": "subscribed"})
    except Exception as e:
        db.session.rollback()

        print(e)
        if "UNIQUE constraint failed" in str(e):
            subscriber = Subscriber.query.filter_by(email=data["email"]).first()
            if subscriber:
                subscriber.frequency = data["frequency"]
                db.session.commit()
                print("Updated Successfully!")
                return jsonify({"status": "updated"})
        else:
            return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)