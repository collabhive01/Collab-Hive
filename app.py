from flask import Flask, render_template, request
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name", "")
    email = request.form.get("email", "")
    company = request.form.get("company", "")
    message = request.form.get("message", "")

    msg = EmailMessage()

    msg["Subject"] = f"New Collab Hive Inquiry from {name}"
    msg["From"] = os.environ.get("GMAIL_EMAIL")
    msg["To"] = "collabhive01@gmail.com"
    msg["Reply-To"] = email

    msg.set_content(
        f"""
NEW COLLAB HIVE INQUIRY
=======================

Name: {name}
Email: {email}
Brand / Company: {company}

Message:
{message}

=======================
Sent from Collab Hive website
"""
    )

    try:

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(
                os.environ.get("GMAIL_EMAIL"),
                os.environ.get("GMAIL_APP_PASSWORD")
            )

            smtp.send_message(msg)

        success = "Thank you! Your inquiry has been sent successfully."

    except Exception as e:

        print("EMAIL ERROR:", e)

        success = "Something went wrong. Please contact us directly."

    return render_template(
        "index.html",
        success=success
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
