from flask import Flask, render_template, jsonify, Response
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/firebase-init.js')
def firebase_init():
    js = f"""
firebase.initializeApp({{
  apiKey:            "{os.getenv('FIREBASE_API_KEY')}",
  authDomain:        "{os.getenv('FIREBASE_AUTH_DOMAIN')}",
  projectId:         "{os.getenv('FIREBASE_PROJECT_ID')}",
  storageBucket:     "{os.getenv('FIREBASE_STORAGE_BUCKET')}",
  messagingSenderId: "{os.getenv('FIREBASE_MESSAGING_SENDER_ID')}",
  appId:             "{os.getenv('FIREBASE_APP_ID')}"
}});
const auth     = firebase.auth();
const provider = new firebase.auth.GoogleAuthProvider();
"""
    return Response(js, mimetype='application/javascript')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/logout', methods=['POST'])
def logout():
    return jsonify({'status': 'logged out'}), 200

if __name__ == '__main__':
    app.run(debug=True)
