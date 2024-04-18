FROM python:3.11.6-slim

ENV PYTHONUNBUFFERED=1 

WORKDIR /app 

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc musl-dev libpq-dev python3-dev libffi-dev \
    && apt-get install -y --no-install-recommends mariadb-client libmariadb-dev-compat \
    && pip install --upgrade pip

RUN apt-get install -y --no-install-recommends unixodbc-dev

COPY ./requirements.txt ./ 

RUN pip install -r requirements.txt 

COPY ./ ./ 

# Expone el puerto 8000 al mundo exterior
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]