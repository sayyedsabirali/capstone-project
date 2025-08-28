# Sentiment Analysis MLOps Project

## 🎯 Project Purpose
This project predicts the sentiment of a given text input as either **Positive** or **Negative**.

---

## 📝 Project Overview
This project is designed to learn and integrate key MLOps concepts, including **DVC, MLflow, AWS, Docker, Kubernetes, Prometheus, and Grafana**. Users can input text through a Flask web interface, and the machine learning model will predict the sentiment. The project demonstrates a complete end-to-end deployment pipeline, from local development to a monitored cloud deployment on Amazon EKS.

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.11.4
* **Libraries & Tools:** Pandas, NLTK, Flask, DVC, MLflow, Prometheus, Grafana
* **Deployment & Infrastructure:** Docker, Kubernetes, AWS (EKS, S3, ECR)

---

## 📁 Project Structure
```
.
├── flask_app/         # Flask application source code
├── src/               # ML source code (data ingestion, preprocessing, modeling, evaluation)
├── tests/             # Test scripts for CI/CD
├── scripts/           # Utility scripts
├── .github/workflows/ # CI/CD pipeline configuration
├── dvc.yaml           # DVC pipeline definition
├── params.yaml        # Pipeline parameters
└── requirements.txt   # Python dependencies
```

---

## 🚀 Installation & Prerequisites
1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv atlas
    ```
3.  **Activate the environment:**
    ```bash
    # On Windows
    atlas\Scripts\activate
    
    # On macOS/Linux
    source atlas/bin/activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Prerequisites:** Ensure **Docker**, **Kubernetes (kubectl)**, and **AWS CLI** are installed and configured on your system.

---

## ⚙️ Setup Workflow

### 1. Project Initialization
* Use the Cookiecutter Data Science template.
* Rename `src.models` to `src.model`.
* Initialize git: `git add . && git commit -m "Initial commit" && git push`

### 2. MLflow & DVC Setup
* Connect the repository with DagsHub for experiment tracking.
* Install packages: `pip install dagshub mlflow`.
* Run experiments and track metrics using MLflow.
* Initialize DVC: `dvc init`, and configure local/remote storage.
* Create the DVC pipeline using `dvc.yaml` and `params.yaml`.
* Reproduce the pipeline: `dvc repro`.

### 3. Flask Application
* Create the `flask_app/` directory and add your `app.py` file.
* Run locally:
    ```bash
    python flask_app/app.py
    ```

### 4. Docker Setup
* Generate `requirements.txt` for Docker: `pipreqs . --force`.
* Build the Docker image:
    ```bash
    docker build -t capstone-app:latest .
    ```
* Run the Docker container:
    ```bash
    docker run -p 8888:5000 -e CAPSTONE_TEST=<your_token> capstone-app:latest
    ```

---

## ▶️ Running the Application

* **Locally:**
    ```bash
    python flask_app/app.py
    ```
* **On Kubernetes:**
    1.  Apply the deployment configuration:
        ```bash
        kubectl apply -f deployment.yaml
        ```
    2.  Get the external IP of the service:
        ```bash
        kubectl get svc
        ```
    3.  Access the application in your browser at `http://<external-ip>:5000`

---

## ✨ Features
* User text input for sentiment prediction (Positive / Negative).
* End-to-end MLOps integration with DVC, MLflow, AWS, Docker, and Kubernetes.
* Monitoring dashboards with Prometheus & Grafana.
* Automated CI/CD pipeline for deployment.

---

## 🎬 Demo
A demo video showcasing the project workflow is available here:
[**Watch Project Demo**](https://drive.google.com/file/d/1Y40cqSpgU7lBtoBCWcZZtTtaXM1H0hFg/view?usp=drive_link)
