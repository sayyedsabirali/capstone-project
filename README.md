Sentiment Analysis MLOps Project
🎯 Project Purpose
This project predicts the sentiment of a given text input as either Positive or Negative.

📝 Project Overview
This project is designed to learn and integrate key MLOps concepts, including DVC, MLflow, AWS, Docker, Kubernetes, Prometheus, and Grafana. Users can input text through a Flask web interface, and the machine learning model will predict the sentiment. The project demonstrates a complete end-to-end deployment pipeline, from local development to a monitored cloud deployment on Amazon EKS.

🛠️ Technologies Used
Programming Language: Python 3.11.4

Libraries & Tools: Pandas, NLTK, Flask, DVC, MLflow, Prometheus, Grafana

Deployment & Infrastructure: Docker, Kubernetes, AWS (EKS, S3, ECR)

📁 Project Structure
.
├── flask_app/         # Flask application source code
├── src/               # ML source code (data ingestion, preprocessing, modeling, evaluation)
├── tests/             # Test scripts for CI/CD
├── scripts/           # Utility scripts
├── .github/workflows/ # CI/CD pipeline configuration
├── dvc.yaml           # DVC pipeline definition
├── params.yaml        # Pipeline parameters
└── requirements.txt   # Python dependencies

🚀 Installation & Prerequisites
Clone the repository:

git clone <your-repository-url>

Create a virtual environment:

python -m venv atlas

Activate the environment:

# On Windows
atlas\Scripts\activate
# On macOS/Linux
source atlas/bin/activate

Install dependencies:

pip install -r requirements.txt

Prerequisites: Ensure Docker, Kubernetes (kubectl), and AWS CLI are installed and configured on your system.

⚙️ Setup Workflow
1. Project Initialization
Use the Cookiecutter Data Science template.

Rename src.models to src.model.

Initialize git: git add . && git commit -m "Initial commit" && git push

2. MLflow & DVC Setup
Connect the repository with DagsHub for experiment tracking.

Install packages: pip install dagshub mlflow.

Run experiments and track metrics using MLflow.

Initialize DVC: dvc init, and configure local/remote storage.

Create the DVC pipeline using dvc.yaml and params.yaml.

Reproduce the pipeline: dvc repro.

3. Flask Application
Create the flask_app/ directory and add your app.py file.

Run locally:

python flask_app/app.py

4. Docker Setup
Generate requirements.txt for Docker: pipreqs . --force.

Build the Docker image:

docker build -t capstone-app:latest .

Run the Docker container:

docker run -p 8888:5000 -e CAPSTONE_TEST=<your_token> capstone-app:latest

5. AWS & CI/CD Integration
Set up AWS credentials and create necessary resources: S3 bucket, ECR repository.

Push the Docker image to ECR.

Configure the GitHub Actions CI/CD pipeline for automated deployment.

6. Kubernetes (EKS) Deployment
Install kubectl and eksctl.

Create the EKS cluster:

eksctl create cluster --name flask-app-cluster --region us-east-1 ...

Deploy the application via the CI/CD pipeline and verify pods, services, and the external IP.

7. Monitoring with Prometheus & Grafana
Launch EC2 instances for Prometheus & Grafana.

Configure Prometheus to scrape metrics from the Flask application.

Add Prometheus as a data source in Grafana and create monitoring dashboards.

▶️ Running the Application
Locally:

python flask_app/app.py

On Kubernetes:

Apply the deployment configuration:

kubectl apply -f deployment.yaml

Get the external IP of the service:

kubectl get svc

Access the application in your browser at http://<external-ip>:5000

✨ Features
User text input for sentiment prediction (Positive / Negative).

End-to-end MLOps integration with DVC, MLflow, AWS, Docker, and Kubernetes.

Monitoring dashboards with Prometheus & Grafana.

Automated CI/CD pipeline for deployment.

🎬 Demo
A demo video showcasing the project workflow is available here:
Watch Project Demo
