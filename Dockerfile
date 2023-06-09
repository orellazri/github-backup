FROM python:3.9.16-alpine

RUN apk update && apk add git libffi-dev gcc libc-dev linux-headers

RUN mkdir /backups

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
