from flask import Flask, render_template, redirect, url_for
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Path to the CSV file where clicks will be stored
CLICK_LOG_FILE = 'click_log.csv'

# Ensure the CSV file exists
if not os.path.isfile(CLICK_LOG_FILE):
    with open(CLICK_LOG_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'link_clicked', 'timestamp'])  # CSV Header


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/track_click/<link>')
def track_click(link):
    # If you want to track users, you can include user_id from session or cookies.
    # For simplicity, we'll set user_id to None (or a random number for now).
    user_id = None
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log the click in the CSV file
    with open(CLICK_LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, link, timestamp])

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
