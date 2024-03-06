# !/bin/sh

echo "Applying the deployments and services"

kubectl apply -f ../k8s/redis-deployment.yaml
kubectl apply -f ../k8s/redis-service.yaml

kubectl apply -f ../k8s/huey-consumer-deployment.yaml
# kubectl apply -f ../k8s/huey-consumer-hpa.yaml
kubectl autoscale deployment huey-consumer-deployment --cpu-percent=50 --min=1 --max=4

kubectl apply -f ../k8s/fastapi-deployment.yaml
kubectl apply -f ../k8s/fastapi-service.yaml
# kubectl apply -f ../k8s/fastapi-hpa.yaml
kubectl autoscale deployment fastapi-deployment --cpu-percent=50 --min=1 --max=4

kubectl apply -f ../k8s/components.yaml
