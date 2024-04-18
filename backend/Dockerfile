FROM python:3.11.6-alpine3.18 

ENV PYTHONUNBUFFERED=1 

WORKDIR /app 

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && apk add --no-cache mariadb-dev\
    && pip install --upgrade pip

RUN apk add --no-cache mariadb-client mariadb-connector-c-dev    

RUN pip install mysqlclient

COPY ./requirements.txt ./ 

RUN pip install -r requirements.txt 

COPY ./ ./ 

# Expone el puerto 8000 al mundo exterior
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 