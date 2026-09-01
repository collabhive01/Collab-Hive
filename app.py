from flask import Flask, render_template, request
import os
import resend

app = Flask(__name__)

resend.api_key = os.environ.get("RESEND_API_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name", "")
    email = request.form.get("email", "")
    company = request.form.get("company", "")
    message = request.form.get("message", "")

    try:

        params = {
            "from": "Collab Hive <onboarding@resend.dev>",
            "to": ["collab.hive01@gmail.com"],
            "subject": f"New Collab Hive Inquiry from {name}",
            "reply_to": email,
            "html": f"""
                <h2>New Collab Hive Inquiry</h2>

                <p><strong>Name:</strong> {name}</p>

                <p><strong>Email:</strong> {email}</p>

                <p><strong>Brand / Company:</strong> {company}</p>

                <h3>Message</h3>

                <p>{message}</p>

                <hr>

                <p>Sent from Collab Hive website</p>
            """
        }

        resend.Emails.send(params)

        success = "Thank you! Your inquiry has been sent successfully."

    except Exception as e:

        print("RESEND ERROR:", e)

        success = "Something went wrong. Please try again."

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
