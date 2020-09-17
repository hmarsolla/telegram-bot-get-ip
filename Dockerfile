FROM python:3.7-slim

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./my_ip_please.py ./

VOLUME /app/config.py

CMD ["python","my_ip_please.py"]