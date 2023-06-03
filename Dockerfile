# Base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /code

# Copy requirements file
COPY requirements.txt /code/

# Install project dependencies
RUN pip install -r requirements.txt

# Copy project code
COPY . /code/
