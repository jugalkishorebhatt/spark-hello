Start Spark Master and Worker services:

kubectl create -f ./kubernetes/spark-master-deployment.yaml
kubectl create -f ./kubernetes/spark-master-service.yaml

Enable Ingress addons:

minikube addons enable ingress

Start ingress service

kubectl apply -f ./kubernetes/minikube-ingress.yaml
