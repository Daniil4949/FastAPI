# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
RUN pipenv install --system --dev

COPY . .

