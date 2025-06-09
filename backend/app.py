from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import os


app = Flask(__name__)
CORS(app)  # Allow React frontend to fetch data

@app.route('/api/data')
def get_data():
    conn = sqlite3.connect('my_database.db')
    cur = conn.cursor()
    cur.execute("SELECT time, weight, status FROM weight_data ORDER BY time ASC")
    rows = cur.fetchall()
    conn.close()
    return jsonify([{"time": r[0], "weight": r[1], "status": r[2]} for r in rows])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
