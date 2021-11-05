FROM python:3.9-slim as base

ENV TZ America/Toronto

FROM base as builder
WORKDIR /usr/src/app

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY app.py .

EXPOSE 80
ENTRYPOINT [ "gunicorn" ] 
CMD [ "-w", "2", "--threads", "4", "--access-logfile", "-", "--worker-class", "gthread", "-b", "0.0.0.0:80", "api" ]