# set official base image
FROM python:3.8.2-alpine3.11

# set working directory
WORKDIR /app

# set envirnment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# set psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# set collect static files
RUN python manage.py collectstatic --noinput

# add user to project
RUN adduser -D raselrostock
USER raselrostock

CMD gunicorn djproperty.wsgi:application --bind 0.0.0.0:$PORT
