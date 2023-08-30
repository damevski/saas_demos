from flask import Flask, jsonify
from flask_httpauth import HTTPDigestAuth
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'UNguessable'
auth = HTTPDigestAuth()

USERS = {
    "rodney": "go_rams"
}

stopwatch_running = False
start_time = None
elapsed_time = 0

@auth.get_password
def get_pw(username):
    if username in USERS:
        return USERS.get(username)
    return None


@app.route('/start', methods=['GET'])
@auth.login_required
def start_stopwatch():
    global stopwatch_running, start_time
    if not stopwatch_running:
        stopwatch_running = True
        start_time = time.time()
    return "Stopwatch started!", 200

@app.route('/stop', methods=['GET'])
@auth.login_required
def stop_stopwatch():
    global stopwatch_running
    if stopwatch_running:
        elapsed_time = time.time() - start_time
        stopwatch_running = False
        return jsonify({"elapsed_time": elapsed_time}), 200
    else:
        return 'Stopwatch not started!', 400

if __name__ == '__main__':
    app.run(debug=True)
