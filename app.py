"""
=============================================================================
CLOUDFORGE LAUNCHPAD
Workshop: From Code to Cloud (Build. Containerize. Deploy.)
=============================================================================
This application demonstrates how to take a simple Python web service
from localhost, containerize it with Docker, and deploy it to AWS.

STUDENT CHALLENGE ZONES:
- Level 1: Modify APP_NAME or GREETING below.
- Level 2: Customize the mission objectives in templates/index.html.
- Level 3: Set the CLOUDFORGE_ENV environment variable (e.g. export CLOUDFORGE_ENV=aws).
- Level 4: Expand the /about or /health endpoints with custom metadata.
=============================================================================
"""

import os
import socket
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# ---------------------------------------------------------------------------
# EASY STUDENT CONFIGURATION (Level 1 Challenge)
# ---------------------------------------------------------------------------
APP_NAME = "CloudForge"
GREETING = "Hello from CloudForge!"
TAGLINE = "Build. Containerize. Deploy."
WORKSHOP_TITLE = "CLOUDFORGE: FROM CODE TO CLOUD"


# ---------------------------------------------------------------------------
# CORE APPLICATION ROUTES
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """
    Renders the CloudForge Launchpad dashboard.
    Demonstrates reading environment variables and system context.
    """
    # Read environment variable with a safe fallback to 'local'
    current_env = os.environ.get("CLOUDFORGE_ENV", "local")
    app_mode = os.environ.get("CLOUDFORGE_MODE", "Workshop")
    
    # Safe host/container detection for educational display
    try:
        hostname = socket.gethostname()
    except Exception:
        hostname = "unknown-host"

    return render_template(
        "index.html",
        app_name=APP_NAME,
        greeting=GREETING,
        tagline=TAGLINE,
        workshop_title=WORKSHOP_TITLE,
        environment=current_env,
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
    # Returns the exact string requested for the AWS deployment demonstration
    return "Application is healthy", 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.route("/about")
def about():
    """
    Returns information about the CloudForge educational workshop.
    Supports both HTML browser viewing and JSON API clients.
    """
    current_env = os.environ.get("CLOUDFORGE_ENV", "local")
    
    # If a JSON client or curl asks with Accept: application/json or query param ?format=json
    if request.headers.get("Accept") == "application/json" or request.args.get("format") == "json":
        return jsonify({
            "application": APP_NAME,
            "workshop": WORKSHOP_TITLE,
            "purpose": "Demonstrate the journey from local development to containerized deployment on AWS.",
            "pipeline": ["Code", "Container", "AWS", "Internet"],
            "environment": current_env,
            "version": "1.0.0"
        })
    
    return render_template(
        "about.html",
        app_name=APP_NAME,
        workshop_title=WORKSHOP_TITLE,
        environment=current_env
    )


# ---------------------------------------------------------------------------
# APPLICATION ENTRYPOINT
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # CRITICAL FOR DOCKER & AWS EC2:
    # Must bind to 0.0.0.0 so the container and cloud host accept external traffic.
    # Port 5000 is our standard workshop port.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
