from flask import Flask, request, jsonify
import time
import logging

logging.basicConfig(filename="requests.log", level=logging.INFO)

app = Flask(__name__)

# In-memory log: {IP: [timestamps]}
request_log = {}

# Rate limit settings
MAX_REQUESTS = 5
WINDOW_SECONDS = 60

@app.before_request
def rate_limiter():
    ip = request.remote_addr
    now = time.time()

    # Get the list of previous request times
    timestamps = request_log.get(ip, [])

    # Keep only timestamps within the window
    timestamps = [t for t in timestamps if now - t < WINDOW_SECONDS]

    if len(timestamps) >= MAX_REQUESTS:
        return jsonify({"error": "⛔ Rate limit exceeded"}), 429

    # Add current timestamp and save back
    timestamps.append(now)
    request_log[ip] = timestamps

@app.route("/api/data")
def data():
    return jsonify({"message": "✅ You are within the limit!"})

@app.after_request
def log_request(response):
    ip = request.remote_addr
    route = request.path
    status = response.status_code
    logging.info(f"{ip} {route} {status} {time.ctime()}")
    return response

if __name__ == "__main__":
    app.run(debug=True)
