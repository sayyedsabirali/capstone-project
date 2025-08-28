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

## ⚙️ End-to-End Setup Workflow
This section provides a detailed walkthrough from project initialization to deployment and monitoring.

### 1. Project Setup & Initialization
First, create a GitHub repository and clone it locally. Set up a Python virtual environment to manage dependencies.
```bash
# Create a virtual environment
python -m venv atlas

# Activate the environment (Windows)
atlas\Scripts\activate
```
Use the Cookiecutter Data Science template to establish a standard project structure. After renaming a source folder for clarity, make your initial Git commit.
```bash
# Initialize project from template
cookiecutter -c v1 [https://github.com/drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)

# Make the initial commit
git add .
git commit -m "Initial commit"
git push
```

### 2. MLflow & DVC Configuration
Connect your repository to DagsHub for experiment tracking with MLflow. Install the necessary packages.
```bash
pip install dagshub mlflow
```
Initialize DVC to version control your data. For local development, you can set up a temporary local remote.
```bash
# Initialize DVC
dvc init

# Add a local remote for testing
dvc remote add -d mylocal local_s3
```
Define your ML pipeline stages in `dvc.yaml` and parameters in `params.yaml`. Once configured, you can reproduce the entire pipeline with a single command.
```bash
# Run the pipeline
dvc repro
```
For production, configure AWS S3 as your remote storage. Install the required libraries and configure your AWS credentials.
```bash
# Install AWS support for DVC
pip install dvc[s3] awscli

# Configure your AWS user credentials
aws configure

# Add S3 as a remote
dvc remote add -d myremote s3://<your-bucket-name>
```

### 3. Flask App & Dockerization
Develop the Flask application inside the `flask_app` directory. Before building the app, push your DVC-tracked data to S3.
```bash
dvc push
```
Generate a `requirements.txt` file specifically for the Flask app. Then, create a `Dockerfile` to containerize the application.
```bash
# Generate requirements for the app
pipreqs . --force

# Build the Docker image
docker build -t capstone-app:latest .
```
Run the container locally to test it, making sure to pass the required environment variables.
```bash
# Run the Docker container
docker run -p 8888:5000 -e CAPSTONE_TEST=<your_dagshub_token> capstone-app:latest
```

### 4. CI/CD and AWS Integration
Create a CI/CD workflow file at `.github/workflows/ci.yaml`. Add your AWS and DagsHub credentials as secrets in your GitHub repository settings. The pipeline will automatically build the Docker image and push it to a pre-configured Amazon ECR repository on every push to the main branch.

### 5. Kubernetes (EKS) Deployment
Before deploying, you need `kubectl` and `eksctl` installed on your machine. Create your EKS cluster with a managed node group.
```bash
# Create an EKS cluster
eksctl create cluster --name flask-app-cluster --region us-east-1 --nodegroup-name flask-app-nodes --node-type t3.small --nodes 1
```
Configure `kubectl` to connect to your new cluster.
```bash
# Update kubeconfig to connect to the new cluster
aws eks --region us-east-1 update-kubeconfig --name flask-app-cluster
```
Verify that your cluster is running and accessible.
```bash
# Check node status
kubectl get nodes
```
The CI/CD pipeline will then apply the `deployment.yaml` to deploy the application. Once deployed, get the external IP of the LoadBalancer to access it.
```bash
# Get the service's external IP
kubectl get svc flask-app-service
```

### 6. Monitoring Setup (Prometheus & Grafana)

#### Prometheus Server Setup
Launch an Ubuntu EC2 instance (t3.medium recommended), allowing inbound traffic on ports `9090` (Prometheus UI) and `22` (SSH). SSH into the instance and run the following commands.
```bash
# Download and extract Prometheus
wget [https://github.com/prometheus/prometheus/releases/download/v2.46.0/prometheus-2.46.0.linux-amd64.tar.gz](https://github.com/prometheus/prometheus/releases/download/v2.46.0/prometheus-2.46.0.linux-amd64.tar.gz)
tar -xvzf prometheus-2.46.0.linux-amd64.tar.gz

# Move files to a standard path
sudo mv prometheus-2.46.0.linux-amd64 /etc/prometheus
```
Configure `/etc/prometheus/prometheus.yml` to scrape your Flask app's metrics endpoint.
```yaml
scrape_configs:
  - job_name: "flask-app"
    static_configs:
      - targets: ["<your-eks-loadbalancer-ip>:5000"]
```
Finally, run the Prometheus server.
```bash
/usr/local/bin/prometheus --config.file=/etc/prometheus/prometheus.yml
```

#### Grafana Server Setup
Launch another Ubuntu EC2 instance, allowing inbound traffic on ports `3000` (Grafana UI) and `22` (SSH). SSH into the instance and install Grafana.
```bash
# Download and install Grafana
wget [https://dl.grafana.com/oss/release/grafana_10.1.5_amd64.deb](https://dl.grafana.com/oss/release/grafana_10.1.5_amd64.deb)
sudo apt install ./grafana_10.1.5_amd64.deb -y
```
Start and enable the Grafana service to run on boot.
```bash
# Start and enable the Grafana service
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```
Access the Grafana UI at `http://<grafana-ec2-ip>:3000`. Add Prometheus as a data source using its IP (`http://<prometheus-ec2-ip>:9090`) and start building dashboards.


## ✨ Features
* User text input for sentiment prediction (Positive / Negative).
* End-to-end MLOps integration with DVC, MLflow, AWS, Docker, and Kubernetes.
* Monitoring dashboards with Prometheus & Grafana.
* Automated CI/CD pipeline for deployment.

---

## 🎬 Demo
A demo video showcasing the project workflow is available here:
[**Watch Project Demo**](https://drive.google.com/file/d/1Y40cqSpgU7lBtoBCWcZZtTtaXM1H0hFg/view?usp=drive_link)
