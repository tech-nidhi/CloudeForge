"""
=============================================================================
CLOUDFORGE LAUNCHPAD
Workshop: From Code to Cloud (Build. Containerize. Deploy.)
=============================================================================
This application demonstrates how to take a simple Python web service
from localhost, containerize it with Docker, and deploy it to AWS.

STUDENT CHALLENGE ZONES:
- Level 1: Modify APP_NAME or GREETING below.
- Level 2: Add or extend the /about endpoint.
- Level 3: Set the APP_ENV environment variable (e.g. export APP_ENV=aws).
- Level 4: Deploy the containerized app to AWS EC2.
=============================================================================
"""

import os
import socket
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# ---------------------------------------------------------------------------
# 1. ENVIRONMENT VARIABLES (Level 1 & Level 3 Challenge)
# ---------------------------------------------------------------------------
APP_NAME = os.getenv("APP_NAME", "CloudForge")
APP_ENV = os.getenv("APP_ENV", os.getenv("CLOUDFORGE_ENV", "local"))
GREETING = os.getenv("GREETING", f"Hello from {APP_NAME}!")
TAGLINE = "Build. Containerize. Deploy."
WORKSHOP_TITLE = f"{APP_NAME.upper()}: FROM CODE TO CLOUD"


# ---------------------------------------------------------------------------
# CORE APPLICATION ROUTES
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """
    Renders the CloudForge Launchpad dashboard.
    Dynamically reflects APP_NAME and APP_ENV.
    """
    app_mode = os.getenv("APP_MODE", "Workshop")
    
    # Safe host/container detection for educational display
    try:
        hostname = socket.gethostname()
    except Exception:
        hostname = "unknown-host"

    return render_template(
        "index.html",
        app_name=APP_NAME,
        app_env=APP_ENV,
        greeting=GREETING,
        tagline=TAGLINE,
        workshop_title=WORKSHOP_TITLE,
        environment=APP_ENV,
        mode=app_mode,
        hostname=hostname,
    )


@app.route("/health")
def health():
    """
    Health check endpoint used by AWS Target Groups / Load Balancers
    and our frontend dashboard health monitor.
    Returns HTTP 200 OK with plain text confirmation.
    """
    return "Application is healthy", 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.route("/about")
def about():
    """
    Returns application metadata and environment info in JSON.
    """
    return jsonify({
        "app": APP_NAME,
        "description": "Built with Python + Docker",
        "environment": APP_ENV
    })


# ---------------------------------------------------------------------------
# APPLICATION ENTRYPOINT
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # CRITICAL FOR DOCKER & AWS EC2:
    # Must bind to 0.0.0.0 so the container and cloud host accept external traffic.
    # Port 5000 is our standard workshop port.
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
