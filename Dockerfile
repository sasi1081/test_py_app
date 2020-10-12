FROM ubuntu:16.04

#MAINTANER Your Name "sasi.1081@gmail.com"

RUN apt-get update -y && \
apt-get install -y python-pip python-dev python3-pip python3.8

WORKDIR /app
RUN  pip3 install wheel

# # COPY requirements.txt /app/requirements.txt
COPY requirements.txt /app/

RUN  pip3 install -r requirements.txt

COPY app.py /app/
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
