from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Database connection
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='yourpassword',
        database='motivio',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def home():
    return "Motivio Backend"

if __name__ == '__main__':
    app.run(debug=True)