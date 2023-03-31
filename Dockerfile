# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN  apt-get update \
  && apt-get install -y wget

RUN apt-get install -y libreoffice-common
RUN apt-get install -y libreoffice-writer
RUN apt-get install -y libreoffice

# Install OpenJDK-11
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;


# install app
COPY load.py  main.py  requirements.txt  save.py  transform.py logger.py download.py /

# final configuration
CMD python3 main.py
