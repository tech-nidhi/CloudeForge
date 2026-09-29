# ☁️ CloudForge Launchpad

> **CLOUDFORGE: FROM CODE TO CLOUD**  
> *Build. Containerize. Deploy.*

Welcome to **CloudForge Launchpad**, an educational web application designed for hands-on cloud workshops. This project teaches students and aspiring cloud architects how to take a simple web application from local development, package it inside a Docker container, and deploy it onto Amazon Web Services (AWS).

---

## 📁 Project Structure

```text
cloudforge-demo/
├── app.py              # Main Flask server and routes (0.0.0.0:5000)
├── requirements.txt    # Minimal Python dependencies (Flask)
├── Dockerfile          # Container specification
├── README.md           # Workshop instructions & mini-challenges
└── templates/
    ├── index.html      # CloudForge Launchpad dashboard
    └── about.html      # Workshop overview page
```

---

## 🚀 1. Run Locally (Localhost)

### Step 1: Install Dependencies
Ensure you have Python 3 installed, then install dependencies:
```bash
pip install -r requirements.txt
```

### Step 2: Start the Application
Run the Flask server:
```bash
python app.py
```

### Step 3: Open in Browser
Open your web browser and navigate to:
```text
http://localhost:5000
```

---

## 💓 2. Test Endpoints

You can verify the endpoints using your browser or via terminal:

| Endpoint | Method | Purpose | Example Response |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | Main Launchpad Dashboard | HTML UI |
| `/health` | `GET` | Health Check (Used by AWS Load Balancers) | `Application is healthy` |
| `/about` | `GET` | Workshop Details & Mission Info | HTML Page or JSON (`?format=json`) |

### Terminal Test Commands:
```bash
# Test health check
curl -i http://localhost:5000/health

# Test about endpoint (JSON output)
curl -s http://localhost:5000/about?format=json
```

---

## 🐳 3. Containerize with Docker

### Step 1: Build the Docker Image
```bash
docker build -t cloudforge-app .
```

### Step 2: Run the Docker Container
Map port `5000` from the container to your host machine:
```bash
docker run -d -p 5000:5000 --name cloudforge-demo cloudforge-app
```

Now open `http://localhost:5000` to see your containerized app live!

To stop the container:
```bash
docker stop cloudforge-demo
docker rm cloudforge-demo
```

---
## 🎯 4. Mini Challenge Ideas for Students

Test your skills by customizing the application:

- **Level 1 (Beginner):** Open `app.py` and modify `APP_NAME` or `GREETING` to your personal handle or team name.
- **Level 2 (Styling & Content):** Open `templates/index.html` and add new mission ideas or customize the color scheme.
- **Level 3 (Environment Config):** Pass `CLOUDFORGE_ENV=production` when launching the Docker container.
- **Level 4 (New Endpoint):** Add a `/status` or `/author` route in `app.py` that returns your name and student ID in JSON.

---

## 🛡️ Important Technical Notes

- **Network Binding:** Flask is configured to bind to `0.0.0.0` (all network interfaces) so that Docker port mappings and AWS EC2 inbound security group rules can route external internet traffic properly.
- **No External Dependencies:** Requires no databases, API keys, or cloud SDKs.
