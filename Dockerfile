FROM python:3.10-slim-buster

# Should be in the root path, otherwise it can't load environment variables
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=reflekt_io.settings \
    PORT=8000 \
    WEB_CONCURRENCY=2

# Install system packages required Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
 && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django

# Call env
ARG DB_NAME=${DB_NAME}
ENV DB_NAME=${DB_NAME}

ARG DB_USER=${DB_USER}
ENV DB_USER=${DB_USER}

ARG DB_PASSWORD=${DB_PASSWORD}
ENV DB_PASSWORD=${DB_PASSWORD}

ARG DB_HOST=${DB_HOST}
ENV DB_HOST=${DB_HOST}

ARG DB_PORT=${DB_PORT}
ENV DB_PORT=${DB_PORT}

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy project code
COPY . .

RUN python manage.py collectstatic --noinput --clear

# Database application
RUN python manage.py migrate --noinput

# Run as non-root user
RUN chown -R django:django /app
USER django

# Run application
CMD gunicorn reflekt_io.wsgi:application
