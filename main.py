import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail credentials
sender_email = "pankajsangle15@gmail.com"
app_password = "krxu kcqw yobe jcaw"  # Use 16-character App Password

# Static list of recipients
recipients = [
    ("company1", "pankajsangle2ndmail@gmail.com"),
    ("company2", "pankajsangle15@gmail.com"),
    ("company3", "dadabhau112001@gmail.com"),
    ("settleforextra", "settleforextra@gmail.com"),
    ]

recipients3 = [
    ("grazitti", "careers@grazitti.com"),
    ("zetheta", "careers@zetheta.com"),
    ("exo edge", "hr@exoedge.in"),
    ("vee healthtek", "careers@veehealthtek.com"),
    ("graymatter", "careers@graymatter.co.in"),
    ("indium software", "careers@indium.tech"),
    ("hakkoda", "careers@hakkoda.com"),
    ("softsensor.ai", "careers@softsensor.ai"),
    ("revolut", "careers@revolut.com"),
    ("atlys", "careers@atlys.com"),
    ("trimble", "careers@trimble.com"),
    ("eclerx", "careers@eclerx.com"),
    ("ion group", "careers@iongroup.com"),
    ("protium", "careers@protium.com"),
    ("checkmarx", "careers@checkmarx.com"),
    ("talentica", "careers@talentica.com"),
    ("cloudtern", "hr@cloudtern.com"),
    ("lessburn", "careers@lessburn.com"),
    ("weekday solutions", "hr@weekdaysolutions.com"),
    ("kantar", "careers@kantar.com"),
    ("irohub infotech", "jobs@irohubinfotech.com"),
    ("rajesh medical", "careers@rajeshmedical.com"),
    ("eci india", "careers@eciindia.com"),
    ("engage digital", "careers@engagedigital.com"),
    ("morningstar", "careers@morningstar.com"),
    ("livingthings.ai", "careers@livingthings.ai"),
    ("inorg global", "careers@inorgglobal.com"),
    ("ssnc", "hr@ssnc.com"),
    ("icreon", "jobs@icreon.com"),
    ("solifi", "careers@solifi.com"),
    ("arrow minds", "jobs@arrowminds.com"),
    ("green success", "careers@green-success.com"),
    ("vanja analytics", "hr@vanjaanalytics.com"),
    ("analytixlabs", "careers@analytixlabs.co.in"),
    ("fynd", "careers@fynd.com"),
    ("zyoin", "careers@zyoin.com"),
    ("data pegasus", "jobs@datapegasus.com"),
    ("bizanalytics", "careers@bizanalytics.in"),
    ("razorpay", "jobs@razorpay.com"),
    ("fresh to home", "careers@freshtohome.in"),
    ("catalyst corp", "hr@catalystcorp.com"),
    ("technomus vehicles", "careers@technomusvehicles.com"),
    ("ninjacart", "jobs@ninjacart.com"),
    ("locus", "careers@locus.sh"),
    ("urbantz", "jobs@urbantz.com"),
    ("zenoti", "careers@zenoti.com"),
    ("the big decisions", "careers@thebigdecisions.com"),
    ("educba", "jobs@educba.com"),
    ("meritnation", "careers@meritnation.com"),
    # ("upgrad", "jobs@upGrad.com")
]


# Email subject and message (personalized)
subject = "Seeking Opportunities in Data/Web Analytics "

for name, email in recipients2:
    try:
        # Create the message
        message = MIMEMultipart()
        message["From"] = f"Pankaj Sangle <{sender_email}>"
        message["To"] = email
        message["Subject"] = subject

        body = f"""\
Dear {name} Hiring Team,
I hope this message finds you well.

I'm reaching out to express my interest in any opportunities at {name} related to Data or Web Analytics.

I have over 2 years of professional experience in data and web analytics, with expertise in:
- Building scalable, dynamic interactive dashboards in Power BI
- Hands-on experience with platforms like GCP Bigquery and Tableau
- Google Analytics (GA4) and Google Tag Manager (GTM) for end-to-end tracking solutions and implementations
- Analyzing user behavior and journeys on e-commerce platforms
- Creating actionable insights using ad hoc reporting to support and speed up the decision making process


I've attached my resume for your review, and would truly appreciate it if you could consider me for any relevant openings.

Thank you for your time!

Warm regards,
Pankaj Sangle
📞 +91 9309747109
🔗 [LinkedIn] - https://www.linkedin.com/in/pankaj-b-sangle-42a483202/
📄 [Resume] - https://drive.google.com/file/d/146T7VD1TwnuShHBf7MTPbVKEGa2eGkvd/view?usp=sharing
"""
        message.attach(MIMEText(body, "plain"))

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, email, message.as_string())
            print(f"✅ Email sent to {email}")

    except Exception as e:
        print(f"❌ Failed to send email to {email}: {e}")
