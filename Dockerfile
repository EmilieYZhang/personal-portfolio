# Original: telling Docker to use official CentOS Stream 8 image
# FROM quay.io/centos/centos:stream8

# Improvement: Better base image using python
FROM python:3.9-slim-buster

# installing oython 3.9
# RUN dnf install -y python3.9

# Improvement: Utilize Docker Layer Caching
# cache requirements.txt if file has not changed, reduce build time

# specify /personal-portfolio directory as workdir of container image
WORKDIR /personal-portfolio

COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy all project files into container image at workdir
COPY . .

# specify command that runs when a container is created from this container image
CMD ["flask", "run", "--host=0.0.0.0"]

# specify port exposed from container
EXPOSE 5000

