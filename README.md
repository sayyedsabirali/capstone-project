# Sentiment Analysis MLOps Project

**Project Purpose:**  
Predicts the sentiment of text input as **Positive** or **Negative**.

---

## Project Overview
This project is designed to **learn and integrate MLOps concepts** such as **DVC, MLflow, AWS, Docker, Kubernetes, Prometheus, Grafana**, and experiment tracking. Users input text, and the ML model predicts sentiment via a **Flask web interface**. The project also demonstrates an end-to-end deployment pipeline from local development to cloud deployment on EKS with monitoring.

---

## Technologies Used
- **Programming Language:** Python 3.11.4  
- **Libraries & Tools:** Pandas, NLTK, Flask, DVC, MLflow, Prometheus, Grafana  
- **Deployment & Infrastructure:** Docker, Kubernetes, AWS (EKS, S3, ECR)  

---

## Project Structure
flask_app/ # Flask application
src/ # Source code (data ingestion, preprocessing, modeling, evaluation)
dvc.yaml # DVC pipeline
params.yaml # Pipeline parameters
requirements.txt # Python dependencies
tests/ # Test scripts for CI/CD
scripts/ # Utility scripts
.github/workflows/ # CI/CD pipeline configuration

yaml
Copy code

---

## Installation & Prerequisites
1. Clone the repository.  
2. Create a virtual environment:  
```bash
python -m venv atlas
```
Activate the environment:

```bash
atlas\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Ensure Docker, Kubernetes, and AWS CLI are installed and configured.

Setup Workflow
1. Project Initialization
Use Cookiecutter Data Science template.

Rename src.models to src.model.

Initialize git: git add . && git commit -m "Initial commit" && git push.

2. MLflow & DVC Setup
Connect repository with Dagshub for experiment tracking.

Install packages: pip install dagshub mlflow.

Run experiments and track metrics using MLflow.

Initialize DVC: dvc init, configure local/remote storage.

Create DVC pipeline using dvc.yaml and params.yaml.

Reproduce pipeline: dvc repro.

3. Flask Application
Create flask_app/ directory and add app file.

Run locally:

bash
```
python flask_app/app.py
```
4. Docker Setup
Generate requirements for Docker: pipreqs . --force.

Build Docker image:

bash
```
docker build -t capstone-app:latest .
```
Run Docker container:
```bash
docker run -p 8888:5000 -e CAPSTONE_TEST=<token> capstone-app:latest
```
5. AWS & CI/CD Integration
Set up AWS credentials and create resources: S3 bucket, ECR repository.

Push Docker image to ECR.

Configure GitHub Actions CI/CD pipeline for automated deployment.

6. Kubernetes (EKS) Deployment
Install kubectl and eksctl.

Create EKS cluster:

```bash
eksctl create cluster --name flask-app-cluster --region us-east-1 ...
```
Deploy app via CI/CD and verify pods, services, and external IP.

7. Monitoring with Prometheus & Grafana
Launch EC2 instances for Prometheus & Grafana.

Configure Prometheus to scrape Flask app metrics.

Add Prometheus as a data source in Grafana and create dashboards.

Running the Application
Locally:

bash
```
python flask_app/app.py
```
On Kubernetes:

```bash
kubectl apply -f deployment.yaml
```
8. Get external-ip
```bash
kubectl get svc
```
Access external URL: http://<external-ip>:5000

Demo
A demo video showcasing the project workflow can be added here:
[https://drive.google.com/file/d/1Y40cqSpgU7lBtoBCWcZZtTtaXM1H0hFg/view?usp=drive_link]

Features
User text input sentiment prediction (Positive / Negative)

End-to-end MLOps integration with DVC, MLflow, AWS, Docker, Kubernetes

Monitoring dashboards with Prometheus & Grafana

CI/CD pipeline for automated deployment
