from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import os


app = Flask(__name__)
CORS(app)  # Allow React frontend to fetch data

@app.route('/')
def home():
    return 'Backend is working!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
