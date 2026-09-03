from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "collab-hive-secret-key"

ENQUIRY_FILE = "enquiries.csv"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/enquire", methods=["POST"])
def enquire():
    name = request.form.get("name", "").strip()
    brand = request.form.get("brand", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    campaign = request.form.get("campaign", "").strip()
    budget = request.form.get("budget", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not brand or not email or not message:
        flash("Please fill all required fields.", "error")
        return redirect(url_for("home") + "#contact")

    file_exists = os.path.exists(ENQUIRY_FILE)

    with open(
        ENQUIRY_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Name",
                "Brand",
                "Email",
                "Phone",
                "Campaign",
                "Budget",
                "Message"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            name,
            brand,
            email,
            phone,
            campaign,
            budget,
            message
        ])

    flash(
        "Thanks! Your campaign enquiry has been received.",
        "success"
    )

    return redirect(url_for("home") + "#contact")


if __name__ == "__main__":
    app.run(debug=True)