# Use an official Python runtime as the base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the necessary packages
RUN apk add --no-cache --virtual .build-deps build-base postgresql-dev \
  && apk add --no-cache --virtual .run-deps libpq \
  && pip install --no-cache-dir -r requirements.txt \
  && apk del .build-deps

# Copy the rest of the application code
COPY . .

# Expose the port
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
