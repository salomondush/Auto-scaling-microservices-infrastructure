# FastAPI with Huey and Redis Queue Project

This project demonstrates a FastAPI application that uses Huey as a task queue with Redis as the backend, orchestrated using Kubernetes on Docker Desktop for macOS. 

The application models a simple task queue system where users can submit data to be encrypted, and the application will queue the encryption task for processing. The encrypted data is stored in redis using a user-provided key. The user can then retrieve or delete the encrypted data using the same key.

The application is deployed as a Kubernetes deployment and service, with a separate deployment for the Huey consumer and a Redis instance. The project also includes scripts for building and deploying the application.

[**Video Demo***](https://www.loom.com/share/e607319673ee46d597b373e561b50854?sid=73727263-d6ed-423a-a1bf-61df7580210f)

## Prerequisites

1. **macOS**: This guide is tailored for macOS. Some commands might differ on other operating systems.

2. **Docker Desktop**: Install Docker Desktop from [here](https://www.docker.com/products/docker-desktop). Ensure that you have Docker Engine version 18.09.0 or greater so that you can use the Docker Kubernetes cluster.

3. **Kubernetes**: Enable Kubernetes in Docker Desktop. You can do this in the Docker Desktop Preferences under the Kubernetes tab. Check the "Enable Kubernetes" box and apply the changes.

4. **kubectl**: This is a command-line tool for interacting with a Kubernetes cluster. It's included with Docker Desktop, so you don't need to install it separately.

5. **hey**: Install `hey` for load testing (optional). Install it using Homebrew with the command `brew install hey`.

## File Structure

Sure, here's a brief explanation of important files and directories in the project:

- [`fastapi-app/`](command:_github.copilot.openRelativePath?%5B%22fastapi-app%2F%22%5D "fastapi-app/"): This directory contains the FastAPI application code.
  - `Dockerfile`: Instructions for Docker to build an image for the FastAPI application
  - `huey_config.py`: Configuration for Huey, the task queue used in the application.
  - `k8s/`: This directory contains Kubernetes configuration files for deploying the application and its dependencies.
    - `fastapi-deployment.yaml`: A Kubernetes deployment for the FastAPI application.
    - `fastapi-service.yaml`: A Kubernetes service for the FastAPI application.
    - `huey-consumer-deployment.yaml`: A Kubernetes deployment for the Huey consumer.
    - `redis-deployment.yaml`: A Kubernetes deployment for a Redis instance.
    - `redis-service.yaml`: A Kubernetes service for the Redis instance.
  - `scripts/`: This directory contains scripts for building and deploying the application.
    - `docker_build_push.sh`: This script builds app docker image and pushes it to a Docker registry.
    - `deploy_k8s.sh`: This script deploys the application to a Kubernetes cluster including Horizontal Pod Autoscaler (HPA) for fast-api and huey-consumer services
    - `undeploy_k8s.sh`: This script undeploys the application from a Kubernetes cluster.
  - `main.py`: This is the main entry point for the FastAPI application.
  - `requirements.txt`: Lists the Python package dependencies for the application.
  - `tasks.py`: This file defines tasks that can be queued for execution by Huey.
  

## Steps to Run the Project

You can run the project manually by building and pushing the Docker image, then deploying the application to Kubernetes. Alternatively, you can use the provided scripts to automate the process.

1. **Clone the Repository**

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Build and push the Docker image**: Navigate to the [`scripts`](scripts/) directory and run the `docker_build_push.sh` script. Note that you may need to log into your docker hub account:

    ```bash
    cd scripts
    ./docker_build_push.sh
    ```

3. **Deploy the application to Kubernetes**: Still in the [`scripts`](scripts/) directory, run the `deploy_k8s.sh` script:

    ```bash
    ./deploy_k8s.sh
    ```

4. **Verify the deployment**: Check that the services and deployments have been correctly created:

    ```bash
    kubectl get svc
    kubectl get deployments
    kubectl top pods
    kubectl top nodes
    ```

**Note:** You might have to wait around `3 minutes` for services to initialize. Remember to make the scripts executable with `chmod +x script_name.sh` if they aren't already. 

## Simulate Load to Test HPA

Use a load testing tool like `hey` to generate traffic and test the scaling behavior:

```bash
hey -z 3m -c 100 http://localhost:8000/test
```

Adjust the `-z` (duration) and `-c` (concurrency) parameters as needed. Monitor the HPA and pod count during and after the test:

On Docker Desktop, you should observe the number of pods increasing in response to the load, demonstrating the HPA's capability to scale your FastAPI application dynamically. After traffic generation is done, kubernetes will scale down the pods to the minimum number (however, not as fast as it scales up to prevent instability).
