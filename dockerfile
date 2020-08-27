FROM python:3.8.5-buster

WORKDIR /app/

COPY pyproject.toml poetry.lock /app/
RUN python -m pip install --upgrade pip poetry==1.0
RUN poetry install --no-dev

COPY . /app/
COPY .env /app/

# FIXME:
CMD ["make", "polling"]
