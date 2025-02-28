## Push docker image to DockerHub

1. docker build -t slavik1987/webapp_ui_tests:0.0.1 .
2. docker login
3. docker push slavik1987/webapp_tests:0.0.1

## Docker compose

1. docker compose up/start/down
2. docker-compose up --build   -> rebuild all services
3. docker-compose build test  -> rebuild service

## Docker

1. docker build -t myapp . -> Build docker image
2. docker images -> Check image
3. docker run myapp -> Run image
4. docker stop myapp -> Stop image
5. docker pull selenium/standalone-chrome
6. docker run -d -p 4444:4444 dockerfile | open http://localhost:4444/

## Minikube

1. minikube start --nodes 2
2. minikube stop
3. minikube delete
4. kubectl config use-context minikube
5. kubectl config get-contexts

## Kubernetes
1. kubectl create -f .
2. kubectl apply -f . -> to deploy changes
3. kubectl get deployment
4. kubectl get service
5. kubectl describe deployment nginx-deployment
6. kubectl get pods [-w,]
7. kubectl get nodes
8. kubectl port-forward deployment/webapp 8000:8000
9. kubectl describe pod webapp-ffdcc87bf-b7v2n
10. kubectl delete deployment webapp
11. kubectl delete service webapp
12. kubectl delete pod <id>
13. kubectl run <new_pod_name> --image=slavik1987/webapp_ui_tests:0.0.1
14. kubectl rollout restart deployment
15. kubectl top pod [pods, nods]
16. kubectl get pods webapp-5f67cbcbd6-pjhbm -o jsonpath='{.spec.containers[*].name}' -> containers list
17. kubectl exec -it webapp-66bb95998-lhdtr  -c webapp-tests-positive -- /bin/bash -c "pytest"
18. kubectl logs -f deployment/webapp -p webapp-66bb95998-lhdtr -c webapp-tests-positive
19. kubectl get ing



## Probe, Helthcheck, Volume

apiVersion: v1
kind: Pod
metadata:
  name: kuard
spec:
  volumes:
    - name: "kuard-data"
      nfs:
        server: my.nfs.server.local
        path: "/exports"
  containers:
    - image: gcr.io/kuar-demo/kuard-amd64:blue
      name: kuard
      ports:
        - containerPort: 8080
          name: http
          protocol: TCP
      resources:
        requests:
          cpu: "500m"
          memory: "128Mi"
        limits:
          cpu: "1000m"
          memory: "256Mi"
      volumeMounts:
        - mountPath: "/data"
          name: "kuard-data"
      livenessProbe:
        httpGet:
          path: /healthy
          port: 8080
        initialDelaySeconds: 5
        timeoutSeconds: 1
        periodSeconds: 10
        failureThreshold: 3
      readinessProbe:
        httpGet:
          path: /ready
          port: 8080
        initialDelaySeconds: 30
        timeoutSeconds: 1
        periodSeconds: 10
        failureThreshold: 3


## Autoscaling
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: timeserver
spec:
  minReplicas: 1                 ❶
  maxReplicas: 10                ❷
  metrics:
  - resource:
      name: cpu
      target:
        averageUtilization: 20   ❸
        type: Utilization
    type: Resource
  scaleTargetRef:                ❹
    apiVersion: apps/v1          ❹
    kind: Deployment             ❹
    name: timeserver



