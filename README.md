# machine_learning_proj
My first ML project
Creating Conda Environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
Conda activate should always be executed in command prompt terminal
```
To setup CI/CD pipleline in heroku, we need to add three informations:

1. Heroku mail: raja.s.dasgupta@gmail.com
2. Heroku API_Key: c9df8ecc-7eda-4598-abfc-386968998824
3. Heroku App name: ml-regression-app-raja

DOCKER build image
```
docker build -t <image_name>:<tagname>
```
Note: Image name for docker must be in lower case only

to list docker images

docker image ls / docker images

to run docker image

docker run -p 5000:5000 -e PORT=5000 <imageID>
docker run -p 5000:5000 -e PORT=5000 1981e860ac16

to check running docker images
docker ps

to stop any docker container
docker stop <container_ID>
