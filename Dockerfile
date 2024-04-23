FROM python:3.10-slim-buster

# Install required system packages.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
&& rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app
WORKDIR /app
 
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    && rm -rf /requirements.txt
 
COPY . /app
 
EXPOSE 80
 
CMD ["sh", "./runserver.sh"]
