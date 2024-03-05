# !/bin/sh

echo "Applying the deployments and services"

kubectl apply -f ../redis/redis-deployment.yaml
kubectl apply -f ../redis/redis-service.yaml
kubectl apply -f ../fastapi-app/fastapi-deployment.yaml
kubectl apply -f ../fastapi-app/fastapi-service.yaml

echo "Getting Services"
kubectl get svc fastapi-app