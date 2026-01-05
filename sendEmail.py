import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os.path import split


def sendEmail(receiverEmail, ipoStatus):
    # -------- 1. Email Login Details --------
    your_email = "dhirajdhunganaofficial@gmail.com"
    your_app_password = "olhdfdeerxbikfzg"  # NOT your Gmail password!

    # -------- 2. Email Content --------
    receiver_email = receiverEmail
    subject = ipoStatus[0] + " - New IPO Alert"

    message = "are " + str(ipoStatus[1]) + " new IPOs" if ipoStatus[1] > 1 else "is a new IPO"

    companyName = ""
    symbol = ""
    listedAs = ""
    listedFor = ""
    type = ""
    tr = ""
    trStart = "<tr>"
    trEnd = "</tr>"
    tdStart = '<td style="border:1px solid #000;">'
    tdEnd = "</td>"

    automationReport = []

    if ipoStatus[2]:
        for data in ipoStatus[2]:
            report = []
            tr = tr + trStart
            if len(data) == 5:
                i = 0
                for text in data:
                    if i == 0:
                        companyName = text
                        report.append(companyName)
                        tr = tr + tdStart + companyName + tdEnd

                    elif i == 1:
                        i += 1
                        continue

                    elif i == 2:
                        symbol = text.split("(")[1].split(")")[0]
                        report.append(symbol)
                        tr = tr + tdStart + symbol + tdEnd
                        temp = text.split(" ")
                        listedFor = temp[1] + " " + temp[2]

                    elif i == 3:
                        listedAs = text
                        tr = tr + tdStart + listedAs + tdEnd
                        report.append(listedAs)
                        tr = tr + tdStart + listedFor + tdEnd
                        report.append(listedFor)

                    elif i == 4:
                        type = text
                        report.append(type)
                        tr = tr + tdStart + type + tdEnd + trEnd

                    i += 1
                automationReport.append(report)


            elif len(data) == 6:
                i = 0
                for text in data:
                    if i == 0:
                        companyName = text
                        report.append(companyName)
                        tr = tr + tdStart + companyName + tdEnd

                    elif i == 1:
                        i += 1
                        continue
                    elif i == 2:
                        symbol = text.split("(")[1].split(")")[0]
                        report.append(symbol)
                        tr = tr + tdStart + symbol + tdEnd

                    elif i == 3:
                        listedAs = text.split(" ")[0]
                        report.append(listedAs)
                        tr = tr + tdStart + listedAs + tdEnd

                    elif i == 4:
                        listedFor = text.split("(")[1].split(")")[0]
                        report.append(listedFor)
                        tr = tr + tdStart + listedFor + tdEnd

                    elif i == 5:
                        type = text
                        report.append(type)
                        tr = tr + tdStart + type + tdEnd

                    i += 1
                automationReport.append(report)

    print("Automation Report: ", automationReport)

    body = f"""
    <html>
        <body style="font-family: Arial, sans-serif; background-color:#f5f5f5; padding:20px;">

        
        <div style="max-width:600px; margin:auto; background:#ffffff; padding:20px; border-radius:8px;">
                
            <p><b>Hi there,<br><br>
            Good News! there {message} issued to be applied.</b></p>
            
            <h2 style="color:#2563eb;">Primary Shares Listing Status</h2>
        
            <table width="100%" cellpadding="10" cellspacing="0"
                   style="border-collapse:collapse; font-size:14px; text-align:center;">
        
                <tr style="background-color:#e5e7eb;">
                    <th rowspan="2" style="border:1px solid #000;">Company Name</th>
                    <th rowspan="2" style="border:1px solid #000;">Symbol</th>
                    <th colspan="2" style="border:1px solid #000;">Listed</th>
                    <th rowspan="2" style="border:1px solid #000;">Type</th>
                </tr>
        
                <tr style="background-color:#f3f4f6;">
                    <th style="border:1px solid #000;">as:</th>
                    <th style="border:1px solid #000;">for:</th>
                </tr>
                
                {tr}
        
            </table>
        
            <p style="margin-top:20px;"><strong>
                You can login to your meroshare account and apply for the listed shares.<br>
                https://meroshare.cdsc.com.np/#/login<br><br>
                Wishing you a very good luck! 🤞<br><br>
                <b>Regards,</b><br>
                Dhiraj Dhungana<br>
                Developer of this automated system.
            </strong></p>
        
        </div>
        
        </body>
    </html>""" if ipoStatus[1] > 0 else """
    <html>
        <body style="font-family: Arial, sans-serif; background-color:#f5f5f5; padding:20px;">

        
        <div style="max-width:600px; margin:auto; background:#ffffff; padding:20px; border-radius:8px;">
                
            <p>Hi there,<br><br>
            Unfortunately there are no IPO has been issued currently.<br>
            But we will be constantly looking for them and if any new IPO or other primary shares are listed you will be notified immediately as per your subscription, so that you wont miss any opportunities.</p>
        
            <h2 style="color:#2563eb;">Primary Shares Listing Status</h2>
        
            <table width="100%" cellpadding="10" cellspacing="0"
                   style="border-collapse:collapse; font-size:14px; text-align:center;">
        
                <tr style="background-color:#e5e7eb;">
                    <th rowspan="2" style="border:1px solid #000;">Company Name</th>
                    <th rowspan="2" style="border:1px solid #000;">Symbol</th>
                    <th colspan="2" style="border:1px solid #000;">Listed</th>
                    <th rowspan="2" style="border:1px solid #000;">Type</th>
                </tr>
        
                <tr style="background-color:#f3f4f6;">
                    <th style="border:1px solid #000;">as:</th>
                    <th style="border:1px solid #000;">for:</th>
                </tr>
        
                <tr>
                    <td style="border:1px solid #000;">N/A</td>
                    <td style="border:1px solid #000;">N/A</td>
                    <td style="border:1px solid #000;">N/A</td>
                    <td style="border:1px solid #000;">N/A</td>
                    <td style="border:1px solid #000;">N/A</td>
                </tr>
            </table>
        
            <p style="margin-top:20px;">
                You can login to your meroshare account and apply for the listed shares.<br>
                https://meroshare.cdsc.com.np/#/login<br><br>
                Wishing you a very good luck!<br><br>
                Regards,<br>
                <b>Dhiraj Dhungana</b><br>
                Developer of this automated system.
            </p>
        
        </div>
        
        </body>
    </html>"""

    # -------- 3. Creating the Email Format --------
    message = MIMEMultipart()
    message["From"] = your_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "html"))

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

    return automationReport