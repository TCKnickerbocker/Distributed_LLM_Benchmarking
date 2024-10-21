# LLM API with Docker and Kubernetes
## Thomas Knickerbocker, Owen Ratgen

This project provides an API for generating text using a language model (e.g., GPT-2), containerized with Docker and deployable on Kubernetes.

## Features
- API built with FastAPI to expose the model
- Dockerfile for containerization
- Kubernetes manifests for deployment

## How to Run
docker run -p 8000:8000 llm-app

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
curl http://<node-ip>:30001/generate/ -X POST -d '{"prompt": "Hello"}'


### Docker

1. Build the Docker image:
   ```bash
   docker build -t llm-app .
   docker run -p 8000:8000 llm-app
#### Build and push to dockerhub:
docker tag llm-app your_dockerhub_user/llm-app:latest
docker push your_dockerhub_user/llm-app:latest

#### Deploy to Kubernetes:
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

### Next Steps
- **Build and Test the Docker Container:**
  ```bash
  docker build -t llm-app .
  docker run -p 8000:8000 llm-app