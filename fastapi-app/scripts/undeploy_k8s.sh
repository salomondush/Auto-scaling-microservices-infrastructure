kubectl delete -f ../k8s/components.yaml

kubectl delete -f ../k8s/redis-deployment.yaml
kubectl delete -f ../k8s/redis-service.yaml
kubectl delete -f ../k8s/huey-consumer-deployment.yaml

kubectl delete -f ../k8s/fastapi-deployment.yaml
kubectl delete -f ../k8s/fastapi-service.yaml

kubectl delete hpa fastapi-deployment
kubectl delete hpa huey-consumer-deployment

