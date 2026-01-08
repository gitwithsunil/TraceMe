import subprocess
import os

def run_holehe(email):
    try:
        result = subprocess.run(
            ["holehe", email],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.stdout
    except Exception as e:
        return f"[holehe ERROR] {e}"

def run_sherlock(username):
    try:
        sherlock_path = os.path.expanduser("~/Documents/kalivscode/traceme/sherlock")
        result = subprocess.run(
            ["python3", "-m", "sherlock_project", username, "--print-found"],
            capture_output=True,
            text=True,
            cwd=sherlock_path,
            timeout=120
        )
        return result.stdout
    except Exception as e:
        return f"[sherlock ERROR] {e}"

def extract_username(email):
    return email.split("@")[0]
