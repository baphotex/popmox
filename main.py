from flask import Flask, jsonify, request, render_template, send_from_directory
import os
import app.py 

app = Flask(__name__,  static_folder='static')

@app.route('/', methods =["GET", "POST"])
def index():
    return render_template("rox_2.html")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
