FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

COPY ./requirements.txt /work/requirements.txt

WORKDIR /work
RUN pip3 install -r requirements.txt
COPY . /work
ENTRYPOINT ["python3"]
CMD ["run_app.py"]
