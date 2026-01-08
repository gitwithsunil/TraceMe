from flask import Blueprint, render_template, request
from app.tools import run_holehe, run_sherlock, extract_username

main = Blueprint("main", __name__, template_folder="../templates")

def format_output(raw_output):
    if not raw_output:
        return []
    lines = raw_output.splitlines()
    return [line for line in lines if '[+]' in line or 'https://' in line]

@main.route("/", methods=["GET", "POST"])
def index():
    email = ""
    holehe_result = []
    sherlock_result = []

    if request.method == "POST":
        email = request.form["email"]
        username = extract_username(email)

        holehe_raw = run_holehe(email)
        sherlock_raw = run_sherlock(username)

        holehe_result = format_output(holehe_raw)
        sherlock_result = format_output(sherlock_raw)

    return render_template("index.html", holehe=holehe_result, sherlock=sherlock_result, email=email)
