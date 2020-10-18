FROM python:3.8.5-buster

WORKDIR /app/

COPY pyproject.toml poetry.lock .env /app/
RUN python -m pip install --upgrade pip poetry==1.0
RUN poetry install --no-dev

COPY . /app/

# FIXME: webhook here
CMD ["make", "polling"]
