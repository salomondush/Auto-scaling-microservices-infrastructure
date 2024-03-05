# script to build and push the fastapi-app docker image to docker hub

cd ../fastapi-app

docker build -t fastapi-app .
docker tag fastapi-app dushims/fastapi-app
docker push dushims/fastapi-app