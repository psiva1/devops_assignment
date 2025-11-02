from flask import Flask, jsonify
import os
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Response

app = Flask(__name__)

# Prometheus counter to track number of requests to /get_info
REQUEST_COUNTER = Counter("get_info_requests_total", "Total number of requests to /get_info")

@app.route("/get_info", methods=["GET"])
def get_info():
    REQUEST_COUNTER.inc()
    return jsonify({
        "APP_VERSION": os.getenv("APP_VERSION", "1.0"),
        "APP_TITLE": os.getenv("APP_TITLE", "Devops Assignment 2024MT03585")
    })

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
