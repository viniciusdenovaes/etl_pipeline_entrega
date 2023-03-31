FROM python:3.8

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
WORKDIR /data_science
COPY main/ /data_science/

ENV PYTHONPATH=$PYTHONPATH:/data_science

ENTRYPOINT ["python", "/data_science/main/main.py"]
