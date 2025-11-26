import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail(receiverEmail, ipoStatus):
    # -------- 1. Email Login Details --------
    your_email = "dhirajdhunganaofficial@gmail.com"
    your_app_password = "olhdfdeerxbikfzg"  # NOT your Gmail password!

    # -------- 2. Email Content --------
    receiver_email = receiverEmail
    subject = ipoStatus[0]+" - New IPO Alert"
    body = """
    Hi there,
    
    Unfortunately there are no IPO has been issued currently. But we will be constantly looking for them and if any new IPO is  listed you will be notified periodically so that you wont miss any IPOs.
    
    So, far you have applied """+str(ipoStatus[1])+""" IPOs.
    
    Regards,
    Dhiraj Dhungana
    Developer of this automated system.
    """

    # -------- 3. Creating the Email Format --------
    message = MIMEMultipart()
    message["From"] = your_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    # -------- 4. Sending the Email --------
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Gmail SMTP server
        server.starttls()  # encrypts the connection
        server.login(your_email, your_app_password)
        server.sendmail(your_email, receiver_email, message.as_string())
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print("Something went wrong:", e)
