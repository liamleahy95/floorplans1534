from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os

app = Flask(__name__)

# Employee data (this will be replaced with names input by the user)
employees = []

# Path to your image
image_path = "static/imagetest.png"

# Home route - displays the employee list and background image
@app.route('/')
def home():
    return render_template('index.html', employees=employees, image_path=image_path)

# Route to paste names
@app.route('/paste_names', methods=['POST'])
def paste_names():
    pasted_names = request.form['pasted_names']
    if pasted_names:
        global employees
        employees = [(name.strip(), "") for name in pasted_names.strip().splitlines()]
    return redirect(url_for('home'))

# Route to clear names
@app.route('/clear_names', methods=['POST'])
def clear_names():
    global employees
    employees = []
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
