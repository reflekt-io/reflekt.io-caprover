FROM python:3.10-slim-buster

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*
 
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
 
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    && rm -rf /requirements.txt
 
COPY . /usr/src/app
 
EXPOSE 80
 
CMD ["sh", "./runserver.sh"]
