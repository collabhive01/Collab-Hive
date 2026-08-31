from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name")
    email = request.form.get("email")
    company = request.form.get("company")
    message = request.form.get("message")

    print("\n==============================")
    print("      NEW CONTACT INQUIRY")
    print("==============================")
    print("Name:", name)
    print("Email:", email)
    print("Company:", company)
    print("Message:", message)
    print("==============================\n")

    return render_template(
        "index.html",
        success="Thank you! Your inquiry has been received."
    )


if __name__ == "__main__":
    app.run(debug=True)