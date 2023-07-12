from flask import Flask, jsonify, request, render_template, send_from_directory
import os

app = Flask(__name__,  static_folder='static')

@app.route('/', methods =["GET", "POST"])
def index():
    return render_template("popmox.html")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
