FROM python:3.12-alpine3.18

ENV PYTHONBUFFERED=1

WORKDIR /django

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD gunicorn hotel.wgsi:application --bind 0.0.0.0:8000

EXPOSE 8000